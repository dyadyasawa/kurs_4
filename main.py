
from src.classes import HeadHunterApi, SaveToJson

profession = input('По какой профессии вывести вакансии?  >>>  ')
print()

hh = HeadHunterApi()
save_json = SaveToJson()

save_json.write_vacancies_to_json(hh.get_choice_vacancies(profession))
list_vacancies = save_json.read_vacancies_from_json()

for ex in sorted(list_vacancies):
    print(ex)

