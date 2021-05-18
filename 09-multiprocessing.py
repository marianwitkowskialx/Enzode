
# Asynchroniczne pobranie danych ze strony WWW
import requests
from multiprocessing.pool import ThreadPool

BASE_URL = "http://51.91.120.89/TABLICE/"

response = requests.get(BASE_URL)
lines = response.text.split("\n")
urls = [f"{BASE_URL}{l.strip()}" for l in lines if len(l.strip())>0 ]
print(urls)

def download_url(url):
    #print(f"Start {url}")
    r = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as fd:
        fd.write(r.content)
    #print(f"Stop {url}")
    return file_name

#download_url("http://51.91.120.89/TABLICE/NO9738R.jpg")
result = ThreadPool(20).imap_unordered( download_url, urls )
for r in result:
    print(r)


