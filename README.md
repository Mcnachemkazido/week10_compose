This project is a simple REST API designed to manage a contact list (Create, Read, Update, Delete).
It is built using Python (FastAPI) and stores data in a MySQL database,
The application is fully containerized with Docker,
making it easy to run without installing complex dependencies locally.



Follow these simple steps to use the application:

1. **Start the App**
    Open your terminal in the project folder and run:
    ```
    docker compose up -d
    ```

2.  **Wait for Initialization**
    Please wait about **30 seconds** for the database to finish setting up before making requests.

3.  **Test the API**
    You can check if the API is running by visiting: `http://localhost:8000/contacts`

4.  **Stop the App**
    To stop the containers and clean up, run:
    ```
    docker compose down
    ```