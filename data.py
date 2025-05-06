import requests
from bs4 import BeautifulSoup
URL="http://localhost:11434/api/generate"
MODEL="llama3"
def extract(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    paragraphs=soup.find_all('p')
    text=' '.join([para.get_text(strip=True) for para in paragraphs])
    return text

def summarization(text):
    prompt = f"Summarize the following in 3 bullet points:\n\n{text[:3000]}" 
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
    response=requests.post(URL, json=payload)
    response.raise_for_status()
    return response.json()["response"]

url = "https://ghost.org/" 
print("Extracting text from blog")
content=extract(url)
print("Summarizing")
summary = summarization(content)
print("\nSummary:")
print(summary)
