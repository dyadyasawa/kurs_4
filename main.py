
from src.classes import HeadHunterApi, Vacancies, DataJson

profession = input('По какой профессии вывести вакансии?  >>>  ')
area = input('В каком регионе?  >>>  ')

hh1 = HeadHunterApi()
dj1 = DataJson()

# print(hh1.get_choice_vacancies(profession, area))

print(dj1.write_vacancies_to_json(hh1.get_choice_vacancies(profession, area)))
