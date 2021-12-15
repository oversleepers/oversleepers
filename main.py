import streamlit as st
import pandas as pd
import plotly.express as px

st.title ("Data Produksi Minyak Mentah dari Berbagai Negara")
st.header ("Tahun 1971-2015")
st.markdown ("""GUI berbasis Streamlit ini berfungsi untuk menggambarkan informasi 
mengenai **_data produksi minyak mentah_** dari berbagai negara di seluruh dunia
dari tahun 1971-2015.""")

##Loading Dataframe - excel
excel_produksi = "produksi_minyak_mentah.xlsx"
sheet1 = "produksi_minyak_mentah"
df = pd.read_excel (excel_produksi, sheet_name=sheet1, usecols="A:D")

# jawaban 1.a
st.subheader ("1. Grafik Jumlah Produksi Minyak Mentah Setiap Tahun")
st.text ("""Anda dapat memilih nama negara yang ingin diketahui beserta rentang waktu 
yang tersedia dibawah ini""")
#-- Streamlit selection
Nama_negara = df['nama_negara'].unique().tolist()
Tahun = df['tahun'].unique().tolist()
Nama_negara_selection = st.multiselect('Nama Negara:',
                                    Nama_negara,
                                    key = "a2",
                                    default = "Australia"
                                    )
Tahun_selection = st.slider('Tahun Produksi:',
                        min_value= min(Tahun),
                        max_value= max(Tahun),
                        value=(min(Tahun),max(Tahun)))

# --- FILTER DATAFRAME berdasarkan selection
mask = (df['tahun'].between(*Tahun_selection)) & (df['nama_negara'].isin(Nama_negara_selection))
number_of_result = df[mask].shape[0]
st.markdown(f'*Jumlah rentang tahun: {number_of_result} tahun*')

# --- GROUP DATAFRAME setelah SELECTION
df_grouped = df[mask].groupby(by=['tahun']).sum()[['produksi']]
df_grouped = df_grouped.rename(columns={'produksi': 'Total Produksi'})
df_grouped = df_grouped.reset_index()

#ploting Bar Chart
bar_chart = px.bar(df_grouped,
                   x='tahun',
                   y='Total Produksi',
                   text='Total Produksi',
                   color_discrete_sequence = ['#F63366']*len(df_grouped),
                   template= 'plotly_white')
st.plotly_chart(bar_chart)

# jawaban 1.b
excel_b = "tahunan.xlsx"
sheet_b = "Sheet1"
df_b = pd.read_excel (excel_b, sheet_name=sheet_b, usecols="A:D")
st.subheader ("2. Grafik Jumlah Produksi Minyak Mentah per 1 Tahun")
st.text ("""Anda dapat memilih nama negara yang ingin diketahui beserta waktu produksi
yang tersedia dibawah ini""")
Nama_negara_b = df_b['nama_negara'].unique().tolist()
Tahun_b = df_b['tahun'].unique().tolist()
#-- Streamlit selection
Nama_negara_selection_b = st.multiselect('Nama Negara:',
                                    Nama_negara_b,
                                    key = "a3",
                                    default = "Canada"
                                    )
Tahun_selection_b = st.slider('Tahun Produksi:',
                        key= "a7",
                        min_value= min(Tahun),
                        max_value= max(Tahun),
                        value=(1980, 1980))

# --- FILTER DATAFRAME berdasarkan selection
mask_b= (df['tahun'].between(*Tahun_selection_b)) & (df['nama_negara'].isin(Nama_negara_selection_b))

# --- GROUP DATAFRAME setelah SELECTION
df_grouped_b = df[mask_b].groupby(by=['tahun']).sum()[['produksi']]
df_grouped_b = df_grouped_b.rename(columns={'produksi': 'Total Produksi'})
df_grouped_b = df_grouped_b.reset_index()

#ploting Bar Chart
bar_chart_b = px.bar(df_grouped_b,
                   x='tahun',
                   y='Total Produksi',
                   text='Total Produksi',
                   color_discrete_sequence = ['#F63366']*len(df_grouped),
                   template= 'plotly_white')
st.plotly_chart(bar_chart_b)

#jawaban 1.c
excel_akumulasi = "akumulasi_produksi.xlsx"
sheet_akumulasi = "akumulasi"
df_akumulasi = pd.read_excel (excel_akumulasi, sheet_name=sheet_akumulasi, usecols="A:F")
st.subheader ("3. Grafik Akumulasi Produksi Minyak Mentah Sepanjang Tahun Masing-Masing Negara")
st.text ("""Ketikkan nama negara pada baris dibawah ini untuk mengetahui total
akumulasi produksi minyak mentah suatu negara""")
#-- Streamlit selection
Nama_negara_a = df_akumulasi['Nama Negara'].unique().tolist()
Nama_negara_a_selection = st.multiselect('Nama Negara:', Nama_negara_a, key = "a1", default="Australia")
mask_a = (df_akumulasi['Nama Negara'].isin(Nama_negara_a_selection))

# --- GROUP DATAFRAME setelah SELECTION
df_a_grouped = df_akumulasi[mask_a].groupby(by=['Tahun 1971-2015']).sum()[["Jumlah produksi"]]
df_a_grouped = df_a_grouped.rename(columns={'Jumlah produksi': 'Total Akumulasi Produksi'})
df_a_grouped = df_a_grouped.reset_index()

#ploting Bar Chart
bar_chart_a = px.bar(df_a_grouped,
                   x='Tahun 1971-2015',
                   y='Total Akumulasi Produksi',
                   text='Total Akumulasi Produksi',
                   color_discrete_sequence = ['#F63366']*len(df_grouped),
                   template= 'plotly_white')
st.plotly_chart(bar_chart_a)

#jawaban 1.d
sheet2 = "data_produksi"
sheet3 = "5_produksi_terbesar"
sheet4 = "5_produksi_terkecil"
sheet5 = "5_produksi_nol"
st.subheader ("4. Negara dengan produksi Terbesar, Terkecil dan Sama Dengan Nol")
st.text ("""Dibawah ini adalah data produksi Minyak Mentah dari berbagai Negara""")
#dataproduksi
df2 = pd.read_excel (excel_produksi, sheet_name=sheet2, usecols="A:F")
df3 = pd.read_excel (excel_produksi, sheet_name=sheet3, usecols="A:H")
df4 = pd.read_excel (excel_produksi, sheet_name=sheet4, usecols="A:H")
df5 = pd.read_excel (excel_produksi, sheet_name=sheet5, usecols="A:F")
st.dataframe(df2)
#dataproduksiterbesar
st.text ("""Berikut adalah daftar 5 negara dengan total produksi terbanyak sepanjang tahun""")
st.dataframe(df3)
#dataproduksiterkecil
st.text ("""Dibawah ini adalah 5 negara dengan total produksi paling sedikit sepanjang Tahun""")
st.dataframe(df4)
#dataproduksinol
st.text ("""Sementara itu, berikut data beberapa negara yang tidak produksi minyak mentah""")
st.dataframe(df5)