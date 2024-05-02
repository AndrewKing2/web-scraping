from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)
all_quotes = []
new_quotes = []
all_authors = []
new_authors = []
all_tags = []
authors = soup.findAll('small')
quotes = soup.findAll('span', attrs={"class":"text"})
tags = soup.findAll('div', attrs={"class":"tags"})
for tag in tags:
    all_tags.append(tag.text)

for quote in quotes:
    all_quotes.append(quote.text)

for author in authors:
    all_authors.append(author.text)


url = 'https://quotes.toscrape.com/page/2/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
tags = soup.findAll('div', attrs={"class":"tags"})
for tag in tags:
    all_tags.append(tag.text)
quotes = soup.findAll('span', attrs={"class":"text"})
for quote in quotes:
    all_quotes.append(quote.text)
authors = soup.findAll('small')
for author in authors:
    new_authors.append(author.text)
all_authors.append(new_authors)
new_authors = []

url = 'https://quotes.toscrape.com/page/3/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
tags = soup.findAll('div', attrs={"class":"tags"})
for tag in tags:
    all_tags.append(tag.text)
quotes = soup.findAll('span', attrs={"class":"text"})
for quote in quotes:
    all_quotes.append(quote.text)
authors = soup.findAll('small')
for author in authors:
    new_authors.append(author.text)
all_authors.append(new_authors)
new_authors = []

url = 'https://quotes.toscrape.com/page/4/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
tags = soup.findAll('div', attrs={"class":"tags"})
for tag in tags:
    all_tags.append(tag.text)
quotes = soup.findAll('span', attrs={"class":"text"})
for quote in quotes:
    all_quotes.append(quote.text)
authors = soup.findAll('small')
for author in authors:
    new_authors.append(author.text)
all_authors.append(new_authors)
new_authors = []

url = 'https://quotes.toscrape.com/page/5/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
tags = soup.findAll('div', attrs={"class":"tags"})
for tag in tags:
    all_tags.append(tag.text)
quotes = soup.findAll('span', attrs={"class":"text"})
for quote in quotes:
    all_quotes.append(quote.text)
authors = soup.findAll('small')
for author in authors:
    new_authors.append(author.text)
all_authors.append(new_authors)
new_authors = []

url = 'https://quotes.toscrape.com/page/6/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
tags = soup.findAll('div', attrs={"class":"tags"})
for tag in tags:
    all_tags.append(tag.text)
quotes = soup.findAll('span', attrs={"class":"text"})
for quote in quotes:
    all_quotes.append(quote.text)
authors = soup.findAll('small')
for author in authors:
    new_authors.append(author.text)
all_authors.append(new_authors)
new_authors = []

url = 'https://quotes.toscrape.com/page/7/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
tags = soup.findAll('div', attrs={"class":"tags"})
for tag in tags:
    all_tags.append(tag.text)
quotes = soup.findAll('span', attrs={"class":"text"})
for quote in quotes:
    all_quotes.append(quote.text)
authors = soup.findAll('small')
for author in authors:
    new_authors.append(author.text)
all_authors.append(new_authors)
new_authors = []

url = 'https://quotes.toscrape.com/page/8/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
tags = soup.findAll('div', attrs={"class":"tags"})
for tag in tags:
    all_tags.append(tag.text)
quotes = soup.findAll('span', attrs={"class":"text"})
for quote in quotes:
    all_quotes.append(quote.text)
authors = soup.findAll('small')
for author in authors:
    new_authors.append(author.text)
all_authors.append(new_authors)
new_authors = []

url = 'https://quotes.toscrape.com/page/9/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
tags = soup.findAll('div', attrs={"class":"tags"})
for tag in tags:
    all_tags.append(tag.text)
quotes = soup.findAll('span', attrs={"class":"text"})
for quote in quotes:
    all_quotes.append(quote.text)
authors = soup.findAll('small')
for author in authors:
    new_authors.append(author.text)
all_authors.append(new_authors)
new_authors = []

url = 'https://quotes.toscrape.com/page/10/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
tags = soup.findAll('div', attrs={"class":"tags"})
for tag in tags:
    all_tags.append(tag.text)
quotes = soup.findAll('span', attrs={"class":"text"})
for quote in quotes:
    all_quotes.append(quote.text)
authors = soup.findAll('small')
for author in authors:
    new_authors.append(author.text)
all_authors.append(new_authors)
new_authors = []

least_occurred_author = min(all_authors, key=lambda x: all_authors.count(x))
most_occurred_author = max(all_authors, key=lambda x: all_authors.count(x))
print(f'Least common author: {least_occurred_author}')
print(f'Most common author:{most_occurred_author}')
print('Total tags:',len(all_tags))
total_length = sum(len(item) for item in all_quotes)

average_length = round(total_length / len(all_quotes),0)

print("Average length of quotes in the list:", average_length)
print()
longest_quote = max(all_quotes,key=len)
print()
shortest_quote = min(all_quotes,key=len)
most_pop_tag = max(all_tags, key=lambda x: all_tags.count(x))
print(f'The most common tag is: {most_pop_tag}')

print(f'The longest quote is: {longest_quote}')
print(f'The shortest quote is: {shortest_quote}')
  



