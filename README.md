# Teebay Django Backend Setup Guide

## Follow the steps below to set up and run the project locally.

## Prerequisites

1. **Python 3.12 or Above**

   Ensure that Python version 3.12 or above is installed on your system.  
   You can check your Python version with the following command:

   ```bash
   python3 --version
   ```

## Setup Instructions

1. **Clone the Repository**

   Clone this repository to your local machine and cd into the root folder:

   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a Virtual Environment**

   Create a virtual environment named venv using Python:

   ```bash
   python3 -m venv venv
   ```

   #### Activate the virtual environment:

   **Linux/macOS**:

   ```bash
   source venv/bin/activate
   ```

   **Windows**:

   ```bash
   venv\Scripts\activate
   ```

3. **Install Required Packages**

   Install all the dependencies specified in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   Before applying migrations ensure you're in the project root directory.

   Run the following commands in order to create and apply database migrations:

   - Create migrations for the `users` app:
     ```bash
     python manage.py makemigrations users
     ```
   - Create migrations for the `products` app:
     ```bash
     python manage.py makemigrations products
     ```
   - Create migrations for the `transactions` app:
     ```bash
     python manage.py makemigrations transactions
     ```
   - Apply all migrations
     ```bash
     python manage.py migrate
     ```

5. **Set Up Firebase Admin SDK Credentials**

   Obtain the Firebase Admin SDK credentials file from the link provided in the assessment document.

   - Copy paste the JSON contents in the following file:
     ```bash
     teebay-mobile-assesment-firebase-adminsdk.json
     ```

## Run the Project

Start the development server using the following command:

```bash
python manage.py runserver
```

**Stopping the Server:**
To stop the development server, press `Ctrl + C` in the terminal.
