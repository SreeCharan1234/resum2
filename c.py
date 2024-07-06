import streamlit as st
from streamlit_option_menu import option_menu
import datetime
import os
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

os.getenv("AIzaSyBIBVb-0Z0QwaucMGOGy8-j_RM22X-4-lE")
genai.configure(api_key="AIzaSyBIBVb-0Z0QwaucMGOGy8-j_RM22X-4-lE")
t=[ "Python", "Java", "C++", "JavaScript", "Ruby", "PHP", "Swift", "Kotlin", 
    "C#", "Go", "R", "TypeScript", "Scala", "Perl", "Objective-C", "Dart", 
    "Rust", "Haskell", "MATLAB", "SQL", "HTML/CSS", "React", "Angular", "Vue.js", 
    "Node.js", "Django", "Flask", "Spring", "ASP.NET", "Ruby on Rails"]
st.set_page_config(page_title="Resume", page_icon='chart_with_upwards_trend', layout="wide", initial_sidebar_state="auto", menu_items=None)
EXAMPLE_NO = 1
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def pseudo_bold(text):
    bold_text = ''.join(chr(0x1D5D4 + ord(c) - ord('A')) if 'A' <= c <= 'Z' else
                        chr(0x1D5EE + ord(c) - ord('a')) if 'a' <= c <= 'z' else c
                        for c in text)
    return bold_text
def streamlit_menu(example=1):
    if example == 1:
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Road Map", "Resume Builder", "Ai bot"],  # required
                icons=["geo-alt-fill", "file-person-fill", "robot"],  # optional
                menu_icon="cast",  # optional
                default_index=0,

               
                
                # optional
            )
        return selected
    if example == 2:
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Road Map", "Resume Builder", "Ai bot"],  # required
                icons=["geo-alt-fill", "file-person-fill", "robot"],  # optional
                menu_icon="cast",  # optional
                default_index=0,
            )
        return selected
    if example == 3:
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Road Map", "Resume Builder", "Ai bot"],  # required
                icons=["geo-alt-fill", "file-person-fill", "robot"],  # optional
                menu_icon="cast",  # optional
                default_index=0,                
                # optional
            )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Road Map":
    st.header(f"Get your persanalised  {selected}")
    
    with st.form(key='survey_form'):
        text_stack_placeholder = pseudo_bold("Known text stacks")
        text_know = st.multiselect("Text Stack You Know",t,[])
        End_Gole =st.multiselect("What is your End Gole", t,[])
        time= st.number_input("Time in months", min_value=1, max_value=12, step=1)
        start_date = st.date_input("Start Data", datetime.date.today()) 
        End_date = st.date_input("end Data", datetime.date.today()) 
        difficulty = st.radio("Till which level you waant to learn the things", ("Easy", "Medium", "Hard"))
        submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        s="So now take a role of expert road map desiesner for students and now now the i know these text_know" +str(text_know)+"and his end gole is to learn " + str(End_Gole)+"i want to complete this my end gole in "+ str(time)+"moths"+"i will start on "+str(start_date)+"end on "+str(End_date)+"i only want to lean till the "+str(difficulty)+"from these imformation give me proper road map which include the resouce(youtube channels) the time line to each topic in deatle and also tell how much time should i give to each day to  complete that task  and sove leatcode questions which are importatnt add imogies and make your reslut in organised manner "
        s=get_gemini_response(s)
        st.write(s)
        
if selected == "Resume Builder":
        st.title(f"You have selected {selected}")
if selected == "Ai bot":
        import streamlit as st
        from openai import OpenAI

        openai_api_key = "Fgsdfg"
        st.header(f"💬 Ai Job Chatbot")
        if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

        for msg in st.session_state.messages:
            st.chat_message(msg["role"]).write(msg["content"])

        if prompt := st.chat_input():
            print(prompt)
            
            st.session_state.messages.append({"role": "user", "content": prompt})
            st.chat_message("user").write(prompt)
            
            msg = get_gemini_response(prompt)
            st.session_state.messages.append({"role": "assistant", "content": msg})
            st.chat_message("assistant").write(msg)

            
