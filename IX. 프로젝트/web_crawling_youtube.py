from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    # url = "https://www.youtube.com/feed/trending?gl=KR"
    url = "https://www.youtube.com/channel/UCoUDrzyCl1IwU602xdTsM-g/videos" #소근커플
    response = requests.post(url)
    # print(response.text)
    soup = BeautifulSoup(response.text, "lxml")
    titles = soup.find_all("a", attrs={"class":"yt-uix-tile-link"})
    for title in titles:
        print(title.text)
        print("https://youtube.com/"+title["href"])


    url = "https://www.youtube.com/feed/trending?gl=KR" #유튜브 트렌딩
    response = requests.post(url)
    # print(response.text)
    soup = BeautifulSoup(response.text, "lxml")
    titles = soup.find_all("a", attrs={"class":"yt-uix-tile-link"})
    n = 1
    for title in titles:
        print(str(n), title.text)
        print("https://youtube.com/"+title["href"])
        n+=1