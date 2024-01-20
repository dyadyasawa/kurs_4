
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
        pass
