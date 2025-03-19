# 🎓 Student Monitoring System

## 🔍 Overview

The **Student Monitoring System** is designed to help **module leaders** track and monitor student engagement with both **formative** and **summative tests**. This system enables educators to gain insights into individual student performance, identify underperforming students, and highlight hardworking students. With the help of an intuitive **Graphical User Interface (GUI)**, module leaders can easily interact with the system and access relevant data to make informed decisions.

The system allows you to:
- View and clean student data.
- Display student test results.
- Track student performance for specific tests.
- Identify underperforming students and highlight hardworking students.

---

## 📌 Key Features:
- ✅ **Interactive GUI**: Easy-to-use interface with intuitive navigation for module leaders.
- ✅ **Test Results Display**: Get the performance results for individual students based on their research ID.
- ✅ **Student Performance Analysis**: Analyze the performance of students across multiple tests.
- ✅ **Identifying Underperforming & Hardworking Students**: Automatically identifies students who are underperforming or showing outstanding effort.
- ✅ **Clean and Preprocess Data**: Load and clean student data, making it ready for analysis.

---

## 🛠 Technology Stack
- **Python** 🐍
- **GUI Framework**: IPython Widgets (ipywidgets)
- **Data Processing**: Custom Python Modules
- **Libraries**: `IPython`, `ipywidgets`, `pandas`

---

## 📂 File Structure:
- **`CWPreprocessing.py`**: Handles data cleaning and preprocessing.
- **`testResults.py`**: Contains functions to display individual student test results.
- **`studentPerformance.py`**: Displays detailed student performance metrics.
- **`underperformingStudent.py`**: Identifies and displays students who are underperforming.
- **`hardworkingStudents.py`**: Identifies and displays hardworking students.

---

## 🛠 How It Works:

1️⃣ **Data Preprocessing & Cleaning**:
   - **Load and Clean Data**: The system starts by loading the student data, ensuring it's clean and ready for further analysis.
   - It performs data cleaning (removing missing or inconsistent data).

2️⃣ **Student Engagement & Performance**:
   - **Student Test Results**: A module leader can enter a student’s research ID to view their test results.
   - **Performance Tracking**: The module leader can enter the student’s research ID and select the test to get a detailed view of their performance.

3️⃣ **Identify Underperforming and Hardworking Students**:
   - The system can identify students who are underperforming or demonstrating exceptional effort and performance.

4️⃣ **Interactive GUI**:
   - The system utilizes **ipywidgets** for an interactive user experience.
   - Several buttons are provided to navigate between the functionalities (e.g., viewing test results, student performance, etc.).

---

## 📊 GUI Layout:

The application is organized into a clean and easy-to-navigate layout:

| **Section**                        | **Button Description**                                               |
|------------------------------------|-----------------------------------------------------------------------|
| **Main Menu**                      | "Welcome to the student's test monitoring system."                   |
| **Data Cleaning**                  | "Load and Clean Data"                                                |
| **Student Test Results**           | "Display Student Test Results"                                       |
| **Student Performance**            | "Display Student Performance"                                        |
| **Underperforming Students**       | "Display Underperforming Students"                                   |
| **Hardworking Students**           | "Display Hardworking Students"                                       |
| **Quit Application**               | "Quit Application"                                                   |

Buttons are used for each operation, and a grid layout is used to display the information and navigate between sections.

---

## 🎯 Key Functions:

- **Clean Data**: The **Load and Clean Data** button will clean and preprocess the dataset for further analysis.
  
- **Display Student Test Results**: Enter a student’s research ID to display their test results.

- **Display Student Performance**: Track and display a student’s performance in a specific test, chosen from available options like **Test 1**, **Test 2**, **Mock Test**, and **Summative Test**.

- **Identify Underperforming Students**: Automatically identify and display students who are underperforming based on predefined criteria.

- **Identify Hardworking Students**: Identify and display students who have shown exceptional engagement and performance.

- **Quit Application**: Exit the system gracefully with a simple message.

---

## 🔧 GUI Implementation:

The GUI is implemented using **ipywidgets** and consists of buttons for different operations. Here’s a quick overview of the interactive elements:

- **Buttons**: Each action (such as displaying results, identifying underperforming students, etc.) is tied to a button that triggers specific event handlers.
- **Input Fields**: Allows the module leader to input the student’s research ID and select test names.
- **Grid Layout**: Buttons are organized in a **grid layout**, providing a clean interface.

---

## 🚀 Future Enhancements:
- **Student Data Export**: Allow the system to export results to a CSV or Excel file for offline analysis.
- **Real-time Updates**: Integrate real-time data analysis and tracking for more dynamic monitoring.
- **Advanced Analytics**: Add additional analytical features, such as trend analysis or predictions for student performance.
  
---

## 🏆 Why This Project Stands Out:
- 🔹 **Simplifies monitoring**: The system simplifies student performance tracking, making it easier for educators to analyze test results.
- 🔹 **Data-driven decision making**: Provides insights into underperforming and hardworking students, supporting data-driven educational decisions.
- 🔹 **Interactive GUI**: The GUI design ensures ease of use for module leaders and educators.
- 🔹 **Customizable**: Can be customized further with additional test data, performance criteria, or new metrics.

---

## 📧 Get in Touch:

If you have questions or need further assistance, feel free to reach out!


