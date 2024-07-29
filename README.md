# Dosa Orders Management System

Welcome to the Dosa Restaurant API! This project provides a fastAPI for managing orders and customers of a Dosa restaurant. It enables functionalities like creating, updating, and retrieving orders, as well as managing customer information

## Features

Order Management: Create, update, retrieve, and delete orders. Customer Management: Add, update, retrieve, and delete customer details. Item Management: Add, update, retrieve, and delete menu items. Technology Stack

This project is built using Python and SQLite databases. It utilizes the FastAPI framework for building the RESTful API and SQLite for data storage.

## Components
1) FastAPI: A modern, fast (high-performance), web framework for building APIs with Python.
2) SQLite Database: A lightweight disk-based database that doesn't require a separate server process. Installation


## Files

- `init_db.py`: Script to initialize the SQLite database and create the necessary tables.
- `main.py`: FastAPI application to perform CRUD operations on the orders table.
- `db.sqlite`: The SQLite database file.
- `example_orders.json` : Raw data file.

## Setup and Installation
1) Make sure python 3.x is installed in your system
2) Clone the repo into the desired directory
3) Ensure the JSON file with orders (example_orders.json) is placed in the correct directory as specified in the script or you can change the directory according to your configuration.
4) After setting up, run the main.py pyhton file which will lauch the server.
5) The server will start running on http://localhost:8000 by default.

## Prerequisites

- Python 3.x
- SQLite
- FastAPI

## Installation

1. **Clone the repository or download the files:**

    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install the required Python packages:**

    ```sh
    pip install fastapi
    ```
3. **Running the code**
   ```sh
   fastapi dev main.py
   ```

## API Endpoints
The API offers the following endpoints:
1) Orders: CRUD operations for managing orders. Customers: CRUD operations for managing customer information. Items: CRUD operations for managing menu items. For detailed information about each endpoint, refer to the API documentation.
2) API Documentation Explore the API documentation to learn about available endpoints and how to interact with them. You can access the documents at the location "http://127.0.0.1:8000/docs".

## Contributing
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. 

## License
This project is licensed under the MIT License.
