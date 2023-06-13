# googlemaps-api-tests
Этот проект посвящён тестированию GoogleMaps API (API - копия авторства Rahul Shetty).

Чтобы запустить тесты локально:
1. Склонируйте репозиторий
2. Установите virtualenv `pip install virtualenv`
3. Откройте проект в PyCharm, задайте Python Interpreter, задайте виртуальное окружение
4. Установите зависимости `pip install -r requirements.txt`
5. Запустите тесты в PyCharm или в командной строке:
`pytest . --alluredir=test_results -s -v`
6. Чтобы посмотреть отчёт о тестах, выполните `allure serve test_results`

Чтобы запустить тесты в Docker:
1. Склонируйте репозиторий
2. Из корневой директории проекта выполните в терминале `docker-compose up --build`
