# The image you are going to inherit your Dockerfile from
FROM python:3.9-alpine

# Set the /django_blog directory as the working directory
WORKDIR /app

RUN addgroup sytemUserGroup && adduser -D -G sytemUserGroup developer 
RUN chmod g+x /app


# Create a user that can run your container
USER developer

# Necessary, so Docker doesn't buffer the output and that you can see the output
# of your application (e.g., Django logs) in real-time.
ENV PYTHONUNBUFFERED 1

# Set environment variables for AWS RDS and S3
COPY ./.env .env

ENV DJANGO_SECRET=${DJANGO_SECRET}


# Copy the requirements.txt file adjacent to the Dockerfile
COPY ./requirements.txt requirements.txt
# Install the requirements.txt file in Docker image
RUN pip install -r requirements.txt

ENV DEBUG=${DEBUG}
# copy the django project into the container image
COPY . .

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]



# RUN docker build -t gcr.io/forward-server-390416/django_blog .