# QuickMart

A small Django online store with a home page, product listing, search and category filter, product detail pages, login/signup/logout, and a customized admin panel.

## Features
- Home page with search and category filter
- Product detail page
- Sign up, login, logout (Django auth)
- Admin panel for managing categories and products (inline price/stock editing)
- `seed` command to load sample products

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # Windows: copy .env.example .env
python manage.py migrate
python manage.py seed           # sample products
python manage.py createsuperuser
python manage.py runserver
```

- Store: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Project structure

```
config/      project settings and root urls
store/       Category and Product models, views, admin, seed command
accounts/    signup form and auth urls
templates/   base, store and registration templates
static/css/  stylesheet
```

## Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<username>/quickmart.git
git push -u origin main
```
