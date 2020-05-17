import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://gamesystemrequirements.com/'

#headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

def get_data(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find_all("a", "main_newshl_box")

    for product in title:
        print(product.find("div", "main_newshl_box_title").find("span").get_text())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('madarauchiha3524@gmail.com', 'xpbrobdjoyaleffs')
get_data(url)