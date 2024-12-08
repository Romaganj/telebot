from bs4 import BeautifulSoup
import requests

url = 'https://www.gismeteo.ua/ua/weather-lviv-4949/now/'
response = requests.get(url, headers={"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
bs = BeautifulSoup(response.text,"lxml")
temp_now = bs.find('span','unit unit_temperature_c')
print(temp_now.text)