
# Inventory Management System

This is a REST API for a event management system built using Django REST Framework.


## Features

- Token Based and Access Control authentication system
- CRUD APIs for products
- Search products by names
- Filter products by Event Categories

## Color Reference

| EndPoints             | Descriptions                                                               |
| ----------------- | ------------------------------------------------------------------ |
| register/   |  Sign up new user |
| login/ | Login user and retrieve Django Auth token|
| logout/ | Logout user |
| products/ | Retrieve list of events, search using ?search=, filter using ?category= |
| products/<id>| Retrieve, update or delete a book|


## Deployment

__Installation__
- Clone the repository
- Create and activate a virtual environment
- Install dependencies
```bash
  virtualenv env
  pip install -r requirements.txt
```

__Setup__
- Run migrations
- Create superuser
```bash
  python manage.py migrate
  python manage.py createsuperuser
```
__Run Server__
Start development server
```bash
  python manage.py runserver
```
The API will be available at `http://127.0.0.1:8000/`
