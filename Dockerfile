# Pull base image
FROM python:3.8

#PSQL Dependencies Source: https://docs.divio.com/en/latest/how-to/install-system-packages/#install-system-packages
RUN apt-get update
RUN apt-get install -y postgresql-client

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /code/
