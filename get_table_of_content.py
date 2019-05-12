
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import datetime

def get_table_of_content(issue_title_list):
    issue_List = []
    index_list = []
    TODAY = datetime.datetime.today().today()
    for issue_title in issue_title_list:
        time.sleep(15)
        new_url = issue_title[0]
        index_list.append(issue_title[1])
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
    data.T.to_csv('Newly_Issue_List{}.csv'.format(TODAY))
