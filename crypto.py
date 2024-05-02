from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.coinbase.com/explore'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

table_rows = soup.findAll("tr")

for row in table_rows[1:6]:
    td = row.findAll("td")
    name = td[0].text
    current_price = float(td[1].text.replace(',', '').replace('$', ''))

    
    change_str = ''.join(filter(str.isdigit, td[3].text))
    if change_str:
        change = float(change_str) / 100
    else:
        change = 0

    cf = 1 + change / 100  
    pre_price = current_price / cf
    sign = ''
    if 'style="color: var(--negative)' in td[3]:
        sign = '-'

    print(f"Currency Name: {name.strip()[1:-3]}")
    print(f"Symbol: {name.strip()[-3:]}")
    print(f"Current price: ${current_price}")
    print(f"Change over past 24 hours:{sign}{change}%")
    print(f"Price before change: ${pre_price:.2f}")
    print()

