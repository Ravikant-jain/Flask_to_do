# Flask To-Do Application

A simple To-Do web application with CRUD operations built using Flask.

## Features
- Add tasks
- Delete tasks
- Edit task
- Simple and lightweight

## Installation and Setup

Follow these steps to set up and run the application:

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/Flask_to_do.git
cd Flask_to_do
```

### 2. Create and Activate a Virtual Environment

#### On Windows:
```sh
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirement.txt
```

### 4. Run the Application
```sh
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## File Structure
```
Flask_to_do/
│── data/              # Task Database (json) 
│── static/css/        # CSS files for styling
│── templates/         # HTML templates
│── .gitattributes     # Git attributes configuration
│── .gitignore         # Ignore unnecessary files in git
│── app.py            # Main application file
│── requirement.txt    # Python dependencies
│── README.md         # Project documentation
```

## License
This project is licensed under the MIT License.

