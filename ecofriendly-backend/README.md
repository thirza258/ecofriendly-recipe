# Eco Friendly AI Backend

This is the backend for the Eco Friendly AI project. It is a Django application that serves as the API for the project. Thank you to WWF and FloridaMilk for the recipes data. All rights about the recipes are reserved for them.


## Setup Instructions

1. **Create a Virtual Environment:**
    ```sh
    python -m venv env
    ```

2. **Activate the Virtual Environment:**
    - On macOS and Linux:
      ```sh
      source env/bin/activate
      ```
    - On Windows:
      ```sh
      .\env\Scripts\activate
      ```

3. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables:**
    - Copy the example environment file to create your own environment configuration:
      ```sh
      cp env.example .env
      ```

5. **Import Research Data:**
    ```sh
    python manage.py import_research
    ```

6. **Apply Migrations:**
    ```sh
    python manage.py migrate
    ```

7. **Run the Django Development Server:**
    ```sh
    python manage.py runserver
    ```