
import json
import requests
from abc import ABC, abstractmethod


class WorkApi(ABC):
    """ Абстрактный класс для работы с API сайтов с вакансиями. """

    @abstractmethod
    def get_vacancies(self, prof, area):
        """ Абстрактный метод для подключения к API и получения вакансий. Реализуется в дочерних классах. """
        pass

    @abstractmethod
    def get_choice_vacancies(self, prof, area):
        """ Абстрактный метод для выборки вакансий по заданным параметрам. Реализуется в дочерних классах. """
        pass


class HeadHunterApi(WorkApi):
    """ Класс для работы с вакансиями через API сайта hh.ru. """

    def get_vacancies(self, prof, area):
        """ Метод для подключения к API и получения вакансий с hh.ru. """

        url = 'http://api.hh.ru/vacancies'

        dict_info = requests.get(f"{url}?text=name:{prof} AND {area}").json()

        return dict_info['items']


    def get_choice_vacancies(self, prof, area):
        """ Метод для выборки вакансий по заданным параметрам с hh.ru. """

        list_vacancies = self.get_vacancies(prof, area)
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
                    'salary_from': vacancy['salary']['from'],
                    'salary_to': vacancy['salary']['to'],
                    'currency': vacancy['salary']['currency'],
                    'description': vacancy['snippet']['responsibility'],
                    'url': vacancy['employer']['alternate_url']
                })
        return vacancies

class SuperJobApi(WorkApi):
    """ Класс для работы с вакансиями через API сайта sj.ru. """

    def get_vacancies_sj(self):
        """ Метод для подключения к API и получения вакансий с sj.ru. """
        pass

    def get_choice_vacancies_sj(self):
        """ Метод для выборки вакансий по заданным параметрам с sj.ru. """
        pass


class Vacancies:
    """ Класс для работы с вакансиями """
    def __init__(self, name, salary_from, salary_to, currency, description, url):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.description = description
        self.url = url

    def __str__(self):
        return (f"Профессия: {self.name}\n"
                f"Зарплата от {self.salary_from} до {self.salary_to} {self.currency}\n"
                f"Обязанности: {self.description}\n"
                f"Ссылка: {self.url}\n")

    def __lt__(self, other):
        return self.salary_from < other.salary_from


class SaveToJson:
    """ Класс для сохранения данных в json-файл """
    def write_vacancies_to_json(self, data_list):
        """ Метод для создания json-файла и записи в него данных """
        with open('data/vacancies_hh.json', "w", encoding=('utf-8')) as file:
            json.dump(data_list, file, ensure_ascii=False, indent=4)

    def read_vacancies_from_json(self):
        """ Метод для создания экземпляров класса из json-файла """
        with open('data/vacancies_hh.json', 'r', encoding=('utf-8') ) as file:
            vacancies = json.load(file)

        list_vacancies = []
        for item in vacancies:
            list_vacancies.append(Vacancies(item['name'],
                                            item['salary_from'],
                                            item['salary_to'],
                                            item['currency'],
                                            item['description'],
                                            item['url']))
        return list_vacancies
