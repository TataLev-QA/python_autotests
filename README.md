<h2>Автотесты на API проекта «Битва покемонов»</h2>

> **Статус проекта:**
> Проект закрытый для POST запросов, но GET можно выполнять без токена: https://pokemonbattle.me/
> 
> 🟢 Поддерживается (активный) 

## Описание проекта и задачи
Автоматизировать часть проверок регресса с помощью Pytest и Requests

## Тест-кейсы, которые автоматизировали
* Создание покемона `POST /pokemons`
* Смена имени покемона `PUT /pokemons`
* Поймать покемона в покебол `POST /trainers/add_pokeball`
* Проверить ответ метода `GET /trainers`

Ожидаемый ответ: 
* response `status code` = 200
* в ответе в `json` приходит корректное поле `trainer_name`
* в ответе приходит корректное поле id в json

## Детали реализации

1. Автотесты написаны с применением PyTest
2. Используется библиотека Requests
3. Параметризированные тесты с использованием декоратора

![image](https://raw.githubusercontent.com/TataLev-QA/python_autotests/main/python_1.jpg)

## Локальный запуск тестов (из терминала)
1. Скачать проект
2. Перейти через терминал в директорию проекта
2. Выполнить команду:

Создаём виртуальное окружение внутри папки проекта.
Далее команды для MacOS (для windows инуструкция [есть вот тут](https://realpython.com/python-virtual-environments-a-primer/#create-it))

``` markdown
python3 -m venv venv
```

``` markdown
source venv/bin/activate
```

4. Устанавливаем библиотеки

``` markdown
python3 -m pip install requests
```

``` markdown
python3 -m pip install pytest
```

5. Запускаем
``` markdown
pytest tests/test_pokemon.py
```

Ожидаемый результат: получим отчет о прохождении тестов.


## Автор

Татьяна Карнаухова ([@levtata](https://t.me/levtata))
