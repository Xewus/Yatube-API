API Yatube

"Yatube" - социальная сеть.

Контент могут создавать только зарегистрированные пользователи.
Для анонимов доступно чтение контента.

К ранее созданному проекту (https://github.com/Xewus/Yatube) добавлено API.
Взаимодествие зарегистрированных пользователей с API требует аутентификации
посредством  JWT-токена.

Инструкции по установке и запуску через терминал:
```
git clone https://github.com/Xewus/api_final_yatube
```
```
cd api_final_yatube/
```
```
python3 -m venv env
```
```
source env/Scripts/activate
```
```
pip install -r requirements.txt
```
```
cd yatube_api/
```
```
python manage.py migrate
```
```
python manage.py runserver
```

Документация будет по ссылке http://localhost:8000/redoc/.
(TODO: Надо починить - вытащить из первого коммита)
