
import requests
from bs4 import BeautifulSoup
url='https://www.rottentomatoes.com/browse/movies_at_home/sort:popular'
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
test = soup.find('div',class_='discovery-tiles__wrap')

test2=test.find("div", class_="js-tile-link")
test3=test2.find('score-pairs').find('div',class_='wrap').find('span')
thelist=[]

for movie in soup.find_all("div", class_="js-tile-link"):
    title=movie.find('span',class_='p--small').string.strip()
    score=movie.find('span',class_='percentage', attrs={'data-qa': 'audience-score'})
    thelist.append({'title': title, 'score': score})
print(response.status_code)
#thelist.sort()
#uniqs= set(thelist)

print(test3)


'''
movies = []
for movie in soup.find_all("div", class_="lister-item-content"):
    title = movie.find("h3").find("a").string
    duration = int(movie.find("span", class_="runtime").string.strip(' min'))
    movies.append({'title': title, 'duration': duration})

print(movies[0:2])
'''
#html/body/div[3]/main/div[1]/div[1]/div[3]/div/div/div[1]/tile-dynamic/a/span[1]
#main-page-content > div.discovery > div.discovery-grids-container.sticky-header > div > div > div:nth-child(1) > tile-dynamic > a > span.p--small
