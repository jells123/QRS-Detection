import requests
from bs4 import BeautifulSoup
import os
import time

if not os.path.exists('train'):
	os.mkdir('train')
dest_folder = os.getcwd() + "/train/"

url = 'https://physionet.org/pn3/incartdb/'
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
		