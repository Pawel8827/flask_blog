import requests
page = requests.get("https://globe.adsbexchange.com/?icao=489882")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
abc = soup.find_all(class_="infoData") 
test = [t.prettify() for t in abc]
speed = soup.find(id= "selected_speed1")
print(speed)
