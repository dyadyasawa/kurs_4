
from src.classes import HeadHunterApi, SuperJobApi, SaveToJson


def interaction_with_user():
    """ Функция для взаимодействия с пользователем. """

    print(f"В данном проекте реализуется предоставление информации о вакансиях с платформ hh.ru и superjob.ru,\n"
          f"а также возможность сохранять полученные данные в json-файл и работать с ними.\n")
    print()
    while True:
        letter = input("С какой платформы желаете получить данные? (h - hh.ru  s - superjob.ru  q - выход) >>>  ")
        if letter.lower() == 'h':
            profession_hh = input("По какой профессии вывести вакансии?: ")
            print()
            hh = HeadHunterApi()
            save_json_hh = SaveToJson()

            switch_hh = 0  # Переключатель для выхода из бесконечного цикла.
            while switch_hh == 0:
                save_json_hh.write_vacancies_to_json(hh.get_choice_vacancies(profession_hh))
                list_vacancies = save_json_hh.read_vacancies_from_json()
                if len(list_vacancies) == 0:
                    print("Увы, по заданной профессии вакансий не найдено. Попробуйте ввести другие данные.")
                    HeadHunterApi.page = 1
                    switch_hh = 1
                else:
                    for ex in sorted(list_vacancies, reverse=True):
                        print(ex)

                    print()
                    print(f"Вакансии отсортированы по зарплате, от большей к меньшей.\n"
                          f"Была выведена страница {HeadHunterApi.page} из {hh.get_vacancies(profession_hh)[1]}.\n")

                    switch1_hh = 0  # Переключатель для выхода из бесконечного цикла.
                    while switch1_hh == 0:
                        value = input("Выберите номер страницы для ее просмотра или q для выхода:  ")
                        print()
                        if value.lower() == 'q':
                            quit()

                        elif value.isdigit() is not True:
                            print("Введите корректное значение.")

                        elif int(value) > hh.get_vacancies(profession_hh)[1]:
                            print("Введите корректное значение.")

                        else:
                            HeadHunterApi.page = int(value)
                            switch1_hh = 1

        elif letter.lower() == 's':
            profession_sj = input("По какой профессии вывести вакансии?: ")
            print()
            sj = SuperJobApi()
            save_json_sj = SaveToJson()

            switch_sj = 0  # Переключатель для выхода из бесконечного цикла.
            while switch_sj == 0:
                save_json_sj.write_vacancies_to_json(sj.get_choice_vacancies(profession_sj))
                list_vacancies = save_json_sj.read_vacancies_from_json()
                if len(list_vacancies) == 0:
                    print("Увы, по заданной профессии вакансий не найдено. Попробуйте ввести другие данные.")
                    SuperJobApi.page = 1
                    switch_sj = 1
                else:
                    for ex in sorted(list_vacancies, reverse=True):
                        print(ex)

                    print()
                    print(f"Вакансии отсортированы по зарплате, от большей к меньшей.\n"
                          f"Была выведена страница {SuperJobApi.page} из {count_of_pages(sj.get_vacancies(profession_sj)[1])}.\n")

                    switch1_sj = 0  # Переключатель для выхода из бесконечного цикла.
                    while switch1_sj == 0:
                        value = input("Выберите номер страницы для ее просмотра или q для выхода:  ")
                        print()
                        if value.lower() == 'q':
                            quit()

                        elif value.isdigit() is not True:
                            print("Введите корректное значение.")

                        elif int(value) > count_of_pages(sj.get_vacancies(profession_sj)[1]):
                            print("Введите корректное значение.")

                        else:
                            SuperJobApi.page = int(value)
                            switch1_sj = 1

        elif letter.lower() == 'q':
            quit()
        else:
            print("Введите корректное значение.")


def count_of_pages(count_of_vacancies):
    """ Возвращает количество страниц по числу вакансий(из расчета 40 вакансий на страницу). """

    if count_of_vacancies / 40 < 1:
        pages = 1
    elif count_of_vacancies / 40 >= 13:
        pages = 13
    elif count_of_vacancies % 40 == 0:
        pages = int(count_of_vacancies / 40)
    else:
        pages = int((count_of_vacancies / 40)) + 1
    return pages
