
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

from get_table_of_content import get_table_of_content


URL = 'https://www.jstage.jst.go.jp/browse/-char/ja'

if(URL)
html = urlopen(URL)
soup = BeautifulSoup(html,'html.parser')

Newly_release_issue = soup.find('ul',{'id':'newly-release-issue-list'})
newly_release_issue_list = Newly_release_issue.findAll('li')
Latest_Issue = []
for i in newly_release_issue_list: 
    Latest_Issue.append([i.a.get('href'),i.a.get('title')]) 

get_table_of_content(issue_title_list = Latest_Issue)