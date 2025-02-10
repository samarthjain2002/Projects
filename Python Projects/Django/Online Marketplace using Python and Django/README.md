# Online Marketplace

## Introduction
This project is a simple online marketplace built using Django, a Python web framework. Users can sign up, browse, list items for sale, and communicate with other users. The project includes authentication, user-to-user messaging, and a dashboard for managing items.

## Features
- **User Authentication**: Sign up, log in, and log out functionality.
- **Item Listings**: Users can create, edit, delete, and view items.
- **Search & Filtering**: Browse items by categories and search by name or description.
- **User Dashboard**: Manage listed items and track interactions.
- **Messaging System**: Communicate with item sellers.
- **Image Upload**: Upload images for listed items.
- **Responsive UI**: Styled using Tailwind CSS.

## Installation
### Prerequisites
Ensure you have Python installed on your machine. It is recommended to use a virtual environment.

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run database migrations:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to set up an admin account.

6. Start the development server:
   ```sh
   python manage.py runserver
   ```

7. Open your browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Usage
- **Home Page**: Browse the newest items and filter by categories.
- **Sign Up/Login**: Create an account or log in to access features.
- **Listing an Item**: Click "New Item," fill out the form, and upload an image.
- **Item Details**: View an item and contact the seller.
- **Dashboard**: View, edit, or delete your listed items.
- **Messaging**: Send and receive messages with item owners.

## Project Structure
```
├── marketplace/
│   ├── conversations/   # User messaging system
│   ├── core/            # Main app for authentication and static pages
│   ├── dashboard/       # User dashboard
│   ├── env/             # Virtual environment
│   ├── item/            # Handles item listings
│   ├── media/           # Uploaded images
│   ├── puddle/          # Main app
│   ├── db.sqlite3       # SQL database
│   ├── manage.py        # Django management script
└── requirements.txt     # Project dependencies
```

## Technologies Used
- **Django**: Web framework
- **Python**: Backend logic
- **Tailwind CSS**: Styling
- **SQLite**: Default database (can be replaced with PostgreSQL/MySQL)
- **Pillow**: Image handling

## Contributing
Feel free to fork this project and submit pull requests with improvements.

## License
This project is open-source and licensed under the MIT License.

