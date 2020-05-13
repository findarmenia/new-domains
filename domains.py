from bs4 import BeautifulSoup
import requests as req
import io
import zipfile
import pandas as pd

url = "http://whoisds.com/newly-registered-domains"
resp = req.get(url)
soup = BeautifulSoup(resp.content, 'html.parser')
table = soup.find("table", { "class" : "table-bordered" })
a_tag = table.find("a")
file_url = a_tag["href"]
r = req.get(file_url)
with r, zipfile.ZipFile(io.BytesIO(r.content)) as archive:
    archive.extractall()
df = pd.read_csv("domain-names.txt", delimiter='\n')
df.to_csv('new_domains.csv', index=False)
