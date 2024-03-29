# Pull base image
FROM python:3.9

#PSQL Dependencies Source: https://docs.divio.com/en/latest/how-to/install-system-packages/#install-system-packages
RUN apt-get update -y
RUN apt-get install -y postgresql-client

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
# Problem statement
RUN pip install pipenv && pipenv install --system
RUN pip install --upgrade pip
RUN pip install djangorestframework
RUN pip install django-cors-headers

# Copy project
COPY . /code/
