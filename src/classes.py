
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

        response = requests.get(f"{url}?text=name:{prof} AND {area}").json()

        with open('../data/hh_vacancies.json', 'w', encoding=('UTF-8')) as file:
            json.dump(response, file, ensure_ascii=False, indent=4)

        with open('../data/hh_vacancies.json', 'r', encoding=('UTF-8')) as file:
            dict_info = json.load(file)
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
                    'salary_from ': vacancy['salary']['from'],
                    'salary_to': vacancy['salary']['to'],
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


h1 = HeadHunterApi()
print(h1.get_choice_vacancies('швея',  'краснодар'))
