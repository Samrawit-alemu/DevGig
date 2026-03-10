# DevGig Backend API

A RESTful API built with **FastAPI** and **MongoDB**. 

## 🎯 Purpose
This project was built from scratch to learn and practice modern backend development concepts—such as Clean Architecture, JWT Authentication, and Dependency Injection .

## 🛠️ Tech Stack
- **Framework:** FastAPI
- **Database:** MongoDB
- **ODM:** Beanie & Motor
- **Authentication:** OAuth2 with Password (JWT & Bcrypt)
- **Data Validation:** Pydantic (v2)

## 📂 Project Structure
```text
devgig_backend/
├── app/
│   ├── api/           # The Routes (Endpoints)
│   ├── auth/          # Security (JWT, Password Hashing)
│   ├── models/        # Database definitions (Beanie Documents)
│   ├── schemas/       # Data Validation (Pydantic models)
│   ├── config.py      # Environment variables & settings
│   ├── main.py        # Entry point and DB connection
├── requirements.txt
└── .gitignore
