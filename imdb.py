import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
response = requests.get(url)

html = response.content

soup = BeautifulSoup(html,"html.parser")

n = float(input("Imdb Puanı: "))

film_isim = soup.find_all("td",{"class":"titleColumn"})
film_puan = soup.find_all("td",{"class":"ratingColumn imdbRating"})

for film_isim, film_puan in zip (film_isim,film_puan):
    film_isim= film_isim.text
    film_puan= film_puan.text
    
    film_isim= film_isim.strip()
    film_isim= film_isim.replace("\n","")

    ilm_puan= film_puan.strip()
    film_puan= film_puan.replace("\n","")

    if (float(film_puan) >= n):
        print("Film ismi: {} Imdb Puanı: {}".format(film_isim,film_puan))
        print("****************************************************************************************************")
