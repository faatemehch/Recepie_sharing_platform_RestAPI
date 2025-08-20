# Recepie_sharing_platform_RestAPI

# 🍳 Recipe Sharing Platform API

![Django REST Framework](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![Djoser](https://img.shields.io/badge/Djoser-2.0-blue?style=for-the-badge)
![PostgreSQL](https://img.shields.io/badge/MySQL-316192?style=for-the-badge&logo=mysql&logoColor=white)

A robust RESTful API for a recipe sharing platform built with Django REST Framework. Features complete user authentication with Djoser, JWT tokens, recipe management, and social features for food enthusiasts.

## ✨ Features

- **🔐 Authentication System**
  - JWT Authentication with Djoser
  - User registration, login, and password reset
  - Email verification
  - Social authentication ready

- **📝 Recipe Management**
  - Create, read, update, and delete recipes
  - Rich text recipe descriptions
  - Image uploads for recipes
  - Categorization and tagging system

- **👥 Social Features**
  - User profiles with bio and avatar
  - Recipe favorites system
  - Rating and review system
  - Follow other users

- **🔍 Search & Filtering**
  - Advanced search across recipes
  - Filter by categories, tags, and ingredients
  - Pagination and ordering

## 🛠️ Tech Stack

- **Backend**: Django 5.0+, Django REST Framework
- **Authentication**: Djoser with Simple JWT
- **Database**: MySQL (with SQLite for development)

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- MySQL
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone [https://github.com/your-username/recipe-sharing-api.git](https://github.com/faatemehch/Recepie_sharing_platform_RestAPI.git)
   cd recipe-sharing-platforn-api

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
4. **Environment configuration**
   ```bash
   cp .env.example .env
   # Edit .env with your database and secret key
5. **Database setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
6. **Run development server**
   ```bash
   python manage.py runserver
