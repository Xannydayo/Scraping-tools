from collections import deque
import re

from bs4 import BeautifulSoup
import requests
import urllib.parse

# Print header
print("\n" + "="*30)
print(" " * 10 + "CREATED BY XANNY" + " " * 10)
print("="*30 + "\n")

user_url = str(input('[+] Masukkan url: '))
urls = deque([user_url])
scraped_urls = set()
emails = set()
count = 0


try:
    while True:
        count += 1
        if count > 10:
            break

        url = urls.popleft()
        scraped_urls.add(url)
        parts = urllib.parse.urlsplit(url)
        base_url = f'{parts.scheme}://{parts.netloc}'
        path = url[:url.rfind('/')+1] if '/' in parts.path else url
        
        print(f'{count} memproses {url}')
        
        try:
            response = requests.get(url)
        except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue
        
        new_emails = set(re.findall(r'[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}', response.text, re.IGNORECASE))
        emails.update(new_emails)
        
        soup = BeautifulSoup(response.text, 'html.parser')
        for anchor in soup.find_all('a'):
            link = anchor.attrs['href'] if 'href' in anchor.attrs else ''
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
                
            if link not in urls and link not in scraped_urls:
                urls.append(link)
except KeyboardInterrupt:
    print('[-] Closing!')
    
print('\n Proses Telah Selesai')
print(f'\n{len(emails)} Email ditemukan \n ===============================')

for mail in emails:
    print(' ' + mail)
print('\n')