# Securing Django Rest Framework with JWT Authentication in HttpOnly Cookie

![drf-jwt-httponly-part-1](https://github.com/user-attachments/assets/32684c54-ce68-405d-88b0-6e19c2734394)

## Overview

This project is a practical implementation of JWT-based authentication in **Django Rest Framework (DRF)** using
**SimpleJWT**. This project is designed to demonstrate how to build a secure authentication system with JWT and handle
token storage in HttpOnly cookies.

The article accompanying this project covers the following topics:

+ Introduction to Authentication and JWT
+ Create a Django Project
+ Install and Configuring SimpleJWT
+ Implement Login API and Storing Tokens in HttpOnly Cookies
+ Implement Refresh Token API
+ Implement JWT Authentication with Cookies
+ Testing Authentication

## How to Run the Project

Follow these steps to set up and run the project locally:

### 1. Prerequisites

Before running the project, ensure you have the following installed:

- Docker
- Docker Compose

### 2. Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/mobinghoveoud/drf-jwt-httponly-cookie.git
cd drf-jwt-httponly-cookie
```

### 3. Set Up Environment Variables

Copy the `.env.example` file to `.env` and complete the values as necessary:

```bash
cp .env.example .env
```

Make sure to configure sensitive information like secret keys, database credentials, etc.

### 4. Run the Project

Now, use Docker Compose to start the application:

```bash
docker-compose up
```

This will start the Django application and all necessary services.

### 5. Access the Application

Once the Docker containers are running, you can access the API at `http://localhost:8000/`.

## Contributions

Feel free to contribute, report issues, or leave feedback through GitHub issues or the comment section of the articles.
