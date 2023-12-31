# -*- coding: utf-8 -*-
"""ChatBotwithOpenAiAPI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18RCMiQYplhx6HO7MGATheYQblAaTorc3
"""

!pip install -q openai
!pip install -q gradio

import openai
import gradio as gr

openai.api_key = "enter your key here"

def openai_chat(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

def chatbot(input, history=[]):
    output = openai_chat(input)
    history.append((input, output))
    return history, history

gr.Interface(fn = chatbot,
             inputs = ["text",'state'],
             outputs = ["chatbot",'state']).launch(debug = True)
