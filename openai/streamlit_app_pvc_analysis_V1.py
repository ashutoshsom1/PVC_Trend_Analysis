import openai
##
import streamlit as st
import speech_recognition as sr
# from gtts import gTTS
# import pygame
from io import BytesIO
import pyttsx3
###
from PIL import Image

image = Image.open(r'C:\Users\ashutosh.somvanshi\voice_text\pngtree-chatbot-icon-chat-bot-robot-png.png')

openai.api_key='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'


Ques_Ans_= open(r"C:\Users\ashutosh.somvanshi\PVC_Trend_Analysis\openai\Ans__.txt","r")
Ques_Ans__ = Ques_Ans_.read()

####################################################################################################
# Function for using GPT

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
     )
    return response.choices[0].message["content"]





# def get_answers_few_shot_approach_(question):
#     prompt = f"""
#     Your task is to answer in a consistent style 

#     <Ques>: What is your name?

#     <Ans>:  my name is sebastin king.
    
#     <Ques>:you have to answer the {question} on the basis of this data {Ques_Ans__}
    
#     if the {question}is not realted to {Ques_Ans__} give the answer not present in data
#     dont give me the question in the result
#     answer in 40 words
#     """
#     answers = get_completion(prompt)
#     return answers
# def get_answers_few_shot_approach_(question):
#     prompt = f"""
#     You will be provided with text delimited by triple quotes.\
#     and text delimited <> will be you question\
#     Answer the question according to text delimited by triple quotes.
#     \"\"\"{Ques_Ans__}\"\"\"
#     Ques: <{question}>
    
#     If the text delimited by triple quotes does not have a relation with question, \ 
#     then simply write \"Question not realted to data.\"
    
#     anwers should be in 30 words
    
#     """
#     answers = get_completion(prompt)
#     return answers
\
    # if the question talk about future trends then give satisfactory answer \  
    
def get_answers_few_shot_approach_(question):
    prompt = f"""
    Your task is to answer the question based on a text file \
    text file is followed by tripple back ticks  ```{Ques_Ans__}```  \ 
    and question is follwed by double qoutes "{question}" \       
    if the question is related to text file then only give the answer \
    else give 'I dont have satisfactory answer for the question , Please ask other questions'   \
        
    dont give the information about data  \    
    answer in 25 words \
    
        

    
    """
    answer = get_completion(prompt)
    return answer    
    
####################################################################################################   


# Function used to read speak
####################################################################################################
class SessionState(object):
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)
            
       

def speak(text):
    engine = pyttsx3.init()
    # engine = pyttsx3.init()
    # engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    
     
    

def recognize_speech():
    r = sr.Recognizer()
    mic = sr.Microphone()
    lang_code = "en-US" #input("Enter language code (e.g. en-US, hi-IN): ")
    with mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,phrase_time_limit=10) #will only listen and strore in audio variable
        try:
            text = r.recognize_google(audio, language=lang_code)
            
            st.text("You Said : " +text)
            return text 
#             speak_text(text)
        except sr.UnknownValueError:
            st.text("Could not understand audio, Please try speaking again")  
            return ("Could not understand audio, Please try speaking again")






def main():
    
    Answer_s = ""
    
    # Define the Streamlit app
    st.set_page_config(page_title="AI Bot for PVC Industry Analysis")
    st.image(image, caption='AI BOT')
    st.title("AI Bot for PVC Industry Analysis")
    if st.button("start"):
            st.write("Start Talking -->")
            # Speech recognition
            transcript = recognize_speech()
            if transcript == "Could not understand audio, Please try speaking again":
                speak(str(transcript))
                Answer_ ="Please try speaking again"
                # speak(str(Answer_))
                st.write("Answer:")
                st.write(Answer_)
                # Answer_ =answer__
            else  :
            # engine.say(transcript)
                speak(str(transcript))
                answer__=  get_answers_few_shot_approach_(transcript)
                speak(str(answer__))
                Answer_s =answer__
                st.write("Answer:")
                st.write(Answer_s)
            

    # Display the answer
    # st.write("Answer:")
    # st.write(Answer_s)

    

    # Add some styling to the common text box
    st.markdown("""<style>
        .common-box {
            background-color: #f0f0f0;
            padding: 10px;
            margin-top: 20px;
            border-radius: 5px;
            box-shadow: 2px 2px 10px #c0c0c0;
        }
    </style>""", unsafe_allow_html=True)
    st.markdown(f'<div class="common-box">{Answer_s}</div>', unsafe_allow_html=True)

    # Add styling to the page
    st.markdown("""<style>
        body {
            background-color: #f5f5f5;
        }
    </style>""", unsafe_allow_html=True)



if __name__ == "__main__":
    main()

