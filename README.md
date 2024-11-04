# Dummy Data Populator

A Python script that populates a MySQL database with 1,000,000 dummy records for testing, using SQLAlchemy ORM. The data includes random first names, last names, and ages, making it ideal for database testing and development.

## Features

- Populates a `person` table with dummy data, including first name, last name, and age.
- Utilizes SQLAlchemy ORM for smooth database interaction.
- Allows passing database credentials as environment variables directly when running the script.
- Includes a MySQL script for easy setup of the `dummy` database and `person` table.

## Prerequisites

- Python 3.x
- MySQL database
- SQLAlchemy library

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/OluchukwuJoseph/dummy-data-populator.git
   cd dummy-data-populator

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Run the MySQL setup script**:
   Use the provided SQL script to create the database and table structure.
   ```bash
   cat create_dummy_db.sql | mysql -u yourusername -p

4. **Run the script with environment variables:**
   You can pass the necessary database credentials directly in the command line. Replace yourusername, yourpassword, etc., with your actual database credentials.
   ```bash
   DB_USER=yourusername DB_PASSWORD=yourpassword DB_HOST=localhost DB_PORT=3306 DB_NAME=dummy python3 populate_dummy_data.py
   ```
   - `DB_USER`: Your MySQL username
   - `DB_PASSWORD`: Your MySQL password
   - `DB_HOST`: Database host, e.g., `localhost`
   - `DB_PORT`: Database port, e.g., `3306`
   - `DB_NAME`: Database name (e.g., `dummy`)

## Files in the Repository
- populate_dummy_data.py: Main Python script that generates and inserts dummy data.
- create_dummy_db.sql: SQL script to create the dummy database and person table.

## Usage
This script is helpful for development and testing, particularly when:

- You need a large dataset for load testing and performance analysis.
- You want to simulate real-world database interactions.
- You’re testing SQL queries, API endpoints, or analytics tools.

## Example Output
Upon successful execution, the script will add 1,000,000 records to the person table with randomly generated data in each row.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with any improvements.
