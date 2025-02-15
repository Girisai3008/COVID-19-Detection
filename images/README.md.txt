# COVID-19 Detection Using Machine Learning

## Overview

This project is a COVID-19 infection detection system using various Machine Learning models such as SVM, KNN, Random Forest, Logistic Regression, and Naive Bayes. It includes a GUI-based application built with PyQt5 that allows users to upload datasets, train models, and make predictions. The project also utilizes MySQL for database storage and OpenCV for graphical analysis.

## Features

- **User Authentication**: Secure login and signup.
- **Dataset Upload**: Load CSV datasets for training and testing.
- **Machine Learning Models**: Supports SVM, KNN, Random Forest, Logistic Regression, and Naive Bayes.
- **Performance Analysis**: Graphical comparison of model accuracy.
- **COVID-19 Prediction**: Predicts infection based on input parameters.
- **Database Storage**: Uses MySQL for storing user details and results.

## Technologies Used

- **Programming Language**: Python 3.6+
- **GUI Framework**: PyQt5
- **Machine Learning Libraries**: scikit-learn, pandas, numpy, scipy
- **Database**: MySQL
- **Data Visualization**: Matplotlib, OpenCV

## Installation

1. **Clone the Repository**:
  a) git clone https://github.com/your-username/your-repo-name.git

   b)cd your-repo-name
   
2. **Install Dependencies**:

   a)pip install -r requirements.txt
  
3. **Set Up Database**:
   - Import covid-19.sql into MySQL.
   - Update DBconn.py with your MySQL credentials.

## How to Run the Application

1. Open a terminal in the project directory.
2. Run the main application:
  
     python main.py
  
3. Login or Signup to access features.
4. Upload a dataset, train models, and analyze results.

## Folder Structure

```
├── admin.py          # Admin panel
├── classification.py # Model training & evaluation
├── covid.py          # COVID detection logic
├── DBconn.py         # Database connection
├── main.py           # Main application file
├── predictor.py      # Prediction script
├── upload.py         # File upload handling
├── covid_train.csv   # Training dataset
├── covid_test.csv    # Testing dataset
├── covid-19.sql      # MySQL schema
├── images/           # UI and graph images
├── README.md         # Project documentation
├── requirements.txt  # Dependencies file
└── .gitignore        # Ignoring unnecessary files

