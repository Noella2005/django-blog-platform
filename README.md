# Django Blog Platform

A beginner-friendly Django blog web application where users can register, create posts, and comment.

## Features

- User authentication (register, login, logout)
- Create, read, update, delete blog posts
- Comment on posts
- Admin panel for managing users and content
- Responsive design with Bootstrap

## Installation

```bash
git clone https://github.com/yourusername/django-blog-platform.git
cd django-blog-platform
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

