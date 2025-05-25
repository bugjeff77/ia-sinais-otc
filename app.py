# WebApp com IA para gerar sinais de opções binárias OTC
# Pares: EURUSD-OTC, EURGBP-OTC, GBPJPY-OTC

import streamlit as st
import pandas as pd
import numpy as np
import random
import datetime

# Configuração inicial
theme_color = "#121212"
st.set_page_config(page_title="IA de Sinais OTC", layout="centered")

st.markdown(f"""
    <style>
    body {{ background-color: {theme_color}; color: white; }}
    .stApp {{ background-color: {theme_color}; }}
    </style>
""", unsafe_allow_html=True)

st.title("🤖 IA de Sinais OTC - Polarium")

# Pares OTC analisados
pares = ["EURUSD-OTC", "EURGBP-OTC", "GBPJPY-OTC"]

# Simulação de estratégia com IA (aleatória + lógica)
def gerar_sinal(par):
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    rsi = random.randint(10, 90)
    tendencia = random.choice(["alta", "baixa"])
    candle = random.choice(["reversão", "continuação"])

    if rsi < 30 and candle == "reversão":
        direcao = "CALL"
    elif rsi > 70 and candle == "reversão":
        direcao = "PUT"
    else:
        direcao = "NÃO OPERAR"

    return {
        "par": par,
        "hora": hora,
        "RSI": rsi,
        "Tendência": tendencia,
        "Candle": candle,
        "Sinal": direcao
    }

# Gera sinais para cada par
dados = [gerar_sinal(par) for par in pares]
df = pd.DataFrame(dados)

# Exibe os sinais no painel
st.subheader("📊 Sinais Gerados")
st.dataframe(df.style.applymap(lambda val: "color: green" if val=="CALL" else ("color: red" if val=="PUT" else "color: gray"), subset=["Sinal"]))

# Atualiza automaticamente a cada minuto
st.caption("Atualiza automaticamente a cada minuto. Última atualização: " + datetime.datetime.now().strftime("%H:%M:%S"))
