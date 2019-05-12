
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

URL = 'https://www.jstage.jst.go.jp/browse/-char/ja'
html = urlopen(URL)
soup = BeautifulSoup(html,'html.parser')

Newly_release_issue = soup.find('ul',{'id':'newly-release-issue-list'})
newly_release_issue_list = Newly_release_issue.findAll('li')
Latest_Issue = []
for i in newly_release_issue_list: 
    Latest_Issue.append([i.a.get('href'),i.a.get('title')]) 

issue_List = []
index_list = []
for Latest_issue in Latest_Issue:
    time.sleep(15)
    new_url = Latest_issue[0]
    index_list.append(Latest_issue[1])
    new_html = urlopen(new_url)
    new_soup = BeautifulSoup(new_html,'html.parser')
    search_resultslist = new_soup.find('div',{'id':'search-resultslist-wrap'})
    search_resultslisting = search_resultslist.findAll('ul',{'class':'search-resultslisting'})
    issue_Title = []
    for i in search_resultslisting:
        if not (i.find_all('div',{'class':'searchlist-title'}) == []):
            for j in i.find_all('div',{'class':'searchlist-title'}):
                issue_Title.append(j.a.get('title'))
    issue_List.append(issue_Title)
    
data = pd.DataFrame(issue_List,index = index_list)
data.column = data.column + 1

data.T.to_csv('issue_list.csv')
