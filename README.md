# Процесс запуска

1. Создать виртуальное окружение командой: `python -m venv venv`
2. Активировать его командой: `venv/Scripts/activate`
2. Клонировать репозиторий: `git clone https://github.com/7Sunset7/app_nasa.git`
4. Перейти в директорию app_nasa: `cd app_nasa`
5. Установить зависимости: `pip install -r req.pip`
6. Указать в файле .env свои данные для бд
7. Провести миграции командами: `python manage.py makemigrations`, `python manage.py migrate`
8. Создать суперпользователя: `python manage.py createsuperuser`
9. Запустить сервер: `python manage.py runserver`
