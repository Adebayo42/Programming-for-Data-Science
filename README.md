# Student Assessment Monitoring System
This repository contains a Python project aimed at developing a student monitoring system for a module leader. The system enables the module leader to track student engagement with online test activities, analyze student performance, identify underperforming students, and recognize hardworking students.

## Purpose:
The primary objective of this project is to facilitate the module leader in monitoring student engagement and performance through a user-friendly interface. The system processes raw datasets from the module's VLE page, cleans and stores the data in an SQLite database, and provides various functionalities for analyzing and visualizing student assessment data.

## Main Features:
### Data Preprocessing (CWPreprocessing.py):

- Processes raw CSV files containing student test results.
- Cleans the data, including renaming columns, handling null values, and removing redundant columns.
- Standardizes grades to a scale of 100 and stores cleaned data in an SQLite database.

### Test Results Retrieval (testResults.py):

- Retrieves all test scores of a student from the database.
- Displays a complete list of the student's assessments with associated marks.
- Utilizes Matplotlib for suitable visualization of test results.

### Student Performance Analysis (studentPerformance.py):

- Determines a student's performance on each test question.
- Calculates both absolute and relative performances for each question.
- Visualizes student performance metrics for effective analysis.

### Identification of Underperforming Students (underperformingStudent.py):

- Analyzes test results in the database to identify underperforming students.
- Sorts student IDs by their grades of the summative online test.
- Highlights the lowest grade of formative tests for each student.

### Recognition of Hardworking Students (hardworkingStudents.py):

- Generates a list of hardworking students based on their summative test grades and self-ratings.
- Organizes student IDs, test grades, and ratings in descending order of grades.

### Graphical User Interface (menu.ipynb):

- Provides an intuitive menu for the module leader to access various functionalities.
- Based on a Python Graphical User Interface (GUI) using IPyWidgets for ease of use.

## Project Summary
This project demonstrates proficiency in Python programming, data preprocessing, database management, and interactive visualization techniques. The structured and user-friendly interface enhances accessibility and usability for module leaders in monitoring and analyzing student assessment data.
