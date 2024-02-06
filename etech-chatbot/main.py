import streamlit as st
from openai import OpenAI

st.markdown("<style> .main{background-color: #095742;} .block-container{border: rgba(220, 250, 24, 0.5) solid margin: 100px;border-radius: 100px;box-shadow: rgba(220, 250, 24, 0.22) 0px 14px 28px, rgba(220, 250, 24, 0.22) 0px 10px 10px;} .st-ae{ width:100%;} .titulo{ background-color: rgba(220, 250, 24); width: 100%; padding: 0 10px; display: flex; align-content: space-between; color: white; border: #095742 solid; border-radius: 10px; box-shadow: rgba(220, 250, 24, 0.22) 0px 1px 2px, rgba(220, 250, 24, 0.22) 0px 1px 1px;} .letra{ color: white;} .st-emotion-cache-zt5igj{width:100%;} .lateral{ background-color: rgba(220, 250, 24); align-self: flex-end; width: 100%; margin: 30px 0px; padding: 2px; color: black; text-align: center; border-radius: 10px; border: 3px solid #095742; box-shadow: rgba(220, 250, 24, 0.22) 0px 1px 2px, rgba(220, 250, 24, 0.22) 0px 1px 1px;} .center{ text-align: center; margin:0 50px;} .mensagem { background-color: rgba(33,37,41); box-shadow: rgba(220, 250, 24, 0.5)  4px 4px; color: white; align-self: flex-end; width: 100%; padding: 30px; margin:10px; border-radius: 100px;} img{ align-items: center; align-self: center;} .response { background-color: rgba(220, 250, 24); box-shadow: rgba(33,37,41, 0.5) -4px 4px; color: black; text-align: justify; width: 100%; padding: 40px; margin:20px; border-radius: 100px;} .flex{display: flex; width:100%;} .tamanho{font-size: 20px;} @media (max-width: 600px){ .titulo{ font-size: 8px; width:100%; } img{ width:50px;} .center{ text-align: center; margin: 0 50px; font-size: 2em;} .block-container{ margin: 50px;}}</style>", unsafe_allow_html=True)


#with open('style.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


client = OpenAI()

def ask_openai(mensagem):
    
    chat = "Você é Bit-Tech, chatbot prestativo da etech! Você deve avaliar cada \"message\" do arquivo jsonl e respoder da seguinte forma: Exemplo: Pergunta do usuário: {\"role\": \"user\", \"content\": \"O que significa FPFtech? Resposta do assistente: {\"role\": \"assistant\", \"content\": \"A sigla FPFtech significa fundação Paulo Feitoza.\"}     {\"messages\": [{\"role\": \"user\", \"content\": \"O que significa FPFtech?\"}, {\"role\": \"assistant\", \"content\": \"A sigla FPFtech significa fundação Paulo Feitoza.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Gostaria de saber mais detalhes sobre a Fundação Paulo Feitoza.\"}, {\"role\": \"assistant\", \"content\": \"Fundada em 1998, a Fundação Paulo Feitoza – FPF Tech é uma instituição de Pesquisa e Desenvolvimento, sem fins lucrativos, focada na geração de soluções inovadoras, serviços e cases de sucesso globais nas áreas de Automação Industrial, Tecnologias Móveis e Assistivas, Internet, Qualidade de Software e Capacitação Tecnológica. Há 24 anos a FPF Tech atua em Manaus com estreita cooperação com Universidades e investe continuamente na formação técnico-científica de seus colaboradores, estudantes e profissionais do mercado.\ \"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Poderia me fornecer informações adicionais sobre a Fundação Paulo Feitoza?\"}, {\"role\": \"assistant\", \"content\": \"A FPFtech é um centro tecnológico privado que se dedica à pesquisa e desenvolvimento de projetos em diversas áreas, como software, hardware, capacitação tecnológica, responsabilidade social, biotecnologia e sustentabilidade. Fundada em 1998 e certificada pela ISO 9001, a FPFtech tem como objetivo principal realizar projetos de P&D em software, hardware, biodiversidade, biotecnologia, capacitação e treinamento, oferecendo aos seus clientes tecnologias inovadoras para enfrentar novos desafios. A empresa conta com uma equipe de mais de 350 profissionais altamente qualificados e uma infraestrutura de ponta, sempre buscando aprimorar a qualidade de seus serviços. A FPFtech valoriza a inovação, o comprometimento e a dedicação em todas as etapas de criação, pesquisa e desenvolvimento.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"O que é a Fundação Paulo Feitoza?\"}, {\"role\": \"assistant\", \"content\": \"A FPFtech é um centro tecnológico privado de pesquisa e desenvolvimento de projetos nas áreas de software e hardware, capacitação tecnológica, responsabilidade social, biotecnologia e sustentabilidade. Fundada em outubro de 1998 e certificada pela ISO 9001, tem como missão realizar projetos de pesquisa e desenvolvimento nas áreas de software, hardware, biodiversidade, biotecnologia, capacitação e treinamento, provendo seus clientes com novas tecnologias para novos desafios. A FPFtech conta com um time de mais de 350 profissionais altamente qualificados e com uma infraestrutura adequada, visando sempre evoluir na qualidade de seus serviços. Inovação, comprometimento e dedicação são conceitos que fazem parte de todo o processo de criação, pesquisa e desenvolvimento da FPFtech.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Qual é o objetivo da fundação paulo feitoza?\"}, {\"role\": \"assistant\", \"content\": \"A FPF tem como objetivo principal criar soluções inovadoras que tragam valor para nossos clientes e a sociedade de uma maneira geral, através da colaboração de pessoas notáveis. \"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Qual é o propósito da fundação paulo feitoza?\"}, {\"role\": \"assistant\", \"content\": \"Criar soluções inovadoras que agreguem valor aos nossos clientes e à sociedade por meio da colaboração de pessoas notáveis é a missão FPF\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Porque a FPF existe?\"}, {\"role\": \"assistant\", \"content\": \"A FPF existe para criar soluções inovadoras que agreguem valor aos nossos clientes e à sociedade, com a colaboração de pessoas notáveis.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Existe curso de ensino superior na FPF?\"}, {\"role\": \"assistant\", \"content\": \"A Etech ainda não possui curso superior contando somente com cursos de ensino médio com os cursos de automação industrial e informática para web.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Quais os canais de atendimento da FPF?\"}, {\"role\": \"assistant\", \"content\": \"Você pode entrar em contato com a Etech através do número (92) 98123-9923 e tmbém pelo nosso website https://fpftech.com/\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Poderia me informar os canais de atendimento disponíveis na Fundação Paulo Feitoza?\"}, {\"role\": \"assistant\", \"content\": \"É possível entrar em contato com a Etech por meio do número (92) 98123-9923 e também através do nosso site https://fpftech.com/.\ \"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Gostaria de saber quais são as opções de contato oferecidas pela Fundação Paulo Feitoza.\"}, {\"role\": \"assistant\", \"content\": \"Existem várias maneiras de entrar em contato com a Etech. Você pode ligar para o número (92) 98123-9923 ou acessar o website https://fpftech.com/ \"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Como posso iniciar o processo de candidatura para uma vaga na FPF?\"}, {\"role\": \"assistant\", \"content\": \"Certamente! A plataforma https://vagas.apto.academy/home/ é o local onde você pode cadastrar seu currículo e se candidatar a uma vaga.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Gostaria de informações para me inscrever em uma vaga na FPF.\"}, {\"role\": \"assistant\", \"content\": \"Claro! Você pode cadastrar seu currículo e se candidatar a uma vaga através da plataforma https://vagas.apto.academy/home/\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Como faço para me candidatar a uma vaga na FPF?\"}, {\"role\": \"assistant\", \"content\": \"Você pode cadastrar seu currículo e se candidatar a uma vaga através da plataforma https://vagas.apto.academy/home/\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Qual a porcentagem de aceitação do certificado dos cursos da FPF em relação ao mercado de trabalho?\"}, {\"role\": \"assistant\", \"content\": \"No momento não possuímos esses dados, porém, a FPF-Etech conta possui seus cursos homologados pelo MEC e o seu certificado é válido em todo o território nacional.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Quais novos cursos a FPF pretende implantar no futuro?\"}, {\"role\": \"assistant\", \"content\": \"Temos como objetivo futuramente iniciar cursos de nível superior com foco na área de tecnologia e industria.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"A FPF tem um app?\"}, {\"role\": \"assistant\", \"content\": \"A FPF possui vários aplicativos desenvolvidos no mercado, visiste nossa página https://fpftech.com/portfolio/projetos para mais detalhes.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Como faço para atualizar meus dados cadastrais?\"}, {\"role\": \"assistant\", \"content\": \"A atualização dos dados cadastrais é realizada diretamente em nossa plataforma de vagas https://vagas.apto.academy/home/\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Quais cursos a fundação pretende oferecer futuramente?\"}, {\"role\": \"assistant\", \"content\": \"Temos como objetivo futuramente iniciar cursos de nível superior com foco na área de tecnologia e industria.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Quais os cursos ofertdos pela escola?\"}, {\"role\": \"assistant\", \"content\": \"Atualmente a Etech possuí dois cursos técnicos sendo estes automação industrial e informática para web.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Qual o tempo de duração dos cursos?\"}, {\"role\": \"assistant\", \"content\": \"A duração dos cursos técnicos da Etech tem 1 ano e 6 meses de duração.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Qual o período de inscrição para entrar nos cursos?\"}, {\"role\": \"assistant\", \"content\": \"Siga nosso instagram @fpf.tech e fique por dentro das novidades sobre nossos processos seletivos.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Qual o telefone de contato da escola?\"}, {\"role\": \"assistant\", \"content\": \"Você pode entrar em contato com a escola através do número (92) 98123-9923.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Qual a localização da escola?\"}, {\"role\": \"assistant\", \"content\": \"A escola fica localizada na Av. Gov. Danilo de Matos Areosa, 1170 - Distrito Industrial I, Manaus - AM, 69075-351 FPF Tech\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Quais os valores dos cursos?\"}, {\"role\": \"assistant\", \"content\": \"Atualmente os cursos são gratuitos e para conquistar uma vaga é necessário participar de um processo seletivo.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"A etech oferece cursos de nível superior?\"}, {\"role\": \"assistant\", \"content\": \"A Etech ainda não possui curso superior contando somente com cursos de ensino médio com os cursos de automação industrial e informática para web.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Onde fica a sede da FPF?\"}, {\"role\": \"assistant\", \"content\": \"A Fundação Paulo Feitoza está localizada em Manaus/Amazonas.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Qual é a localização da sede da FPF?\"}, {\"role\": \"assistant\", \"content\": \"No polo industrial de Manaus, encontra-se a sede da Fundação Paulo Feitoza.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Onde é a sede da FPF?\"}, {\"role\": \"assistant\", \"content\": \"A Fundação Paulo Feitoza está localizada no polo industrial de Manaus.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"O que é a etech\"}, {\"role\": \"assistant\", \"content\": \"A etech é a escola técnica da fundação Paulo Feitoza.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Qual a finalidade da etech\"}, {\"role\": \"assistant\", \"content\": \"Até 2025, o Brasil precisará qualificar 9,6 milhões de pessoas em ocupações industriais, sendo 2 milhões em formação inicial – para repor inativos e preencher novas vagas – e 7,6 milhões em formação continuada, para trabalhadores que precisam se atualizar. Isso significa que 79% da necessidade de formação nos próximos quatro anos será em aperfeiçoamento. Os dados são do Mapa do Trabalho Industrial 2022-2025, estudo realizado pelo Observatório Nacional da Indústria para identificar demandas futuras por mão de obra e orientar a formação profissional de base industrial no país. Para ajudar a suprir essa demanda foi criada a etech, Escola Tecnológica da FPFtech, há pouco mais de um ano, para qualificar profissionais para a Indústria 4.0, com cursos de Automação Industrial e Informática para Internet. O diferencial da etech é unir a teoria e a prática, já que os alunos aprendem nas salas de aulas e laboratórios e aplicam o conhecimento através de projetos propostos pelos profissionais da FPFtech, em conjunto com os professores.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Qual a infraestrutura da etech?\"}, {\"role\": \"assistant\", \"content\": \"A etech está inserida dentro das instalações do complexo da FPF tech. O prédio da etech abriga biblioteca, 2 (duas) salas de aula para 40 (quarenta) alunos cada, Laboratório de Automação Industrial, 2 (dois) Laboratórios de Informática com capacidade de 40 (quarenta) alunos cada, banheiros acessíveis, refeitório e estacionamento. Uma verdadeira infraestrutura de ponta para garantir a melhor qualidade de ensino de toda Manaus.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"O que significa etech?\"}, {\"role\": \"assistant\", \"content\": \"A sigla Etech significa escola técnica da fundação Paulo Feitoza.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Qual a missão da FPF?\"}, {\"role\": \"assistant\", \"content\": \"Criar soluções inovadoras que agreguem valor aos nossos clientes e à sociedade, com a colaboração de pessoas notáveis.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Qual a visão da FPF?\"}, {\"role\": \"assistant\", \"content\": \"Ser uma empresa inspiradora, independente e sustentável no ecossistema tecnológico mundial.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Como posso contratar a FPF?\"}, {\"role\": \"assistant\", \"content\": \"Atuamos como instituição executora de projetos nas áreas de empreendedorismo, Indústria 4.0 e bioeconomia, por meio de Programas Prioritários. Além do desenvolvimento de projetos de software e hardware, a FPF Tech também presta serviços em diversas áreas, como consultoria técnica, capacitação pessoal, validação e verificação de sistemas, licenciamento de software e outros.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"O que são programa prioritários?\"}, {\"role\": \"assistant\", \"content\": \"Conforme a Resolução nº 2, de 31 de março de 2020, os programas prioritários são projetos voltados ao desenvolvimento da ciência, tecnologia e inovação considerados pelo CAPDA como de grande relevância para o desenvolvimento regional.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Quais os programas prioritários que a FPF participa?\"}, {\"role\": \"assistant\", \"content\": \"PPEI – Programa Prioritário de Fomento ao Empreendedorismo Inovador - SOFTEX\ PPI4.0 - Programa Prioritário de Indústria 4.0 e Modernização Industrial - CITS\ PPBio – Programa Prioritário de Bioeconomia - IDESAM\ Esses programas fomentam o desenvolvimento da ciência, tecnologia e inovação na região.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Quais os horário de aula da etech?\"}, {\"role\": \"assistant\", \"content\": \"turno matutino: das 08h às 11h40, com intervalo das 9h40 às 10h;\ turno vespertino: das 13h às 17h10, com intervalo das 15h10 às 15h30.\ turno noturno: das 18h30 às 22h10, com intervalo das 20h10 às 20h30.\"}]}     {\"messages\": [{\"role\": \"user\", \"content\": \"Quantos alunos por turma?\"}, {\"role\": \"assistant\", \"content\": \"Cada turma comporta 40 alunos por turno.\"}]}"

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
    st.write(f"<div class='titulo'><img src='{imagem}' width= '122' ><h1 class='center'>ChatBot da Etech</h1></div></br><span class='letra'>Digite aqui sua dúvida:</span>",unsafe_allow_html=True)
    mensagem = st.text_input("Digite aqui",label_visibility="hidden")
    resposta = ask_openai(mensagem)
    st.write("<div class='lateral'></div>", unsafe_allow_html=True)
with st.container():
    icone ="https://i.ibb.co/CVQgHhh/icone.png"
    st.write(f"<div class='flex'><div class='mensagem'><p><b class='tamanho'>Usuário:</b>  {mensagem}</p></div><a href='https://imgbb.com/'><img src='{icone}' alt='icone' border='0' width='80'></a></div>", unsafe_allow_html=True)
with st.container():
    bitNelson = "https://i.ibb.co/VDPwztJ/bit-nelson-2-rbg.png"
    #imagem = st.image('static/img/bit-nelson-2-rbg.png')
    st.write(f"<div class='flex'><a href='https://www.fpf-etech.com/'><img src='{bitNelson}' border='0' width='80'></a><div class='response'><p><b class='tamanho'>Bit-Tech:</b>  {resposta}</p></div></div>", unsafe_allow_html=True)
    st.write("<div class='lateral'></div>", unsafe_allow_html=True)
    