# Online Library 📚  
Проект для управления онлайн-библиотекой с возможностью бронирования книг, оставления отзывов и рекомендаций.  

## Основные особенности  
- **Каталог книг**: Фильтры по жанрам, авторам, наличию, поиск по названию/автору.  
- **Бронирование**: Авторизованные пользователи могут забронировать книги на 2 дня.  
- **Отзывы и рейтинги**: Возможность оценить и прокомментировать только прочитанные книги.  
- **Рекомендации**: Персонализированные подборки на основе истории чтения.  
- **Админка**: Управление книгами, пользователями и наличием экземпляров.  
- **Мультилокации**: Поддержка нескольких филиалов библиотеки с картой Google Maps.  

## Используемые технологии  
- **Backend**: Python (Django, DRF), PostgreSQL, JWT.  
- **Frontend**: React, TypeScript, Redux Toolkit, Axios.  
- **Интеграции**: Google Maps API, SMTP-сервер для email-уведомлений.  
- **Деплой**: Docker, Nginx, Gunicorn (опционально).  

## Требования  
### Backend  
- Python 3.10+  
- PostgreSQL 14+  
- Django 4.2  
- DRF 3.14  
- JWT 1.7  

### Frontend  
- Node.js 18.x  
- React 18  
- TypeScript  

## Установка  
### Backend  
1. Клонируйте репозиторий:
    ```bash
   git clone https://github.com/anny-tar/Online-Library.git
   cd online-library/backend  
2. Установите зависимости:
    ```bash
   pip install -r requirements.txt  
3. Настройте PostgreSQL:
   - Создайте базу данных и пользователя.
   - Обновите settings.py с учетными данными БД.
4. Примените миграции:
    ```bash 
   python manage.py migrate  
5. Запустите сервер:
    ```bash 
   python manage.py runserver  

### Frontend  
1. Перейдите в папку фронтенда
    ```bash 
    cd ../frontend  
2. Установите зависимости:
    ```bash
   npm install  
3. Запустите локальный сервер:
    ```bash
   npm start  

## Переменные окружения
Создайте .env в папке backend:
SECRET_KEY=your_django_secret_key  
DEBUG=True  
ALLOWED_HOSTS=localhost,127.0.0.1  
DATABASE_URL=postgres://user:password@localhost:5432/dbname  
EMAIL_HOST_USER=your_email@example.com  
EMAIL_HOST_PASSWORD=your_email_password 

## Структура проекта
СТРУКТУРА

## Автор
- Тарасова Анна Алексеевна, студент ПИБ-21, ПривГУПС, https://github.com/anny-tar.

## Лицензия
MIT License