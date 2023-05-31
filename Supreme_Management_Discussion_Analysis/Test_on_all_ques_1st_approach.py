import openai
##
import pandas as pd
from io import BytesIO
import pyttsx3
import time
###
from PIL import Image

image = Image.open(r'C:\Users\ashutosh.somvanshi\voice_text\pngtree-chatbot-icon-chat-bot-robot-png.png')

openai.api_key='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'


text_data= open(r"C:\Users\ashutosh.somvanshi\PVC_Trend_Analysis\Supreme_Management_Discussion_Analysis\Supreme_Text_files\tokens.txt","r")
text_data__ = text_data.read()

# Read the text file containing the questions
file = open(r"C:\Users\ashutosh.somvanshi\PVC_Trend_Analysis\Supreme_Management_Discussion_Analysis\Question_MDA.txt", "r")
questions = file.readlines()

# Remove any leading or trailing whitespace from the questions
questions = [question.strip() for question in questions]

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


# Checking of relevant question
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

tokens = word_tokenize(text_data__)
stop_words = set(stopwords.words('english'))  # You can adjust the language as needed
filtered_words = [word for word in tokens if word.lower() not in stop_words]
relevant_words = filtered_words

####################################################################################################

    
def is_question_relevant(question):
    # relevant_keywords = ["crude oil", "price", "production", "demand", "supply","Future"]
    
    question_lower = question.lower()
    for keyword in relevant_words:
        if keyword in question_lower:
            return True
    return False

def get_answers_few_shot_approach_(question): 
    
    prompt = f""" 
        Your task is to give the answer on the basis of a text file \
        text file is followed by tripple back ticks  ```{text_data__}```  \ 
        and question is follwed by double qoutes "{question}" \ 
        if question is not related to data then it will give a message "I don't have a satisfactory answer" \
        dont loose the information in the text \
        give answer upto 50 words  \ 
    
    """ 
    
    if is_question_relevant(question):
        answer = get_completion(prompt)
        if answer:
            return answer  # Limit the answer to 25 words
        else:
            return "I don't have a satisfactory answer for the question. Please ask another question."
    else:
        return "I don't have a  answer for the question. Please ask another question."
    
    
####################################################################################################   


# Function used to read speak
####################################################################################################
       

def speak(text):
    engine = pyttsx3.init()
    # engine = pyttsx3.init()
    # engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    
df_answers = pd.DataFrame(columns=['Question', 'Answer'])    
df_answers['Question'] = questions
empty_Answer = [] 

for question in questions:
    time.sleep(30)
    answer = get_answers_few_shot_approach_(question)
    empty_Answer.append(answer)

    # Display the question and answer
    # print("Question:", question)
    print(f"Question :--->", {question})
    print(f"Answer:--->", {answer})
    print("=" * 50)

df_answers['Answer'] = pd.Series(empty_Answer)
df_answers.to_csv(r'C:\Users\ashutosh.somvanshi\PVC_Trend_Analysis\Supreme_Management_Discussion_Analysis\Supreme_Text_files\Answers_MDA_1st_approach.csv')
