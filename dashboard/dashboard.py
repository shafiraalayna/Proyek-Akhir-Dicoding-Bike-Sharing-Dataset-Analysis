import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import datetime

sns.set(style='white')

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4665/4665338.png")
    st.header("Bike Sharing")
    st.subheader("Rentang Waktu")
    st.subheader("Januari 2011 - Desember 2012")
    
    

st.header('Proyek Akhir Dicoding: Bike Sharing Dataset Analysis 🚲🔍')



#Perkembangan peminjaman sepeda tahun 2011
st.subheader('Perkembangan Peminjaman Sepeda Tahun 2011')
df1 = pd.read_csv("dashboard/perkembangan2011.csv")

total_peminjaman_1 = df1["count"].sum()
st.metric("Total Peminjaman Sepeda Tahun 2011", value=total_peminjaman_1)

fig, ax = plt.subplots(figsize=(16, 10))
ax.bar(
    df1["month"],
    df1["count"],
    linewidth=3,
    color="#ee3a8c"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='x', rotation=45)

st.pyplot(fig)



# Perkembangan Peminjaman Sepeda Tahun 2012
st.subheader('Perkembangan Peminjaman Sepeda Tahun 2012')
df2 = pd.read_csv("dashboard/perkembangan2012.csv")

total_peminjaman_2 = df2["count"].sum()
st.metric("Total Peminjaman Sepeda Tahun 2012", value=total_peminjaman_2)

fig, ax = plt.subplots(figsize=(16, 10))
ax.bar(
    df2["month"],
    df2["count"],
    linewidth=3,
    color="#ee3a8f"
)
ax.tick_params(axis='x', rotation=45)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)





#Dampak Cuaca Terhadap Peminjaman Sepeda Selama 2 Tahun
st.subheader("Dampak Cuaca Terhadap Peminjaman Sepeda Selama 2 Tahun")
df3 = pd.read_csv("dashboard/dampakcuaca.csv")

col1, col2, col3 = st.columns(3)

with col1:
    total_clear = df3[df3["weather"] == 'Clear']
    st.metric("Total Peminjam Saat Cerah", value=total_clear["count"])

with col2:
    total_mist = df3[df3["weather"] == 'Mist']
    st.metric("Total Peminjam Saat Berkabut", value=total_mist["count"])

with col3:
    total_snow = df3[df3["weather"] == 'Light Snow']
    st.metric("Total Peminjam Saat Salju Ringan", value=total_snow["count"])

fig, ax = plt.subplots(figsize=(20, 6))
colors = ["#e03a69", "#e66187", "#ec89a5"]
sns.barplot(
    y="weather", 
    x="count",
    orient="h",
    data=df3.sort_values(by="count", ascending=False),
    palette=colors,
    ax=ax
)
ax.set_title("Peminjaman Sepeda Tergantung Cuaca", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)
