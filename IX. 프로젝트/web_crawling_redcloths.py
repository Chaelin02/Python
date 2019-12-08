from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':
    url = "https://www.styleshare.kr/search?keyword=%EB%B9%A8%EA%B0%84%EC%83%89%20%EC%9B%90%ED%94%BC%EC%8A%A4"
    with urlopen(url) as response:
        soup = BeautifulSoup(response,"lxml")
    print(soup)
