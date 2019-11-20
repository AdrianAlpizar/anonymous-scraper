# anonymous-scraper

An anonymous python web scraper built with BeautifulSoup, that makes requests using the package Tor as a SOCKS5 proxy for maximum anonymity, and saves the scraped content to memory using SQLite3. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the dependencies .

```bash
pip install -r requirements.txt
```

## Importing the dependencies

```python
import socks
import socket
from bs4 import BeautifulSoup
import requests
import sqlite3
```

## Executing correctly

1. Use in [Linux](https://www.linux.org/) for maximum anonymity.
2. Make sure [Tor](https://www.torproject.org/) package is installed.
3. Set the port inside ```scraper.py``` to the port [Tor](https://www.torproject.org/) runs on in your machine.
4. Run ```scraper.py```

```bash
python scraper.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
