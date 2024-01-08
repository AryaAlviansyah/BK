import streamlit as st

def main():
    st.title("Aplikasi Streamlit di VSCode")
    
    long_paragraph = """
    Ini adalah paragraf panjang yang berisi banyak teks. 
    Anda dapat menambahkan sebanyak yang Anda inginkan 
    untuk menampilkan teks dalam satu paragraf.
    """
    
    st.markdown(long_paragraph)

if _name_ == "_main_":
    main()
