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

## Branches and Responsibilities

| Branch Name         | Assigned Member | Responsibility                  |
|---------------------|-----------------|--------------------------------|
| feature-accounts     | Member 1        | Login, register, profile        |
| feature-posts        | Member 2        | Blog posts (create/view)        |
| feature-comments     | Member 3        | Comment system                  |
| feature-layout       | Member 4 (You)  | Navbar, base.html, layout, GitHub |

> ⚠️ Everyone should make changes **only** in their own branch!

---

## How to Switch to Your Branch

Before you start working, run the following commands to get the latest updates and switch to your branch:

```bash
git fetch origin
git checkout feature-branch-name

#Example: 
If your branch is called feature-accounts, run:

git fetch origin
git checkout feature-accounts
