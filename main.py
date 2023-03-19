import pyperclip
import requests
from pynput import keyboard
from pynput.keyboard import Key, KeyCode

API_KEY = "your_openai_api_key"

def get_latex_code(text):
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "text-davinci-003",
        "prompt": f"Convert the following text to LaTeX code: {text}",
        "max_tokens": 100,
        "temperature": 0.5,
        "top_p": 1,
        "n": 1,
        "stop": "\n"
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["text"].strip()
    else:
        return None

def on_release(key):
    if key == KeyCode.from_char('c') and keyboard.Controller().pressed(Key.ctrl):
        selected_text = pyperclip.paste()
        latex_code = get_latex_code(selected_text)
        if latex_code:
            pyperclip.copy(latex_code)

with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
