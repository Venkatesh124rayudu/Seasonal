# Seasonal Flavors Django Project

This project is a Django web application that manages seasonal flavors for a chocolate house. It allows users to suggest new flavors, manage ingredients, and view customer suggestions and orders.

## Requirements

- Python 3.x (preferably Python 3.10 or higher)
- Django 5.x
- SQLite (for development environment, no setup required)
- Docker (optional, for containerized setup)

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/seasonal-flavors.git
cd seasonal-flavors

2. Create a Virtual Environment

It is recommended to create a virtual environment to isolate project dependencies.

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install Dependencies

Install the necessary Python dependencies listed in requirements.txt:

pip install -r requirements.txt

Ensure that the following packages are included:

    Django
    Other dependencies used in the project

4. Migrate the Database

Run the following command to set up the database tables:

python manage.py migrate

5. Start the Development Server

To run the project locally, start the Django development server:

python manage.py runserver

By default, the application will run on http://localhost:8000/.
6. Access the Application

    Navigate to http://localhost:8000/seasonal-flavors/ to view the list of seasonal flavors.
    You can add new seasonal flavors or view existing ones.
    To manage ingredients, visit the "Ingredient Inventory" section.
    Customers can suggest new flavors and provide feedback.
URL Endpoints:

    /seasonal-flavors/ - Displays all seasonal flavors and options to add new ones.
    /ingredient-inventory/ - Displays the ingredients available and allows updates.
    /customer-suggestions/ - Lists customer flavor suggestions and allergy concerns.
    /add-customer-suggestion/ - Form to add a new customer suggestion.
    /add-seasonal-flavor/ - Form to add a new seasonal flavor.
Docker Setup (Optional)

If you want to run the project using Docker, follow these steps:
1. Build the Docker Container

docker-compose up --build

2. Access the Application

The application will be available at http://localhost:8000

The root of the project is http://localhost:8000/seasonal-flavors/
![Screenshot 2024-11-16 183839](https://github.com/user-attachments/assets/1a5dff60-27c1-4169-a505-324b35ffd259)
![Screenshot 2024-11-16 183621](https://github.com/user-attachments/assets/d45900f3-bf4a-4b25-bd2c-a2cfcb6b1249)
![Screenshot 2024-11-16 183658](https://github.com/user-attachments/assets/0d9913e3-c48d-4109-8348-0acb12102292)
![Screenshot 2024-11-16 183738](https://github.com/user-attachments/assets/3f18cbef-cbcb-420c-b89b-85a29d922375)
![Screenshot 2024-11-16 183907](https://github.com/user-attachments/assets/3a87dcd7-50a9-47ad-b1ee-a8595d1707a7)




