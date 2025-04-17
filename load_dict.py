import re
import json
import os

def remove_html_tags(text):
    cleana = re.compile('<.*?>')
    clean = re.sub(cleana, '', text)
    return clean

def load():
    print(os.getcwd())
    with open('video_data.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    text_list = [item["text"] for item in json_data] 
    text_lista = [remove_html_tags(text) for text in text_list] 
    return text_lista


def different_load():
    print(os.getcwd())  
    with open('spam_results.json', 'r', encoding='utf-8') as file:
        json_data = json.load(file) 
    
    return list(json_data.keys())  
