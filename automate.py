from logging import setLoggerClass
from dotenv import load_dotenv
import os
from requests import Session
from bs4 import BeautifulSoup as bs

load_dotenv()

WEBSITE = os.getenv('WEBSITE')
WEBSITE_USERNAME = os.getenv('WEBSITE_USERNAME')
PASS = os.getenv('PASS')

if __name__ == '__main__':
    with Session() as s:
        site = s.get(WEBSITE)
        bs_content = bs(site.content, "html.parser")
        login_data = {}
        for input in bs_content.find_all("input"):
            try:
                login_data[input['name']] = input['value']
            except KeyError:
                login_data[input['name']] = None
        login_data['account[email]'] = WEBSITE_USERNAME
        login_data['account[password]'] = PASS
        login_data['account[remember_me]'] = '0'
        
        response = s.post(WEBSITE,login_data)
        breakpoint()
        home_page = s.get(response.url)
        

