import streamlit as webapp
from PIL import Image
import time
# from get_probability import get_prob
from get_paragraph import get_para

from PIL import Image



#opening the image

# image = Image.open('cfilt_logo.jpg')



#displaying the image on streamlit app

# webapp.image(image, width=200)



webapp.sidebar.title("Demo - Topic to Essay Generation with KG")
webapp.title("""Knowledge Enhanced Topic to Essay Generation""")



def get_text():
    input_text = webapp.text_input("Topic Words (Enter 5 comma separated topic-words) - ","")
    return input_text

def write_response(response):
    webapp.header('Response')
    webapp.text(response)

def follow(thefile):
    # thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


webapp.subheader("Demo Application")

user_input = get_text()
should_generate = webapp.button('Generate Response')
user_input = "TOPIC : " + user_input
data_load_state = webapp.text("")
# without_kg = webapp.text("")

def checkfile(data_load_state):
    with open("gpt.txt",'r',encoding="utf-8") as f:
        response = f.read()
        response = response.strip("\n")
        if response:
            data_load_state.text("Paragraph generated!")
            webapp.write(response)
            
        else:
            time.sleep(10)
            checkfile(data_load_state)


if should_generate:
    # if model_invoked == 'gpt-2':
    # response = generate_response_gpt2(user_input, temp)
    # logfile = open("gpt.txt","r")
    # loglines = follow(logfile)
    # str1 = ""
    # for line in loglines:
    #     str1 +=line
    # response = str1
    with open("topic.txt","w") as f:
        f.write(user_input)
    data_load_state.text('Generating paragraph...')
    # time.sleep(10)
    topics = user_input+"\n\n###\n\n"
    webapp.write(get_para(topics))
    # checkfile(data_load_state)

