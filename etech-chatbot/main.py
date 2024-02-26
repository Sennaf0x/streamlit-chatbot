import streamlit as st
from openai import OpenAI
from Chat import chat

with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

client = OpenAI()

def ask_openai(mensagem):
    
    if(mensagem == ""):
        resposta = "Como posso ajudá-lo?"
        return resposta
    
    else: 
        completion = client.chat.completions.create(
            model="ft:gpt-3.5-turbo-0613:personal:cb-etech:8ZwbruP2",
            
                messages=[
                    {
                    "role": "system",
                    "content": f"{chat}"
                    },
                    {
                    "role": "user",
                    "content": mensagem
                    }
                ],
                temperature=1,
                max_tokens=200,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
                )
            
        answer = completion.choices[0].message.content
        print(answer)
        return answer
            
with st.container():
    
    imagem = "https://assets-global.website-files.com/620ba2c48ef2a94e3ba42435/65317f284897f296c6b25e12_Ativo%2016%404x.png"
    
    st.write(f'''
                <div class='titulo'>
                    <img src='{imagem}' width= '122' >
                    <h1 class='center'>ChatBot da Etech</h1>
                </div>
                </br>
                <span class='letra'>Digite aqui sua dúvida:</span>
             ''',unsafe_allow_html=True)
    
    
    mensagem = st.text_input("Digite aqui:",label_visibility="hidden")
    resposta = ask_openai(mensagem)
    st.write("<div class='lateral'></div>", unsafe_allow_html=True)
    
with st.container():
    
    icone ="https://i.ibb.co/CVQgHhh/icone.png"
    st.write(f'''
                <div class='flex'>
                    <div class='mensagem'>
                        <p><b class='tamanho'>Usuário:</b>  {mensagem}</p>
                    </div>
                    <a href='https://imgbb.com/'>
                    <img src='{icone}' alt='icone' border='0' width='80'>
                    </a>
                </div>
            ''', unsafe_allow_html=True)
    
with st.container():
    bitNelson = "https://i.ibb.co/VDPwztJ/bit-nelson-2-rbg.png"
    #imagem = st.image('static/img/bit-nelson-2-rbg.png')
    st.write(f'''
                <div class='flex'>
                    <a href='https://www.fpf-etech.com/'>
                    <img src='{bitNelson}' border='0' width='80'>
                    </a>
                    <div class='response'>
                        <p><b class='tamanho'>Bit-Tech:</b>  {resposta}</p>
                    </div>
                </div>
            ''', unsafe_allow_html=True)
    
    st.write("<div class='lateral'></div>", unsafe_allow_html=True)
    