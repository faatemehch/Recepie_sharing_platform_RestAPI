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

- **Backend**: Django 4.2+, Django REST Framework
- **Authentication**: Djoser with Simple JWT
- **Database**: PostgreSQL (with SQLite for development)
- **Image Handling**: Django Storages (AWS S3 ready)
- **API Docs**: Swagger/OpenAPI with drf-yasg
- **Testing**: Pytest with factory_boy

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- MySQL
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/recipe-sharing-api.git
   cd recipe-sharing-api
