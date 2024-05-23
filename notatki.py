import requests
from bs4 import BeautifulSoup

def get_cordinates(miejscowośc:str)->list[float,float]:
    url:str=f"https://pl.wikipedia.org/wiki/Lublin{miejscowość}"
    response=requests.get(url)
    response_html=BeautifulSoup(response.text,"html.parser")
    latitude= float(response_html.select(".latitude")[1].text.repleace(","._new"."))
    longitude=float(response_html.select(".latitude")[1].text.repleace(","._new"."))
    return [latitude, longitude]

miejscowość=input("Podaj nazwę miejscowości")
print(get_cordinates(miejscowość))