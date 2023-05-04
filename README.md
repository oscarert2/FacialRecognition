Face Recognition App

This is a face recognition app built with Django and various Python libraries. It allows users to take a photo with their webcam and compare it to a database of stored images to find the closest match.
Installation

    Install Python 3 on your computer.
    Install pipenv by running pip install pipenv in your terminal or command prompt.
    Clone this repository to your local machine.
    Navigate to the project directory in your terminal or command prompt.
    CD into the Django directory.
    Run pipenv shell to create a virtual environment.
    Run pipenv install to install all the required libraries and dependencies, including Django, NumPy, OpenCV, and face_recognition.

Usage

    Once you have installed all the necessary libraries and dependencies, run the command python manage.py runserver in your terminal
    within the folder called facialreq to start the Django development server.
    Open your web browser and go to http://localhost:8000 to access the app.
    Click on the "Start Camera" button to activate your webcam and take a photo.
    Once you have taken a photo, click on the "Recognize" button to compare it to the stored images in the database.
    The app will display the closest match, along with a percentage indicating the degree of similarity.

Libraries Used

    Django
    NumPy
    OpenCV
    face_recognition
    Matplotlib
    scikit-learn
    Pandas
    Pickle
