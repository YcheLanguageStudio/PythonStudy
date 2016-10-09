import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/top250?start={}"
counter = 0
film_counter = 0

while film_counter<166:
    r = requests.get(url.format(film_counter))
    #print(r.content)
    soup = BeautifulSoup(r.content, "html.parser")
    for rate in soup.find_all(class_="rating_num"):
        counter += float(rate.string)
        film_counter += 1
        if film_counter>=166:
            break

print(counter)