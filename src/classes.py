
import json
import requests
from abc import ABC, abstractmethod


class WorkApi(ABC):
    """ Абстрактный класс для работы с API сайтов с вакансиями. """

    @abstractmethod
    def get_vacancies(self):
        """ Абстрактный метод для подключения к API и получения вакансий. Реализуется в дочерних классах. """
        pass

    @abstractmethod
    def get_choice_vacancies(self):
        """ Абстрактный метод для выборки вакансий по заданным параметрам. Реализуется в дочерних классах. """
        pass


class HeadHunterApi(WorkApi):
    """ Класс для работы с вакансиями через API сайта hh.ru. """

    def get_vacancies_hh(self):
        """ Метод для подключения к API и получения вакансий с hh.ru. """
        pass

    def get_choice_vacancies_hh(self):
        """ Метод для выборки вакансий по заданным параметрам с hh.ru. """
        pass


class SuperJobApi(WorkApi):
    """ Класс для работы с вакансиями через API сайта sj.ru. """

    def get_vacancies_sj(self):
        """ Метод для подключения к API и получения вакансий с sj.ru. """
        pass

    def get_choice_vacancies_sj(self):
        """ Метод для выборки вакансий по заданным параметрам с sj.ru. """
        pass
