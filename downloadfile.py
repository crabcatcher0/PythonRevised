#can download any file like pdf, csv
url = 'https://pdfobject.com/pdf/sample.pdf' #path of pdf

import math
import requests
from tqdm import tqdm
import time

data = requests.get(url)
#at 1 time i just want to download 256 bytes 
chunk_size = 256 #how many size of data you want to get in 1 go
size = int(data.headers['Content-Length'])
r = requests.get(url, stream=True) #will get data at once, will get data one by one
n = math.ceil(size/chunk_size)
#file handling

with open("file.pdf", "wb") as file:
    for chunk in tqdm(r.iter_content(chunk_size=chunk_size), total=n):
        time.sleep(0.1)
        file.write(chunk)
        
