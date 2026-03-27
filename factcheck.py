from groq import Groq
import streamlit as st

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def ai_fact_check(text):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",   # 🔥 best model
            messages=[
                {
                    "role": "system",
                    "content": "You are a fact-checking assistant. Tell whether the statement is TRUE or FALSE and explain briefly."
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            max_tokens=150
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"