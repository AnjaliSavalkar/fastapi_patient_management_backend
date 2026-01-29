# 🏥 FastAPI Patient Management Backend

A clean, scalable **FastAPI backend application** for managing patient records.  
This project demonstrates **industry-standard backend structure**, proper separation of concerns, and RESTful API design.

---

## 🚀 Features

- Create, view, update, and delete patient records
- Automatic data validation using **Pydantic**
- Computed fields for **BMI** and **health verdict**
- JSON-based persistence (easy to replace with DB)
- Clean layered architecture (Routes, Services, Models, Utils)
- Interactive API documentation using **Swagger UI**

---


## 📁 Why This Folder Structure?

This project follows a **layered backend architecture** where each folder has a single responsibility.  
This improves **readability, scalability, maintainability, and testability**.

### Folder Responsibilities

- **`app/`** – Core application code  
- **`models/`** – Data schemas and validation (Pydantic models)  
- **`routes/`** – API endpoints (HTTP layer)  
- **`services/`** – Business logic and core rules  
- **`utils/`** – Reusable helper functions (storage, utilities)  
- **`patients.json`** – Lightweight datastore (can be replaced with a database)  

### Why This Matters

- Clean separation of concerns  
- Easy to debug and extend  
- Industry-standard backend design  
- Interview- and production-ready  

> This structure ensures the backend remains clean, scalable, and easy to maintain as the application grows.

---

## 🚀 Run with Docker

Pull the Docker image from Docker Hub and run the FastAPI app:

```bash
# Pull the image
docker pull anjali0000/patient-api:latest

# Run the container
docker run -d -p 8000:8000 anjali0000/patient-api:latest

# Open FastAPI docs in browser
http://127.0.0.1:8000/docs
