# Production_simulator(https://productionsimulator.herokuapp.com/)
> Web application that allows to manage projects, employees and tools of production, it also allows to add information(posts) for others employees. + REST API (project maybe be offline due to free tier usage limits on AWS, if you want to see it LIVE let me know)

## Table of contents
* [General info](#general-info)
* [Login details](#login-details)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Contact](#contact)

## General info
### From the beginning the project has assumptions to be made such as:
* DB should be random and logical (imitate real production)
* DB needs to be created automatically and easy to created 
* Django should connect to created DB and get informations from there
* Setup for project should be as easy as possible, with all necessary instrucitons
* for each of the modulus there will be instructions how to run it

<b>REST API</b> documentation -> [API-guide.md](api/API-guide.md)

## Login details
Login as admin:
* username - admin
* password - admin

Or as any user created -> [users_informations.txt](Assets/users_informations.txt)

## Screenshots
![Employee](Assets/img/employee.PNG)
![Information](Assets/img/information.PNG)
![Profile](Assets/img/profile.PNG)
![Project](Assets/img/project.PNG)
![Tool](Assets/img/tool.PNG)

## Technologies
* Python - version 3.8.2
* Django - version 3.05
* PostgreSQL - version 	12.2
* Django REST framework - version 3.11
* AWS(RDS, S3)
* Bootstrap - version 4.4.1
* jquery - version 3.4.1
* HTML5/CSS

## Setup

### Database + local server
1.Install python and PostgreSQL

2.Run

```
    pip install -r requirements.txt
```

3.Create server in PostgreSQL

4.Run [create_db_postgresql.py](Assets/create_db_postgresql.py) (in Assets folder) and follow instructions 

<b>Read comments on the top of the file</b>

### AWS + Heroku
* For instructions to deploy it on AWS go to: [AWS_HEROKU_instructions.md](Assets/AWS_HEROKU_instructions.md)

## Features
List of features:
* Fully functional REST API
* optimized queries
* authorization system(login, logout, register, reset password, update)
* fully functional "blog" with pagination(adjustment for production needs)
* full logic related to the production plant has been preserved
* easy-to-use database search engine based on filters
* fully automatic postgreSQL database creation
* include CRUD
* the tools created by the program could be used in reality, all standards were maintained in their creation
* added caching

## Contact
Created by <b>Marek Chałabis</b> email: chalabismarek@gmail.com
