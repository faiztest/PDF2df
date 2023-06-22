import streamlit as st
import pdfplumber
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(
     page_title="PDFs to dataframe",
     page_icon="https://digilib.polteknuklir.ac.id/perpus/images/default/logo.png",
     layout="wide"
)

@st.cache_data(experimental_allow_widgets=True)
def convert(uploaded_files):
    data = []
    for file in uploaded_files:
        with pdfplumber.open(file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
        data.append({"File Name": file.name, "Text": text})
    return data

@st.cache_data()
def split(extracted_data):
    df = pd.DataFrame(extracted_data)
    df = df.replace(r'\n',' ', regex=True) 
    pattern = '|'.join(word_list)
    split_df = df['Values'].str.split(pattern, expand=True)
    result_df = pd.concat([rd, split_df], axis=1)
    new_columns = ['File Name', 'Text', 'intro'] + word_list
    result_df.columns = new_columns
    return result_df    


st.title("PDF to Text Converter")
st.header("Upload PDF Files")

uploaded_files = st.file_uploader("Choose files", type=['pdf'], accept_multiple_files=True)
text_search = st.text_input("Split your PDFs into parts. Separate words (cAsE sEnSiTiVe) by semicolons (;)")
word_list = [keyword.strip() for keyword in text_search.split(";")]
st.write(word_list)

if st.button("Convert"):
    extracted_data = convert(uploaded_files)
    result_df = split(extracted_data)
    
    if not df.empty:
        st.subheader("Extracted Text")
        st.dataframe(df)
