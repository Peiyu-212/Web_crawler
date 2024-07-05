import os
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from django.conf import settings

from ..models import Image, News


class NBANewsCrawler:
    url = 'https://tw-nba.udn.com/nba/index'
    res = requests.get(url)

    def get_img_url(self, soup_txt) -> str:
        img_content = soup_txt.find('figure').img
        img_response = requests.get(img_content.get('src'))
        img_data = img_response.content
        img_path = os.path.join(settings.MEDIA_URL,
                                f'image_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}.jpg')
        with open(img_path, 'wb') as img_file:
            img_file.write(img_data)
        image = Image.objects.create(
            title=img_content.get('alt'),
            url=img_content.get('src'),
            filepath=img_path
        )
        return image

    def save_news(self, obj: dict) -> None:
        News.objects.create(
            **obj
        )

    def catch_different_news(self) -> None:
        soup = BeautifulSoup(self.res.text, 'lxml')
        focus_links = soup.find_all('div', class_='box_body')[0]
        news_links = focus_links.find_all('a')

        for link in news_links:
            news_url = link.get('href')
            news_response = requests.get(news_url)
            news_response.encoding = 'utf-8'
            news_soup = BeautifulSoup(news_response.text, 'lxml')
            news_title = link.get('title')
            author_div = news_soup.find('div', class_='shareBar__info--author')
            if author_div:
                time_span = author_div.find('span').get_text(strip=True)
                authority = author_div.get_text(strip=True).replace(time_span, '').strip()
            news_content = news_soup.find_all('p')
            non_empty_p_tags = [p.get_text(strip=True) for p in news_content
                                if p.get_text(strip=True) and not p.find('figure')]
            combined_text = ' '.join(non_empty_p_tags)
            image = self.get_img_url(news_soup)
            self.save_news({'content': combined_text, 'news_time': datetime.strptime(time_span, '%Y-%m-%d %H:%M'),
                            'authority': authority, 'created_time': datetime.now(), 'title': news_title,
                            'photo': image})
