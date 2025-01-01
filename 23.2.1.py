import requests
from bs4 import BeautifulSoup
import pandas as pd
user_login = input('Введите логин пользователя Кинопоиск: ') #Пример: 1761357

def collect_user_rates(user_login):
    page_num = 1

    data = []

    while True:
        url = f'https://www.kinopoisk.ru/user/{user_login}/votes/list/vs/vote/page/{page_num}/#list'
        html_content = requests.get(url).text

        soup = BeautifulSoup(html_content, 'lxml')

        entries = soup.find_all('div', class_=['item', 'item even'])
        print(len(entries))
        if len(entries) == 0:  # Признак остановки
            break

        for entry in entries:
            info = entry.find('div', class_='info')
            nameRus = info.find('div', class_='nameRus')
            film_name = nameRus.find('a').text

            rating = info.find('div', class_='rating')
            kinopoisk_rating = str(rating.find('b')).replace('<b>','').replace('</b>', '')

            user_rating = entry.find('div', class_='vote').text

            data.append({'Название фильма или сериала (год выпуска)': film_name, 'Рейтинг кинопоиска': kinopoisk_rating, 'Рейтинг пользователя': user_rating})

        page_num += 1  # Переходим на следующую страницу

    return data
user_rates = collect_user_rates(user_login)
df = pd.DataFrame(user_rates)

df.to_excel('user_rates.xlsx')