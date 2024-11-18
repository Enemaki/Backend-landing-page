## Secure User API with JWT Authentication (Django REST Framework)

This project is a backend API built with Django REST Framework to handle user registration, login, and authorization for a potential React landing page application. It offers a secure foundation for user management with JSON Web Token (JWT) based authentication.

Features:

  * User Model: Defines user data fields (e.g., username, email, password) and related functionalities.
  * Registration Endpoint: Allows users to create new accounts with secure password hashing.
  * Login Endpoint: Enables existing users to log in and receive JWT tokens for authorization.
  * JWT Authentication: Implements token-based authentication for secure access to protected resources in the future.
  * Authorization: Validates JWT tokens provided in requests for accessing protected API endpoints (not included in this initial version).

Important Note: This project focuses on user management functionalities. Integrating this API with a React landing page requires additional development on the frontend.

### Technologies Used

  * Python (3.x)
  * Django ([Django Web Framework](https://www.google.com/url?sa=E&source=gmail&q=https://www.google.com/url?sa=E%26source=gmail%26q=https://www.djangoproject.com/))
  * Django REST Framework ([Django REST framework](https://www.google.com/url?sa=E&source=gmail&q=https://www.google.com/url?sa=E%26source=gmail%26q=https://www.django-rest-framework.org/))

### Setting Up

1.  Clone the Repository:

<!-- end list -->

```bash
git clone https://github.com/your-username/secure-user-api.git
```

2.  Create a Virtual Environment (recommended):

<!-- end list -->

```bash
python3 -m venv venv
source venv/bin/activate
```

3.  Install Dependencies:

<!-- end list -->

```bash
pip install -r requirements.txt
```

4.  Run Django Migrations:

<!-- end list -->

```bash
python manage.py migrate
```

5.  Run Django Development Server:

<!-- end list -->

```bash
python manage.py runserver
```

This will start the Django development server and expose the API at http://127.0.0.1:8000/ by default.

### API Endpoints:

  * POST register: Registers a new user.
  * POST login: Logs in a user and returns a JWT token upon successful authentication.

Note: Authorization functionalities are not currently implemented in the API endpoints. Future development can involve creating protected endpoints and integrating JWT validation into the API views.

### Integrating with React Landing Page:

  * Configure the React application to send user credentials (username/email and password) to the login endpoint (`/api/v1/auth/login`).
  * Upon successful login, store the received JWT token securely in the React application (e.g., local storage with appropriate security measures).
  * Include the JWT token in the Authorization header of subsequent API requests to access protected resources (future implementation).

### Understanding the Code:

Explore the project code to see how user management is implemented:

  * models.py: Defines the User model with relevant fields and password hashing functionalities.
  * serializers.py: Serializers define how data is formatted for API responses and requests.
  * views.py: Views handle user registration, login, and JWT token generation.
  * auth.py: (Optional) You can create a custom authentication backend to handle JWT verification and user access control (for future authorization).

### Contributing

This project provides a secure user management API. Feel free to fork the repository and contribute\! You can explore:

  * Implementing authorization for protected API endpoints.
  * Adding functionalities like password reset or email verification.
  * Integrating social login options.

### License

This project is licensed under the MIT License. See the LICENSE file for details.
