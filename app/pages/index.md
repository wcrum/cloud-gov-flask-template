Title: Index
Summary: Template cloud.gov Application
Authors: William Crum
Date: January 23, 2022
base_url: /

# Welcome to a Flask Template

This website and code base focuses on demoing a basic server side renders full stack application within the [cloud.gov](https://www.cloud.gov) application factory and cloud.gov User Authentication and Authorization (UAA).

This templates backend is written in Python using Flask micro-web framework. 

## Backend Development
- Python 
- Flask
- SQLModel
- MySQL

The backend is written in Python and Flask with SQLModel as the ORM, using AWS RDS MySQL as the database.


### Backend Connections
- Gunicorn
- PyMySQL

### Technologies and Reasoning
**Flask**: I decided to use flask because the lightweight API and Rendering capabilites.

**SQLModel**: I wanted to use a newer library that handles typing and the ORM. I could of used a mix of pydantic and SQLAlchemy but reasoned using SQLModel (which was traditionally built for FastAPI) I could of done the same thing. Context handling for SQLModel was a bit tricky since Flask was not meant for SQLModel.

## Frontend Development
- Bootstrap 5
- Jdenticon

> Code and Design by William Crum