from groq import Groq
import streamlit as st 
import time
import os

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

st.title("Sexta-Feira") 
pergunta  = st.text_input('pergunta:')
if st.button('enviar'):
    # if pergunta.strip():
        reposta =  client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        temperature=0.7,

        messages=[
        {
        'role':'system',
        'content':"Você é a Sexta-Feira, uma desenvolvedora de sfotware que domina todas linguagens de programação simpática e bem-humorada. Solta uma piada leve ou um comentário engraçado de vez em quando, mas nunca enrola: vai direto ao ponto, explica com clareza e prioriza respostas objetivas e curtas. Evita textos longos e explicações desnecessárias — resolve o problema primeiro, humor vem como tempero, não como enrolação."
        },
        {
            'role':'user',
            'content': pergunta
            
        }
        ]
        )

        st.text(reposta.choices[0].message.content)
        time.sleep(0)
