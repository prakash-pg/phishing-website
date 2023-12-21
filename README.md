# Phishing Website Detection with Django

This repository contains a Django web application for detecting whether a given website is phishing or not. The detection is based on a machine learning model implemented using the RandomForestClassifier from scikit-learn. The trained model is loaded into the Django web application, allowing users to input a website URL and receive a prediction regarding its phishing status.



- phish_detect: Django app containing the main logic for web application functionality.
- static: Static files (CSS and JavaScript) for styling and client-side functionality.
- templates: HTML templates for rendering web pages.
- manage.py: Django management script for various tasks.

### Prerequisites

Make sure you have the following installed:

- Python (>=3.6)
- Django
- scikit-learn
- pandas
- numpy

Install the required packages using:

```bash
pip install -r requirements.txt
```

### Model File

Place the trained machine learning model file `Phishing.pickle` in the project root directory.

### Running the Application

Navigate to the project directory and run the following commands:

```bash
python manage.py migrate
python manage.py runserver
```

Visit [http://localhost:8000/](http://localhost:8000/) in your web browser to access the application. 

## Usage

1. Enter a website URL in the provided input field on the homepage.
2. Click the "Detect" button to submit the URL for phishing detection.
3. View the prediction result displayed on the webpage.

