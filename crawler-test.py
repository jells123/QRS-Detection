import requests
from bs4 import BeautifulSoup
import os
import time

if not os.path.exists('test'):
	os.mkdir('test')
dest_folder = os.getcwd() + "/test/"

url = 'https://physionet.org/physiobank/database/mitdb/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html5lib')

hrefs_list = soup.find_all('a', href=True)
for entry in hrefs_list:
	link = entry['href']
	if link.endswith('.dat') or link.endswith('.atr') or link.endswith('.hea'):
		print(url + link + "...")
		time.sleep(1)
		data_request = requests.get(url + link)
		with open(dest_folder + link, 'wb') as f:
			f.write(data_request.content)
		print(link, data_request.status_code)
		