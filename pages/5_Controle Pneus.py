import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt

st.set_page_config(page_title="Pneus 2° Vida", page_icon="🛞")
df = pd.read_excel("MottuSâoLuís.xlsx",sheet_name="PneusSegundaVida")
st.title('Análise de Pneus - Borracharia')
st.write('Dados dos pneus recolhidos em diferentes situações:')
st.dataframe(df)

situacao_total = df["Quantidade"].sum()
situacao_count = df.groupby('Situação')['Quantidade'].sum()
st.write("Quantidade total de pneus por situação:")
st.write(situacao_count)
st.write(f"Quantidade total de pneus por situação = {situacao_total}")

fig, ax = plt.subplots(figsize=(12, 8))  
bars = ax.bar(situacao_count.index, situacao_count.values, color=['green', 'red', 'yellow'])
ax.set_title('Quantidade de Pneus por Situação')
ax.set_xlabel('Situação')
ax.set_ylabel('Quantidade de Pneus')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, yval, ha='center', va='bottom')

st.pyplot(fig)


df['Total Pneus'] = df['Tipo Pneu Dianteiro'] + df['Tipo Pneu Traseiro']
quantidade_por_semana = df.groupby('Semana')['Total Pneus'].sum().reset_index()

st.title("Análise da Quantidade Total de Pneus por Semana")

st.subheader("Tabela de Quantidade de Pneus por Semana")
st.write(quantidade_por_semana)

fig, ax = plt.subplots(figsize=(10, 8))
bars = ax.bar(quantidade_por_semana['Semana'], quantidade_por_semana['Total Pneus'], color='green')
ax.set_xlabel('Semana')
ax.set_ylabel('Quantidade Total de Pneus')
ax.set_title('Quantidade Total de Pneus por Semana')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 1, yval, ha='center', va='bottom')

st.pyplot(fig)

total_dianteiro = df['Tipo Pneu Dianteiro'].sum()
total_traseiro = df['Tipo Pneu Traseiro'].sum()

st.write("Quantidade Total de Pneus por Tipo:")
st.write(f"Total Pneus Dianteiros: {total_dianteiro}")
st.write(f"Total Pneus Traseiros: {total_traseiro}")

fig, ax = plt.subplots(figsize=(10, 8))
bars = ax.bar(['Dianteiro', 'Traseiro'], [total_dianteiro, total_traseiro], color=['blue', 'orange'])
ax.set_xlabel('Tipo de Pneu')
ax.set_ylabel('Quantidade Total')
ax.set_title('Quantidade Total de Pneus por Tipo')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 1, yval, ha='center', va='bottom')

st.pyplot(fig)