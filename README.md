### Процесс запуска

Создать виртуальное окружение командой: python -m venv venv
Активировать его командой: venv/Scripts/activate
Клонировать репозиторий: git clone https://github.com/7Sunset7/app_nasa.git
Перейти в директорию app_nasa: cd app_nasa
Установить зависимости: pip install -r requirements.txt
Указать в файле .env свои данные для бд
Провести миграции командами: python manage.py makemigrations, python manage.py migrate
Создать суперпользователя: python manage.py createsuperuser




 
 
