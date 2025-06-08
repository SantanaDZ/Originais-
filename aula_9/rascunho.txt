import streamlit as st 

# Markdown
'''

# Olá, eu sou o André Santana Martins 👋
---
## Sobre Mim

Sou Técnico de Informática na **Prefeitura de Belo Horizonte** e estou cursando **Análise e Desenvolvimento de Sistemas** na **UNIFENAS**, atualmente no 3º/5º período. Buscando aprimorar minhas habilidades e expandir meu conhecimento, estou me formando como **Desenvolvedor Full Stack** através da **Infinity School**.

Com foco nas principais linguagens de programação e tecnologias do mercado, estou sempre em busca de novos desafios e oportunidades para crescer como desenvolvedor.
'''
st.image('profile.jpeg', width=180)

'''        

---

## Experiência Profissional na área de tecnologia

2020 - 2022 

Estágio de Técnico de TI - Prodabel

'''
st.image('PRODABEL.png', width=180)
'''

2022 - Atualmente

Técnico de TI - Zoom Tecnologia 
'''
st.image('zoom.png', width=180)
'''
---

## Tecnologias que estou aprendendo e utilizando:

- **Frontend**: HTML, CSS, JavaScript, React
- **Backend**: Node.js, Express
- **Banco de Dados**: MySQL, MongoDB
- **Ferramentas**: Git, GitHub, Docker
- **Metodologias Ágeis**: Scrum, Kanban

---

# Projetos

Confira alguns dos meus projetos abaixo:

- [Cadastro de Produtos](https://github.com/SantanaDZ/Cadastro-de-Produtos) – Sistema de cadastro de produtos com interface gráfica.
- [Auto Cert](https://github.com/SantanaDZ/AUTO-CERT) – Gerador automático de certificados personalizados.
- [Curso Infinity](https://github.com/SantanaDZ/CURSO-INFINITY) – Projetos produzidos no curso Infinty.

---

# 📫 Como me encontrar

- **E-mail**: [andresantmartins@outlook.com](mailto:andresantmartins@outlook.com)
- **LinkedIn**: [André Santana Martins](https://www.linkedin.com/in/andre-santana-martins-b8b619355)
- **Telefone**: +55(31)98438-2472
---

Estou sempre aberto a novas oportunidades e colaborações. Sinta-se à vontade para entrar em contato! 😄

'''

st.text_input('Envie uma mensagem: ')
st.button('Enviar')

mensagens = []
