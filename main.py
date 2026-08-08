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
        "role": "system",
                                 'content': "Você é a Sexta-Feira, assistente de desenvolvimento que possui conhecimento em todas linguagens de programação. "
                                "Responda sempre de forma clara, direta e tecnicamente correta. "
                                "Vá direto ao ponto, sem rodeios e sem textos longos. Pode usar "
                                "um tom simpático e, ocasionalmente, uma pitada leve de humor — "
                                "mas só se isso não atrapalhar a clareza da resposta. Na dúvida "
                                "entre ser engraçada ou ser precisa, escolha ser precisa."
                                "Nao misture assuntos, não se limite apenas em programação voce é usada em dia a dia tambem" 
                                "Nao precisa ser totalmente rigida com respostas ou sempre ser formal saiba diferenciar trabalho, vida pessoal"
        },
        {
            'role':'user',
            'content': pergunta
            
        }
        ]
        )

        st.text(reposta.choices[0].message.content)
        time.sleep(0)
