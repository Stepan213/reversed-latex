import pyperclip
import requests
from pynput import keyboard
from pynput.keyboard import Key, KeyCode

from config import API_KEY

def get_latex_code(text):
    url = "https://api.openai.com/v1/edits"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    data= {
        "model": "text-davinci-edit-001",
        "input": text,
        "instruction": "Rewrite to LaTeX code.",
    }
    response = requests.post(url, json=data, headers=headers)

    return response.json()['choices'][0]['text']#.strip()

def on_release(key):
    if key == KeyCode.from_char('c') and keyboard.Controller().pressed(Key.ctrl):
        print("yes")
        selected_text = pyperclip.paste()
        print(selected_text)
        latex_code = get_latex_code(selected_text)
        if latex_code:
            pyperclip.copy(latex_code)

with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
