
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

from get_table_of_content import get_table_of_content

word1 = ''
word2 = ''
Issues = ''

URL_1 = 'https://www.jstage.jst.go.jp/browse/-char/ja'
URL_2 = 'https://www.jstage.jst.go.jp/result/global/-char/ja?item1=4&word1={}&cond1=&item2=&word2=&cond2=&item3=&word3=&cond3=&item4=&word4=&count={}&from=&order=&type=&license=&attribute=&languageType=&option=&yearfrom=&yearto=&category=&cdjournal=&favorite=&translate=&bglobalSearch=false&sortby=1&showRecodsH=20&showRecords=20'.format(word1,word2,Issue)
html = urlopen(URL)
soup = BeautifulSoup(html,'html.parser')

Newly_release_issue = soup.find('ul',{'id':'newly-release-issue-list'})
newly_release_issue_list = Newly_release_issue.findAll('li')
Latest_Issue = []
for i in newly_release_issue_list: 
    Latest_Issue.append([i.a.get('href'),i.a.get('title')]) 

get_table_of_content(issue_title_list = Latest_Issue)