# CWPreprocessing Module

# It contains functions to clean the given test results of students and store them into the SQLite tables

# Writen By: F315284
# Date: January, 2024

import pandas as pd
import DAFunction as func

path = "../Data/TestResult/"

# Function 0: Fetch File names
##############################################################################

files = func.file_names(path)
tests = list(files.keys())
tests_1 = [item for item in tests if item != 'StudentRate']


# Function 1: Load files
##############################################################################

def load_files():
    """
    Loads CSV files and renames column names.

    Globals Created:
    - dfTest_1_V1: DataFrame for Formative_Test_1 after column renaming.
    - dfTest_2_V1: DataFrame for Formative_Test_2 after column renaming.
    - dfTest_3_V1: DataFrame for Formative_Test_3 after column renaming.
    - dfTest_4_V1: DataFrame for Formative_Test_4 after column renaming.
    - dfMock_Test_V1: DataFrame for Formative_Mock_Test after column renaming.
    - dfSumTest_V1: DataFrame for SumTest after column renaming.
    - dfStudentRate_V1: DataFrame for StudentRate after column renaming.
    
    """
    
    # Read CSV files    
    for key in files:
        globals()[f"df{key}"] = func.read_file(path + files[key])    
    
    # Create Global variables
    global dfTest_1_V1, dfTest_2_V1, dfTest_3_V1, dfTest_4_V1, dfMock_Test_V1, dfSumTest_V1, dfStudentRate_V1
    
    # Rename columns names
    for key in files:
        globals()[f"df{key}_V1"] = func.rename_column(globals()[f"df{key}"])    
    
    # Display success messages for each loaded file
    print(f"Data Preparation: Step 1")
    print("-----------------------------------")    
    for key in files:
        print(f"{files[key]} loaded successfully")
    print(f"\nStep 1 completed!!!\n")

        
# Function 2: Replace null values
##############################################################################        
        
def replace_null():
    """
    Replaces null values in the global DataFrames.

    Globals Created:
    - dfTest_1_V2: DataFrame for Formative_Test_1 after null value replacement.
    - dfTest_2_V2: DataFrame for Formative_Test_2 after null value replacement.
    - dfTest_3_V2: DataFrame for Formative_Test_3 after null value replacement.
    - dfTest_4_V2: DataFrame for Formative_Test_4 after null value replacement.
    - dfMock_Test_V2: DataFrame for Formative_Mock_Test after null value replacement.
    - dfSumTest_V2: DataFrame for SumTest after null value replacement.
    - dfStudentRate_V2: DataFrame for StudentRate after null value replacement.

    """
    # Create Global variables
    global dfTest_1_V2, dfTest_2_V2, dfTest_3_V2, dfTest_4_V2, dfMock_Test_V2, dfSumTest_V2, dfStudentRate_V2
    
    # Replace null values in DataFrames
    for test in tests:
        globals()[f"df{test}_V2"] = func.remove_null(globals()[f"df{test}_V1"])
    
    # Display success message
    print(f"Data Preparation: Step 2")
    print("-----------------------------------")
    print("Null values replaced successfully!")
    print(f"\nStep 2 completed!!!\n")
    
    
# Function 3: Retain Students hightest test scores
##############################################################################

def retain_highest_score():
    """
    Retains the highest test scores in the global DataFrames.

    Globals Created:
    - dfTest_1_V3: DataFrame for Formative_Test_1 with retained highest test scores.
    - dfTest_2_V3: DataFrame for Formative_Test_2 with retained highest test scores.
    - dfTest_3_V3: DataFrame for Formative_Test_3 with retained highest test scores.
    - dfTest_4_V3: DataFrame for Formative_Test_4 with retained highest test scores.
    - dfMock_Test_V3: DataFrame for Formative_Mock_Test with retained highest test scores.
    - dfSumTest_V3: DataFrame for SumTest with retained highest test scores.
    
    """
    # Create Global variables
    global dfTest_1_V3, dfTest_2_V3, dfTest_3_V3, dfTest_4_V3, dfMock_Test_V3, dfSumTest_V3

    # Retain highest test scores in DataFrames
    for test in tests_1:
        globals()[f"df{test}_V3"] = func.highest_score(globals()[f"df{test}_V2"])
    
    # Display success message
    print(f"Data Preparation: Step 3")
    print("-----------------------------------")
    print("Students hightest test score retained successfully!")
    print(f"\nStep 3 completed!!!\n")
    
    
# Function 4: Drop redundant columns
##############################################################################

def exclude_columns():
    """
    Excludes redundant columns in the global DataFrames.

    Globals Created:
    - dfCleanTest_1: DataFrame for Formative_Test_1 with excluded redundant columns.
    - dfCleanTest_2: DataFrame for Formative_Test_2 with excluded redundant columns.
    - dfCleanTest_3: DataFrame for Formative_Test_3 with excluded redundant columns.
    - dfCleanTest_4: DataFrame for Formative_Test_4 with excluded redundant columns.
    - dfCleanMock_Test: DataFrame for Formative_Mock_Test with excluded redundant columns.
    - dfCleanSumTest: DataFrame for SumTest with excluded redundant columns.
    
    """
    # Create Global variables
    global dfCleanTest_1, dfCleanTest_2, dfCleanTest_3, dfCleanTest_4, dfCleanMock_Test, dfCleanSumTest
    
    # Exclude redundant columns from DataFrames    
    for test in tests_1:
        globals()[f"dfClean{test}"] = func.drop_columns(globals()[f"df{test}_V3"])
    
    # Display success message
    print(f"Data Preparation: Step 4")
    print("-----------------------------------")
    print("Redundant columns excluded successfully!")
    print(f"\nStep 4 completed!!!\n")
    
    
# Function 5: Grades Standardisation
##############################################################################

def standardize_grade():
    
    """
    Standardizes grades across global DataFrames.

    Globals Created:
    - dfFormattedCleanTest_1: DataFrame for Formative_Test_1 with standardized grades.
    - dfFormattedCleanTest_2: DataFrame for Formative_Test_2 with standardized grades.
    - dfFormattedCleanTest_3: DataFrame for Formative_Test_3 with standardized grades.
    - dfFormattedCleanTest_4: DataFrame for Formative_Test_4 with standardized grades.
    - dfFormattedCleanMock_Test: DataFrame for Formative_Mock_Test with standardized grades.
    - dfFormattedCleanSumTest: DataFrame for SumTest with standardized grades.
    
    """
    # Create Global variables
    global dfFormattedCleanTest_1, dfFormattedCleanTest_2, dfFormattedCleanTest_3
    global dfFormattedCleanTest_4, dfFormattedCleanMock_Test, dfFormattedCleanSumTest
    
    
    #Update columns datatypes    
    for test in tests_1:
        globals()[f"dfClean{test}_V2"] = func.update_datatype(globals()[f"dfClean{test}"])
    
    # Standardize students grades
    for test in tests_1:
        globals()[f"dfFormattedClean{test}"] = func.grade_standardisation(globals()[f"dfClean{test}_V2"])
    
    # Display success message
    print(f"Data Preparation: Step 5")
    print("-----------------------------------")
    print("Grades standardisation completed successfully!")
    print(f"\nStep 5 completed!!!\n")
    
    
# Function 6: Create SQLite3 Database
##############################################################################

def create_database():
    """
    Creates a SQLite3 database using 'CWDatabase.db' file.
    """
    print(f"Data Preparation: Step 6")
    print("-----------------------------------")
    func.create_db()
    print(f"\nStep 6 completed!!!\n")
    
    
# Function 7: Create Tables
##############################################################################

def create_database_tables():
    """
    Creates tables in a SQLite3 database using global formatted dataframes.

    Tables created:
    - 'Test_1': Dataframe dfFormattedCleanTest_1
    - 'Test_2': Dataframe dfFormattedCleanTest_2
    - 'Test_3': Dataframe dfFormattedCleanTest_3
    - 'Test_4': Dataframe dfFormattedCleanTest_4
    - 'Mock_Test': Dataframe dfFormattedCleanMock_Test
    - 'SumTest': Dataframe dfFormattedCleanSumTest
    - 'Student_Rating': Dataframe dfStudentRate_V2
    
    """
    print(f"Data Preparation: Step 7")
    print("-----------------------------------")
    
    # write Tests to Database
    for test in tests_1:
        func.create_table(globals()[f"dfFormattedClean{test}"], f'{test}')
    
    # write StudentRate to Database
    func.create_table(dfStudentRate_V2, 'Student_Rating')

    print(f"\nStep 7 completed!!!\n")


# Function 8: Grouped Functions for data cleaning   
##############################################################################

def clean_data():
    """
    Perform a sequence of data cleaning operations:

    1. Load files into the data cleaning pipeline.
    2. Replace null or missing values with appropriate data.
    3. Retain the highest scores for analysis.
    4. Exclude unnecessary columns from the dataset.
    5. Standardize grade.
    6. Create a database structure to store the cleaned data.
    7. Create necessary database tables for the data.

    This function represents a sequence of steps involved in cleaning and preparing data 
    for analysis and storage, involving loading, replacing missing values, retaining 
    essential information, excluding unnecessary columns, standardizing metrics, 
    and organizing the cleaned data in a database-ready format.
    """
    load_files()
    replace_null()
    retain_highest_score()
    exclude_columns()
    standardize_grade()
    create_database()
    create_database_tables()
   
    
    
# Function 9: Display Test Tables
##############################################################################
    
def display_test(test_num):
    """
    Displays a specific test table based on the test number.

    Arg:
    - test_num: Test number to display from the database (integer).

    Output:
    - Displays the table corresponding to the provided test number.
    
    """
    test_table = func.read_tables(test_num)
    display(test_table)

# Function 10: import image
##############################################################################
image = func.read_image("myimage.jpg")
    
    
#Function Testing
##############################################################################

if __name__=="__main__":
    clean_data()
              
    
    
        
