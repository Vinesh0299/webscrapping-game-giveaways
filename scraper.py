import requests
from bs4 import BeautifulSoup
import smtplib

urls = ['https://gamesystemrequirements.com/']

def get_data(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    titles = soup.find('div', 'main_newshl_cont mnb_fthl')
    
    for title in titles:
        data = title.find('div', 'main_newshl_box_title').find('span').get_text()
        if('free' in data.lower()):
            with open("already_sent.txt", "a") as file:
                file.write(data+"\n")
            print(data)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('madarauchiha3524@gmail.com', 'xpbrobdjoyaleffs')

if __name__ == '__main__':
    for url in urls:
        get_data(url)