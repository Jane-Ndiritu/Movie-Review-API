# Movie Review API

A fully functional RESTful API that allows users to **create, read, update, and delete movie reviews**. This project simulates a real-world backend development environment, focusing on **database design, API architecture, authentication, and deployment**.

The API enables users to manage reviews for movies while enforcing authentication and authorization rules to ensure data integrity and security.

## Features

* User authentication (register & login)
* Add reviews for movies
* Update existing reviews
* Delete reviews
* View all reviews or reviews for a specific movie
* Secure endpoints with authentication & authorization
* Persistent storage using a relational database
* Deployed to a live environment

---

## Tech Stack

* **Backend:** Django / Django REST Framework *(or Node.js + Express)*
* **Database:** PostgreSQL / MySQL / SQLite
* **Authentication:** JWT (JSON Web Tokens)
* **Deployment:** Render / Railway / Heroku
* **API Style:** RESTful

## Project Structure

```
movie-review-api/
├── app/
│   ├── models/
│   ├── serializers/
│   ├── views/
│   ├── urls.py
│   └── permissions.py
├── manage.py
├── requirements.txt
├── .env
└── README.md
```
## Authentication & Authorization

* Users must register and log in to access protected routes
* JWT tokens are required for creating, updating, or deleting reviews
* Users can only update or delete **their own reviews**
## API Endpoints
### Authentication

| Method | Endpoint              | Description                  |
| ------ | --------------------- | ---------------------------- |
| POST   | `/api/auth/register/` | Register a new user          |
| POST   | `/api/auth/login/`    | Log in and receive JWT token |

### Reviews

| Method | Endpoint             | Description                        |
| ------ | -------------------- | ---------------------------------- |
| GET    | `/api/reviews/`      | Get all reviews                    |
| GET    | `/api/reviews/<id>/` | Get a single review                |
| POST   | `/api/reviews/`      | Add a new review *(auth required)* |
| PUT    | `/api/reviews/<id>/` | Update a review *(owner only)*     |
| DELETE | `/api/reviews/<id>/` | Delete a review *(owner only)*     |

---

## Database Models
### User

* id
* username
* email
* password

### Movie

* id
* title
* release_year

### Review

* id
* movie (Foreign Key)
* user (Foreign Key)
* rating
* comment
* created_at
* updated_at

---

## Setup & Installation

Clone the Repository
git clone https://github.com/your-username/movie-review-api.git
cd movie-review-api
2. Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt
4. Environment Variables

Create a .env file:

SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
5. Run Migrations
python manage.py migrate
6. Start Development Server
python manage.py runserver
### Deployment

The API is deployed to a live environment.

🔗 Live API URL:

https://your-deployed-api-url.com

Deployment includes:

Production-ready database

Environment variables

Secure authentication

### Testing

Manual testing using Postman / Thunder Client

Auth-protected endpoints tested with JWT tokens

Future Improvements

Add movie data from external APIs (TMDB)

Review likes and comments

Role-based access (admin/moderator)

Pagination & filtering

API documentation with Swagger/OpenAPI
