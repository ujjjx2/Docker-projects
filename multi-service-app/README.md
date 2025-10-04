# Multi-Service Docker Application

A containerized Flask backend with Nginx reverse proxy, orchestrated with Docker Compose.

## Features
- Flask REST API backend
- Nginx reverse proxy frontend
- Docker Compose orchestration
- Inter-container networking

## 🛠️ Prerequisites

- Docker installed on your system
- Docker Compose (usually included with Docker Desktop)
- Git for version control

## 📁 Project Structure
<pre>
multi-service-docker-app/
├── docker-compose.yml # Multi-container orchestration
├── backend/
│ ├── Dockerfile # Backend container definition
│ ├── app.py # Flask application
│ └── requirements.txt # Python dependencies
└── frontend/
├── Dockerfile # Nginx container definition
└── nginx.conf # Nginx configuration
</pre>

## Quick Start
git clone https://github.com/ujjjx2/multi-service-docker-app
cd multi-service-docker-app
docker-compose up --build

## Things I learnt
- Multi-container application design
- Dockerfile best practices
- Docker Compose orchestration
- Inter-container networking
- Reverse proxy configuration
- Containerized development workflow
- Production deployment preparation

## ℹ️ Author
Ujjwal Gupta

## 🔗 Links
GitHub: @ujjjx2
<br>
Docker Hub: ujjjx 