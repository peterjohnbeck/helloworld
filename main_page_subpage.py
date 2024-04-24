import streamlit as st
from mypages.page_1 import func_page_1
from mypages.subpages_1.subpage_1_1 import func_subpage_1_1
from mypages.subpages_1.subpage_1_2 import func_subpage_1_2

def main():
    st.sidebar.subheader('Page Selection')
    page_selection = st.sidebar.selectbox('Please select a page', ['Main Page','Page 1'])
    pages_main = {
            'Main Page': main_page,
            'Page 1': run_page_1
    }

    subpages_page_1 = {
            'Subpage 1.1': run_subpage_1_1,
            'Subpage 1.2': run_subpage_1_2
    }

    if page_selection == 'Main Page':
        # run selected page
        pages_main[page_selection]()
    
    elif page_selection == 'Page 1':
        st.sidebar.subheader('Subpage selection')
        subpage_selection_1 = st.sidebar.selectbox("Please select a subpage",tuple(subpages_page_1.keys()))

        # run selected subpage
        subpages_page_1[subpage_selection_1]()

def main_page():
    st.title('Main Page')
    st.subheader("Main page subheader")

def run_page_1():
    func_page_1()
   

def run_subpage_1_1():
    func_subpage_1_1()

def run_subpage_1_2():
    func_subpage_1_2()

if __name__ =='__main__':
    main()

