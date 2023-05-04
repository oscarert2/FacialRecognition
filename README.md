Face Recognition App

View the working project on this github pages.

https://oscarert2.github.io/FacialRecognition/

This is a face recognition app built with Django and various Python libraries. It allows users to take a photo with their webcam and compare it to a database of stored images to find the closest match.
Installation

    Install Python 3.11
    pip install pipenv
    cd Django
    pipenv shell
    pipenv install Django
    cd facialreq
    python manage.py runserver
    Open your web browser and go to http://localhost:8000 to access the app.

Usage

    Once you have installed all the necessary libraries and dependencies, run the command python manage.py runserver in your terminal
    within the folder called facialreq to start the Django development server.
    Open your web browser and go to http://localhost:8000 to access the app.
    Click on the "Start Camera" button to activate your webcam and take a photo.
    Once you have taken a photo, click on the "Recognize" button to compare it to the stored images in the database.
    The app will display the closest match, along with a percentage indicating the degree of similarity.

![Alt text](https://cdn.discordapp.com/attachments/410145817501106186/1103529769028550746/image.png)


![Alt text](https://cdn.discordapp.com/attachments/410145817501106186/1103531524965548082/image.png)

click results to view if the face was in the database

![Alt text](https://media.discordapp.net/attachments/410145817501106186/1103802843590299718/image.png?width=705&height=476)

Libraries Used

    Django
    NumPy
    OpenCV
    face_recognition
    Matplotlib
    scikit-learn
    Pandas
    Pickle
