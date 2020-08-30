# Rating App Backend

Настройки Backend
--

Настройте виртульное окружение проекта.

Если хотите использовть sqlite, в settings замените DATABASES, на:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
Если же используете postgresql, то создайте базу данных и пользователя на 
локальной машине, и пропишите их в настройках DATABASES в settings.

Сгенерируйте и поместите ваш секретный ключ в настройку ```SECRET_KEY```.

Настройте состяние дебага ```DEBUG``` (True/False).

Замените ```TIME_ZONE``` на нужную вам.

##### Установите зависимости:
```
$ pip install -r requirements.txt
```

##### Выполните миграции и создание супер пользователя:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

##### Выполните сборку статики:
В backend (там же где лежит файл manage.py) создайте папку с названием 
```static```, затем выполните:
```
python manage.py collectstatic
```

##### Запустите локальный сервер:
```
python manage.py runserver
```

##### Основные url адреса со стороны backend:
```
http://127.0.0.1:8000/admin/          Административная панель django,
http://127.0.0.1:8000/api/courses/    Вывод API приложения courses,
http://127.0.0.1:8000/swagger/        Просмотр автодокументации проекта,
http://127.0.0.1:8000/silk/           Просмотр HTTP запросов.
```
