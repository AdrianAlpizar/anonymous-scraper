import socks
import socket
from bs4 import BeautifulSoup
import requests
import sqlite3

# connect/create database
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE database (title text)""")
# port tor runs on (change it to whatever it is in your system)
socks.setdefaultproxy(socks.SOCKS5, "localhost", 950) 
socket.socket = socks.socksocket

# get site (this case: my website)
source = requests.get('https://adrianalpizar.github.io/projects.html').text
soup = BeautifulSoup(source, 'lxml')

# scrape
for item in soup.find_all("div", {"class": "box-items"}):
    title = item.div.div.h3.text

    # '?' protects against SQL Injections
    cur.execute("INSERT INTO database VALUES (?)", (title,))

conn.commit()
conn.close()