import requests  # http requests

from bs4 import BeautifulSoup  # web scraping

# send the mail
import smtplib
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# system date and time manipulation
import datetime
now = datetime.datetime.now()

# email content placeholder
content = ''  # empty python string

# extracting Hacker News Stories


def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i+1)+'::'+tag.text+"\n"+'<br>')
                if tag.text != "More" else '')
        # print(tag.prettify) #find all HTML tags
    return(cnt)
