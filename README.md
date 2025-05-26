# Freebie Tracker 

## Overview

The **Freebie Tracker ** is a command-line application that manages relationships between developers,companies,and the freebies that companies give to developers.
***

## Technologies used

- Python3
- SQLAlchemy
- Alembic
- SQLite (for viewing your database in the editor)
- Pipenv (for the virtual environment and dependency management)


## Features

- Track which developers received which freebies from which companies.
- Establish many-to-many relationships uisng an association table('freebies').
- Provide aggregate and custom query methods such as:
  - `Dev#received_one?`
  - `Dev#give_away`
  - ` Company#give_freebie`
  - `Company#oldest_dev`
- Generate and apply database migrations using Alembic.



## Installation

### Getting Started 
1. **Clone the repository**   
Open your terminal and run the following command:
    ```sh
    $git clone https://github.com/awuorochelle75/python-p3-freebie-tracker.git



2. **Navigate to the project folder**
    ```sh
        $cd python-p3-freebie-tracker

3. **Set up and activate a virtual environment with pipenv**
    ```sh
        $pipenv install
        $pipenv shell

4. **Set up the database**
    ```sh
        $alembic upgrade head

5.  **Seed the database**
    ```sh
        $python seed.py

## **Usage**
1. You can run the CLI using:
    ```sh
        $python debug.py

- Then you can interact with your models and database through the interactive shell.


## Models
- Dev
  - id
  - name

- Company
  - id
  - name
  - founding_year

- Freebie(Join Table)
  - id
  - item_name
  - dev_id(FK)
  - company_id(FK)
    



## Contact Information
📧 Email: awuorochelle@gmail.com

## License
📜 MIT License @2025 Rochelle Awuor
