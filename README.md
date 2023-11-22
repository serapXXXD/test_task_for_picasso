# test_task_for_picasso

## Установка через Docker

### У вас должен быть установлен и запущен Docker


Скопируйте проект командой 
 ```bash
git clone git@github.com:serapXXXD/test_task_for_picasso.git
 ```
Или
 ```bash
git clone https://github.com/serapXXXD/test_task_for_picasso.git
 ```
Откройте его в терминале

Перейдите в 
 ```bash
cd picasso_infra
 ```

Создайте .env файл
 ```bash
touch .env
 ```

Получите новый ключ джанго 
https://djecrety.ir/

Формат ключа:
django-insecure-```jvlf+slausy7o2#ak^%yji@p*g7lx(rxy4m23v1%+kwic_6ign```


Вам нужно заполнить .env по примеру

 ```bash
SECRET_KEY=django-insecure-jvlf+slausy7o2#ak^%yji@p*g7lx(rxy4m23v1%+kwic_6ign
DEBUG=1 
PRODUCTION=1 

POSTGRES_ENGINE='django.db.backends.postgresql_psycopg2'
POSTGRES_NAME=picasso
POSTGRES_USER=picasso
POSTGRES_PASSWORD=posgres
POSTGRES_HOST=data_base
POSTGRES_PORT=5432

ALLOWED_HOSTS=127.0.0.1,localhost

REDIS_HOST=redis
REDIS_PORT=6379
 ```
Пояснения:
 ```bash
После занка "=" пробелов быть не должно!

DEBUG=1 дебаг включен | 0 дебаг выключен

PRODUCTION=1 использует базу данных Postgres | 0 Sqlite

В параметре "ALLOWED_HOSTS" укажите список хостов слитно через запятую
 ```

Запускаем docker-compose

 ```bash
docker-compose up --build -d

 ```

Проверьте запущенные контейнеры 

 ```bash
docker ps
 ```
Должно быть запущенно 5 контейнеров
 ```bash
NAMES
picasso_infra_nginx_1
picasso_infra_backend_1
picasso_infra_celery_1
picasso_infra_data_base_1
picasso_infra_redis_1
 ```

Далее нужно сделать миграцию
 ```bash
docker exec picasso_infra_backend_1 python manage.py migrate
 ```

И собрать статику
 ```bash
docker exec picasso_infra_backend_1 python manage.py collectstatic --no-input
 ```
Переходдим по ссылке

Для загрузки файла

http://localhost/api/v1/upload/

Для получения списка файлов

http://localhost/api/v1/files/

### Для администрирования:

Далее нужно провалиться в образ с бэкэндом
 ```bash
docker exec -it blog_infra_backend_1 sh
 ```

Создайте супер пользователя 
 ```bash
python manage.py createsuperuser
 ```
Заполните требуемые поля

Выходим из образа
 ```bash
exit
 ```

Далее перейдте по ссылке 

http://localhost/admin/

После этого сайтом можно пользоваться