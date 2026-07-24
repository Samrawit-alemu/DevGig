# DevGig Backend API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## 📖 Overview

**DevGig** is a robust, asynchronous RESTful API backend designed for a freelance job marketplace platform. Built with **FastAPI** and **MongoDB**, it provides secure user authentication, JWT-based authorization, and comprehensive job management (CRUD) capabilities. 

This project demonstrates modern Python backend development practices, focusing on performance, security, and clean code architecture.

## ✨ Key Features

- **Asynchronous by Design**: Built entirely with async Python using FastAPI, Motor (Async MongoDB Driver), and Beanie ODM for high concurrency and performance.
- **Secure Authentication**: Implements industry-standard OAuth2 with Password Flow, utilizing JSON Web Tokens (JWT) for secure session management and password hashing for data protection.
- **Job Management (CRUD)**: Complete endpoints to Create, Read, Update, and Delete job postings, with authorization checks to ensure users can only modify their own postings.
- **Data Validation & Serialization**: Leverages Pydantic models for strict input validation, ensuring data integrity and automatically generating interactive API documentation.
- **CORS Ready**: Pre-configured Cross-Origin Resource Sharing (CORS) to seamlessly integrate with modern frontend frameworks (e.g., React, Next.js, Vue) running on standard development ports.

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs with Python.
- **Database**: [MongoDB](https://www.mongodb.com/) - NoSQL database for flexible data storage.
- **ODM**: [Beanie](https://beanie-odm.dev/) - Asynchronous Python object-document mapper (ODM) for MongoDB.
- **Authentication**: JWT (JSON Web Tokens), Passlib (Bcrypt for hashing), python-multipart.
- **Validation**: Pydantic.

## 📁 Project Structure

```text
devgig_backend/
├── app/
│   ├── api/           # API Routers (Endpoints for Auth and Jobs)
│   ├── auth/          # Authentication logic and Security (JWT, Hashing)
│   ├── models/        # Database Models (Beanie/MongoDB Documents)
│   ├── schemas/       # Data Validation Schemas (Pydantic)
│   ├── config.py      # Environment Configuration
│   ├── deps.py        # Dependency Injection (e.g., get_current_user)
│   └── main.py        # FastAPI Application Entry Point & Lifespan
├── requirements.txt   # Project Dependencies
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- A running MongoDB instance (Local or MongoDB Atlas)

### Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd devgig_backend
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Create a `.env` file in the root directory (or configure your environment) with the necessary variables defined in `app/config.py` (e.g., `DATABASE_URL`, `DATABASE_NAME`, `SECRET_KEY`, `ALGORITHM`).

### Running the Application

Start the development server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The API will be accessible at `http://127.0.0.1:8000`.

## 📚 API Documentation

FastAPI automatically generates interactive API documentation. Once the server is running, you can access:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 🤝 Endpoints Overview

- **Authentication (`/auth`)**:
  - `POST /auth/register` - Register a new user.
  - `POST /auth/login` - Authenticate and receive a JWT access token.
  - `GET /auth/me` - Get current authenticated user details.

- **Jobs (`/api/v1/jobs`)**:
  - `GET /api/v1/jobs` - List all job postings.
  - `POST /api/v1/jobs` - Create a new job posting (Requires Auth).
  - `GET /api/v1/jobs/{job_id}` - Get details of a specific job.
  - `PUT /api/v1/jobs/{job_id}` - Update a job posting (Requires Auth & Ownership).
  - `DELETE /api/v1/jobs/{job_id}` - Delete a job posting (Requires Auth & Ownership).
