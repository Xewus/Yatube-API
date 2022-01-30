API Yatube

"Yatube" - социальная сеть.

К ранее созданному проекту (https://github.com/Xewus/Yatube) добавлено API испоьзуя Django Rest Framework.
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
for Windows:
```
source env/Scripts/activate
```
for Linux:
```
. env/bin/activate
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
- [ ] TODO: Надо починить - вытащить из первого коммита.
