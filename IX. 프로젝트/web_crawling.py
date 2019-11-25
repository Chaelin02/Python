# pip install beautifulsoup4   플레이스토어 같은거
# pip install lxml 해석기

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':
    #네이버웹툰 > 원수를 사랑하라 제목을 가져오자
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=733079")
    soup = BeautifulSoup(data, "lxml")
    # print(soup)

    cartoon_titles = soup.find_all("td", attrs={"class":"title"})
    for cartoon_titles in cartoon_titles:
        title = cartoon_titles.find("a").text
        print(title)