# pip install beautifulsoup4   플레이스토어 같은거
# pip install lxml 해석기

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':
    #네이버웹툰 > 원수를 사랑하라 제목을 가져오자
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=733079")
    soup = BeautifulSoup(data, "lxml")      #httpResponse -> HTML
    data.close()
    # print(soup)
    html = "<html><head><meta charset='utf-8'></head><body>"
    cartoon_titles = soup.find_all("td", attrs={"class":"title"})   #<td class="title">...</td>
    for cartoon_titles in cartoon_titles:                   # cartoon_titles[:2]를 해서 원하는 화까지 정할수 있음
                                                            #가장 최신화하려면
        title = cartoon_titles.find("a").text                   #텍스트 가져오기.<a>text</a>
        link = cartoon_titles.find("a").get("href")             #태그의 속성값 가져오기.<a href="">text</a>
        link = "https://comic.naver.com" + link
        print(title)
        print(link)
        html += "<a html='{}'> {} </a><br>".format(link,title)      #<a href='Link'>title</a>
    html += "</body></html>"
    # print(html)
    outputSoup = BeautifulSoup(html,"lxml")                # 내가생성한 html 문자열을 soup 객체로 만들자
    prettyHtml = str(outputSoup.prettify())                 # 예쁘게 html 코드로 만들자
    with open("원수를 사랑하라.html","w",encoding="utf-8") as f:        #html 파일 만들자
        f.write(prettyHtml)

