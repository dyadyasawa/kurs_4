
from src.classes import HeadHunterApi, SaveToJson


def interaction_with_user():
    """ Функция для взаимодействия с пользователем. """

    print(f"В данном проекте реализуется предоставление информации о вакансиях с платформ hh.ru и superjob.ru,\n"
          f"а также возможность сохранять полученные данные в json-файл и работать с ними.\n")
    print()
    while True:
        letter = input("С какой платформы желаете получить данные? (h - hh.ru  s - superjob.ru  q - выход) >>>  ")
        if letter.lower() == 'h':
            profession = input("По какой профессии вывести вакансии?: ")
            hh = HeadHunterApi()
            save_json = SaveToJson()

            switch = 0
            while switch == 0:
                save_json.write_vacancies_to_json(hh.get_choice_vacancies(profession))
                list_vacancies = save_json.read_vacancies_from_json()
                if len(list_vacancies) == 0:
                    print("Увы, по заданной профессии вакансий не найдено. Попробуйте ввести другие данные.")
                    switch = 1
                else:
                    for ex in sorted(list_vacancies, reverse=True):
                        print(ex)

                    print()
                    print(f"Вакансии отсортированы по зарплате, от большей к меньшей.\n"
                          f"Была выведена страница {HeadHunterApi.page} из {hh.get_vacancies(profession)[1]}.\n")

                    switch1 = 0
                    while switch1 == 0:
                        value = input("Выберите номер страницы для ее просмотра или q для выхода:  ")
                        print()
                        if value.lower() == 'q':
                            quit()

                        elif value.isdigit() is not True:
                            print("Введите корректное значение.")

                        elif int(value) > hh.get_vacancies(profession)[1]:
                            print("Введите корректное значение.")

                        else:
                            HeadHunterApi.page = int(value)
                            switch1 = 1

        elif letter.lower() == 's':
            pass
        elif letter.lower() == 'q':
            quit()
        else:
            print("Введите корректное значение.")


