import streamlit as st
from mypages.page_1 import func_page_1
from mypages.page_2 import func_page_2

def main():
    st.sidebar.subheader('Page Selection')
    page_selection = st.sidebar.selectbox('Please select a page',['Main Page','Page 1', 'Page 2'])
    pages_main = {
        'Main Page': main_page,
        'Page 1': run_page_1,
        'Page 2': run_page_2
    }

    pages_main[page_selection]()

def main_page():
    st.title('Main Page')

def run_page_1():
    func_page_1()

def run_page_2():
    func_page_2()

if __name__ == '__main__':
    main()
