import openai
import time
import yaml

# Set up OpenAI API credentials
openai.api_key='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'

# Read the text file containing the questions
file = open(r"C:\Users\ashutosh.somvanshi\PVC_Trend_Analysis\Gpt_Data_understanding Capability\question_.txt", "r")
questions = file.readlines()

file_ =open(r"C:\Users\ashutosh.somvanshi\PVC_Trend_Analysis\Gpt_Data_understanding Capability\Table_data.yaml", 'r')
yaml_data = yaml.safe_load(file_)


# Remove any leading or trailing whitespace from the questions
questions = [question.strip() for question in questions]


# Function for using GPT

def get_answers_few_shot_approach_(question): 
    
    prompt = f""" 
        Your task is to answer a question based on a tabular data \
        tabular data is followed by tripple back ticks  ```{yaml_data}```  \ 
        and question is follwed by double qoutes "{question}" \ 
        while answering please do not repeat the question \
        if the question is not realted to data give 'It is nor realevant to data ask something else \
    
    """ 
    
    
    answer = get_completion(prompt)
    return answer

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    time.sleep(20)
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
     )
    return response.choices[0].message["content"]


# Iterate through each question and get answers
for question in questions:

    answer = get_answers_few_shot_approach_(question)

    # Display the question and answer
    # print("Question:", question)
    print(f"Question :--->", {question})
    print(f"Answer:--->", {answer})
    print("=" * 50)
