

#### Это  микросервис по загрузкефайлов.


#### Как запустить dev-версию сервиса


Скачайте код:
```sh
git clone https://github.com/Michael-Zapivahin/django-selery-docker
```

Перейдите в каталог проекта:
```sh
cd django-selery-docker/project
```

[Установите Python](https://www.python.org/), если этого ещё не сделали.

Проверьте, что `python` установлен и корректно настроен. Запустите его в командной строке:
```sh
python --version
```
**Важно!** Версия Python должна быть не ниже 3.10.

Возможно, вместо команды `python` здесь и в остальных инструкциях этого README придётся использовать `python3`. Зависит это от операционной системы и от того,

установлен ли у вас Python старой второй версии.

В каталоге проекта создайте виртуальное окружение:
```sh
python -m venv venv
```
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`


Установите зависимости в виртуальное окружение:
```sh
pip install -r requirements.txt
```

Определите переменные окружения. Создать файл `.env` в каталоге `project/` с содержанием:
```sh
FILES_DIR = 'files'
```

Создайте файл базы данных:

```sh
python manage.py migrate
```
Запустите сервер:

```sh
python manage.py runserver
```

Откройте сайт в браузере по адресу [http://127.0.0.1:8000/api/files](http://127.0.0.1:8000/api/files). 

Запустите Redis  в новом окне терминала

``` cli
docker run -p 6379:6379 --name some-redis -d redis
```
Запустите Celery  в новом окне терминала
```cli
celery -A picasso worker --loglevel=info
```

Сервис готов к работе.

Запуск тестов из каталога project/
```cli
python manage.py test file_app
```


## Развертывание проекта с помощью `Docker`

Для настройки переменных окружения используется файл `.env.dev` аналогичный `.env`

Обратитесь к пункту `Как запустить prod-версию сайта`, чтобы заполнить `.env.dev`.

Настройки, что для `Development`, что для `Production` фактически идентичны, разница лишь в настройке `DEBUG`. Для `Production` она со значением `False`.

### _Development_
Разворачиваем проект после того, как соберём фронтенд. Обратитесь к пункту из `README` - `Собрать фронтенд`.

Перейдите в директорию `django-selery-docker/` и выполните команду:
```
docker-compose -f docker-compose.yml up -d --build
```
После того, как проект будет развернут необходимо выполнить маграции:
```
docker-compose -f docker-compose.prod.yml web python manage.py migrate
```
Сервис будет доступен по [адресу](http://0.0.0.1:8000/api/).



