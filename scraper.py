import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

urls = ['https://gamesystemrequirements.com/']

receiver_addresses = ['Vinesh.katewa@gmail.com']

def get_data(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    titles = soup.find('div', 'main_newshl_cont mnb_fthl')
    
    for title in titles:
        data = title.find('div', 'main_newshl_box_title').find('span').get_text()
        if('free' in data.lower()):
            with open("already_sent.txt", "a+") as file:
                file.seek(0)
                exists = False
                for line in file.readlines():
                    if(data in line):
                        exists = True
                if(not exists):
                    file.write(data+"\n")
                    send_mail(data, title["href"])

def send_mail(data, link):
    # Creating server for sending mail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('madarauchiha3524@gmail.com', 'xpbrobdjoyaleffs')

    for address in receiver_addresses:
        # Creating the message to be sent
        message = MIMEMultipart()
        message['From'] = 'madarauchiha3524@gmail.com'
        message['To'] = address
        message['Subject'] = 'New game is available for free!'
        message.attach(MIMEText(data+"\n\n"+"Click here: " + link, 'plain'))

        text = message.as_string()
        server.sendmail('madarauchiha3524@gmail.com', address, text)

    server.quit()

def add_receiver_email(email):
    receiver_addresses.append(email)

if __name__ == '__main__':
    for url in urls:
        get_data(url)