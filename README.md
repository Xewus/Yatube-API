API Yatube
Yatube - учебный проект. В данной части реализован только функционал API.

Контент могут создавать только зарегестрированные пользователи.
Для анонимов доступго чтение контенты.

Взаимодествие зарегистрированных пользователей с API требует аутентификации
посредством  JWT-токена.

Инструкции по установке и запуску через терминал

1. git clone https://github.com/Xewus/api_final_yatube
2. cd api_final_yatube/
3. python -m venv env
4. source env/Scripts/activate
5. pip install -r requirements.txt
6. cd yatube_api/
7. python manage.py runserver
Всё.

Документация будет по ссылке http://localhost:8000/redoc/.
