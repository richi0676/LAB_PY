
from bs4 import BeautifulSoup
import requests
import pandas as pd



url = "https://www.worldometers.info/coronavirus/?utm_campaign=homeAdvegas1?%22%20%5Cl%22countries"
data = requests.get(url)
soup = BeautifulSoup(data.text,'html5lib')
covid_dict = {}
div = soup.find_all("div", {"id": "maincounter-wrap"})
for i in div:
  content_div = i.find("div",{"class":"maincounter-number"})
  covid_dict[i.find("h1").text.replace(":","").strip()] = content_div.find("span").text.strip()
print(covid_dict)
tables = soup.find_all('table')
table_header = tables[0].find_all('th')
table_head = []
for i in range(15):
  if i != 0:
    table_head.append(table_header[i].text.replace("\n","").replace("\xa0",""))
print(table_head)
Covid_data = pd.DataFrame(columns=table_head)
for row in tables[0].tbody.find_all('tr'):
  col = row.find_all('td')
  if (col != []):
    country = col[1].text.strip()
    totalCases = col[2].text.strip()
    totalDeaths = col[4].text.strip()
    totalRecovered = col[6].text.strip()
    Covid_data = Covid_data.append({"Country,Other":country,
                                    "TotalCases":totalCases,
                                    "TotalDeaths":totalDeaths,
                                    "TotalRecovered":totalRecovered,},ignore_index=True)

Covid_data.drop(Covid_data.index[:7],inplace=True)
Covid_data.to_csv("Covid_data.csv",index=False)




