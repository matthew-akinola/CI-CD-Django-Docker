# CircleCI-Django-Docker

This is a Django project for building RESTful APIs using Django and Django REST Framework. It provides a foundation for developing web applications with a focus on scalability, flexibility, and ease of maintenance.

# Features

* Django backend with Django REST Framework for building APIs
* PostgreSQL database for data storage
* Docker for containerization and easy deployment
* CircleCI for continuous integration and continuous deployment (CI/CD)
* AWS S3 for storing static files
* AWS RDS for PostgreSQL as the database service

# Prerequisites

Make sure you have the following installed on your system:

* Python (version 3.9.2)
* Docker (version 20.10.5)
* Docker Compose (version 1.26.2)

Installation

- Clone the repository:
        
    ```bash
    git clone https://github.com/matthew-akinola/CI-CD-Django-Docker
    cd CI-CD-Django-Docker

    ```
- Create a virtual environment and activate it:

    ```bash
        python -m venv env
        source env/bin/activate  # For Linux/Mac
        env\Scripts\activate  # For Windows
    ```
- Setup the environment variables
    * create a .env file and populate with your secret credentials

- install dependencies
    ```bash
        pip install -r requirements.txt
    ```

- collect static files
    
    ```bash
        python manage.py collectstatic
    ```
- make database migration
    
    ```bash
        python manage.py makemigrations
        python manage.py migrate
    ```

- Setup the environment variables
    * create a .env file and populate with your secret credentials

- Start the docker 

    ```bash
        docker-compose -d 
    ```

# For comprehensive navigation of the codebase, checkout this article

https://matthewakinola.hashnode.dev/a-deep-dive-into-containerization-cicd-and-aws-for-django-rest-applications-part-2