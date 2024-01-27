
import json
import requests
from abc import ABC, abstractmethod
import os


class WorkApi(ABC):
    """ Абстрактный класс для работы с API сайтов с вакансиями. """

    @abstractmethod
    def get_vacancies(self, prof):
        """ Абстрактный метод для подключения к API и получения вакансий. Реализуется в дочерних классах. """
        pass

    @abstractmethod
    def get_choice_vacancies(self, prof):
        """ Абстрактный метод для выборки вакансий по заданным параметрам. Реализуется в дочерних классах. """
        pass


class HeadHunterApi(WorkApi):
    """ Класс для работы с вакансиями через API сайта hh.ru. """

    page = 1

    def get_vacancies(self, prof):
        """ Метод для подключения к API и получения вакансий с hh.ru. """

        url = 'http://api.hh.ru/vacancies'

        dict_info = requests.get(f"{url}?text=name:{prof}&area=113&page={self.page - 1}").json()

        return dict_info['items'], dict_info['pages']

    def get_choice_vacancies(self, prof):
        """ Метод для выборки вакансий по заданным параметрам с hh.ru. """

        list_vacancies = self.get_vacancies(prof)[0]
        vacancies = []
        for vacancy in list_vacancies:
            if vacancy['salary'] == None:
                continue

            elif vacancy['salary']['from'] == None:
                continue

            elif vacancy['salary']['to'] == None:
                continue

            else:
                vacancies.append({
                    'name': vacancy['name'],
                    'area': vacancy['area']['name'],
                    'salary_from': vacancy['salary']['from'],
                    'salary_to': vacancy['salary']['to'],
                    'currency': vacancy['salary']['currency'],
                    'description': vacancy['snippet']['responsibility'],
                    'url': vacancy['employer']['alternate_url']
                })
        return vacancies


class SuperJobApi(WorkApi):
    """ Класс для работы с вакансиями через API сайта superjob.ru. """

    page = 1

    def get_vacancies(self, prof):
        """ Метод для подключения к API и получения вакансий с superjob.ru. """

        api_key = os.getenv('SJ_API_KEY')
        headers = {'X-Api-App-Id': api_key}
        params = {'keyword': prof, 'count': 40, 'page': self.page - 1}
        url = 'http://api.superjob.ru/2.20/vacancies/'

        dict_info = requests.get(url, params=params, headers=headers).json()
        return dict_info['objects'], dict_info['total']

    def get_choice_vacancies(self, prof):
        """ Метод для выборки вакансий по заданным параметрам с superjob.ru. """

        list_vacancies = self.get_vacancies(prof)[0]
        vacancies = []
        for vacancy in list_vacancies:
            if vacancy['payment_from'] == 0:
                continue

            elif vacancy['payment_to'] == 0:
                continue
            vacancies.append({
                'name': vacancy['profession'],
                'area': vacancy['town']['title'],
                'salary_from': vacancy['payment_from'],
                'salary_to': vacancy['payment_to'],
                'currency': vacancy['currency'],
                'description': vacancy['work'],
                'url': vacancy['link']
            })
        return vacancies


class Vacancies:
    """ Класс для работы с вакансиями """
    def __init__(self, name, area, salary_from, salary_to, currency, description, url):
        self.name = name
        self.area = area
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.description = description
        self.url = url

    def __str__(self):
        return (f"Профессия: {self.name}\n"
                f"Место: {self.area}\n"
                f"Зарплата от {self.salary_from} до {self.salary_to} {self.currency}\n"
                f"Обязанности: {self.description}\n"
                f"Ссылка: {self.url}\n")

    def __gt__(self, other):
        return self.salary_from > other.salary_from


class SaveToJson:
    """ Класс для сохранения данных в json-файл """

    def write_vacancies_to_json(self, data_list):
        """ Метод для создания json-файла и записи в него данных """
        with open('data/vacancies.json', "w", encoding=('utf-8')) as file:
            json.dump(data_list, file, ensure_ascii=False, indent=4)

    def read_vacancies_from_json(self):
        """ Метод для создания экземпляров класса из json-файла """
        with open('data/vacancies.json', 'r', encoding=('utf-8') ) as file:
            vacancies = json.load(file)

        list_vacancies = []
        for item in vacancies:
            list_vacancies.append(Vacancies(item['name'],
                                            item['area'],
                                            item['salary_from'],
                                            item['salary_to'],
                                            item['currency'],
                                            item['description'],
                                            item['url']))
        return list_vacancies
