Референс - шаблон для сайта Crypto Finder
https://themewagon.com/themes/free-bootstrap-5-cryptocurrency-website-template-cryptocoin/

Референс - шаблон сайта разработка ПО и Сайтов
https://themewagon.com/themes/patrix-free-responsive-bootstrap-5-landing-page-template/

Посмотреть путь в какой папке находимся
pwd

Переход в папку 
CD Имя  Переход назад CD ..

Создать файл зависимостей
pip freeze > "название файла"

Установить пакеты с файла зависимостей
pip install -r req.txt


Создание виртуального окружения
python -m venv venv

# Learningpyh
Запуск консоли Django:
    python manage.py shell

Супер пользователь админ
    $ python manage.py createsuperuser

Создать миграцию
    python manage.py makemigrations

Применить миграцию
    python manage.py migrate

Для запуска проекта:
    1. Создать виртуальное окружение .venv , активировать его.
    2. Установить зависимости из файла req.txt командой pip install req.txt
    3. Установть PosgreSQL 15 версии. https://www.postgresql.org/
    4. Послен установки и настройки PosgreSQL, создать в ней базу данных с названием 'Learning_crypto_DB'.
    5. В файле Settings.py приложения Crypto в DATABASES указать Ваш пароль от базы данных при создании на PosgreSQL
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Learning_crypto_DB',
        'USER': 'postgres',
        'PASSWORD': 'ВАШ ПАРОЛЬ',
        'HOST': 'localhost',
        'PORT': 5432,
        }
    }   
    5. В терминале пререйти в папук Crypto командой CD crypto
    6. Запустить серевер python manage.py runserver
    7. Перейти по ссылкы localhost в браузере - запустится приложение Django
