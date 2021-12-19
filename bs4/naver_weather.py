import requests
from bs4 import BeautifulSoup


def  scrape_weather():
    print('[오늘의 날씨]')
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hk8GRlp0Jy0ssB6D7LKssssssUw-502435'
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')
    cast = soup.find('p',attrs = {'class':'summary'}).get_text() # 어제보다 ~~
    current_temp = soup.find('span',attrs = {'class':'blind'}).get_text().replace('도씨','')
    min_temp = soup.find('span',attrs = {'class':'lowest'}).get_text() #최저온도
    max_temp = soup.find('span',attrs = {'class':'highest'}).get_text() #최저온도

    #출력
    print(cast)
    print('현재 {} (최저 {}/ 최고 {})'.format(current_temp,min_temp,max_temp))

    
    
    
if __name__ == "__main__":
    scrape_weather()  # 오늘의 날씨 정보 가져오기

