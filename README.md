Программа получает информацию о вакансиях с разных платформ в России(hh.ru и superjob.ru),
сохраняет ее в json-файл и работает с ним.
Вакансии, у которых зарплата не указана или указана равной нулю не выводятся.
Выводимые данные сортируются по зарплате(от большей к меньшей).
По умолчанию выводится первая страница(нулевой элемент списка).
В дальнейшем есть возможность ввести необходимый номер страницы и просмотреть ее.
Для запроса на superjob.ru необходимо передавать ключ авторизации.
Он хранится в переменной api_key в src/classes.py.
По завершению работы программы просмотренные данные сохраняются в data/vacancies.json.