# General function

#This Python module contains generalised functions that other modules like Test Results, Performance, Underperforming, and Hardworking Students rely upon to execute their specific tasks.

# Writen By: F315284
# Date: January, 2024

import pandas as pd
import sqlite3
import os
path = "../Data/"



# Function 0: # Create dictionary of file names in path
##############################################################################

def file_names(path):
    """
    Generate a dictionary mapping unique keys to file names based on the provided path.

    Parameters:
    - path (str): The path to the directory containing the files.

    Returns:
    dict: A mapping of keys to corresponding file names.

    Example:
    >>> file_names("/path/to/files")
    {'123': 'File123.txt', '456': 'File456.txt', '789': 'Other789.txt', 'nonFfile': 'nonFfile.txt'}
    
    """
    key, value = [], []
    for file in os.listdir(path):
        if file[0] == 'F':
            key.append(file[10:-4])
            value.append(file)
        else:
            key.append(file[0:-4])
            value.append(file)
    return dict(zip(key, value))
    


# Function 1: # Read File Function
##############################################################################


def read_file(file):
    """
    Reads a CSV file and returns its content as a pandas DataFrame.

    Args:
    - file (str): Name or path of the CSV file.

    Returns:
    - pandas.DataFrame: DataFrame containing the CSV data.

    Raises:
    - FileNotFoundError: If the specified file does not exist.
    - pd.errors.EmptyDataError: If the file is empty or contains no data.
    - pd.errors.ParserError: If an error occurs during CSV parsing.
    """
    try:
        dataframe = pd.read_csv(file)
        return dataframe
    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError) as e:
        print(f"Error reading CSV file: {e}")
        raise


# Function 2: Rename columns name
##############################################################################

def rename_column(dataframe):
    """
    Renames columns in a DataFrame based on a predefined mapping.

    Args:
    - dataframe (pandas.DataFrame): The DataFrame to rename columns.

    Returns:
    - pandas.DataFrame: DataFrame with renamed columns.
    
    """
    
    # new column name mappings
    column_mapping = {'research id': 'research_id',
                  'State'      : 'state',
                  'Started on' : 'started_on',
                  'Completed'  : 'completed',
                  'Time taken' : 'time_taken',
                  'Grade/600'  : 'grade',
                  'Grade/700'  : 'grade',
                  'Grade/600'  : 'grade',
                  'Grade/1000' : 'grade',
                  'Grade/10000': 'grade',
                  'Q 1 /100'   : 'q1',
                  'Q 1 /500'   : 'q1',
                  'Q 2 /100'   : 'q2',
                  'Q 2 /500'   : 'q2',
                  'Q 2 /300'   : 'q2',
                  'Q 3 /100'   : 'q3',
                  'Q 3 /600'   :'q3',
                  'Q 4 /100'   : 'q4',
                  'Q 4 /200'   : 'q4',
                  'Q 4 /700'   : 'q4',
                  'Q 5 /100'   : 'q5',
                  'Q 5 /400'   : 'q5',
                  'Q 5 /500'   : 'q5',
                  'Q 6 /100'   : 'q6',
                  'Q 6 /500'   : 'q6',
                  'Q 6 /400'   : 'q6',
                  'Q 7 /1500'  : 'q7',
                  'Q 7 /1000'  : 'q7',
                  'Q 8 /1500'  : 'q8',
                  'Q 8 /2000'  : 'q8',
                  'Q 9 /1500'  : 'q9',
                  'Q 9 /2000'  : 'q9',
                  'Q 10 /1000' : 'q10',
                  'Q 10 /2000' : 'q10',
                  'Q 11 /400'  : 'q11',
                  'Q 12 /500'  : 'q12',
                  'Q 13 /600'  : 'q13',
                  'Which of followings are true for you': 'programming_education',
                  'Which of the followings have you studied or had experience with':'programming_knowledge',
                  'What level programming knowledge do you have?' : 'programming_knowledge_level',
                  'Do you like programming': 'programming_interest',
                  'What do you think about sci-fi movies ?':'sci-fi_movies_interest',
                  'What do you think about learning to program  ?':'learning_programming_interest',
                  'Can you please specify the programming language you know which a':'programming_language_tools' 
                  
                 }
    # Rename column names based on mapping
    #dataframe = globals()[dataframes]
    k = []
    v = []
    for key, value in column_mapping.items():
        if key in dataframe.columns:
            k.append(key)
            v.append(value)
            col = dict(zip(k,v))        
    return dataframe.rename(columns = col, inplace = False)



# Function 3: function to replace na and '-'
##############################################################################

def remove_null(dataframe):
    """
    Replaces 'NAs' and '-' with zero in the DataFrame.

    Args:
    - dataframe (pandas.DataFrame): The DataFrame to process.

    Returns:
    - pandas.DataFrame: DataFrame with 'NAs' and '-' replaced by zero.
    
    """
    # assign the dataframe to a new dataframe
    new_dataframe = dataframe.copy()
    
    # Replace 'NAs' and '-' with zero
    new_dataframe.replace('-', 0, inplace = True)
    new_dataframe.fillna(0, inplace = True)
    
    # Return the modified dataframe
    return new_dataframe




# Function 4: Retaining highest Score
##############################################################################

def highest_score(dataframe):
    """
    Retains only the highest test score for each student in the DataFrame.

    Args:
    - dataframe (pandas.DataFrame): The DataFrame containing student test scores.

    Returns:
    - pandas.DataFrame: DataFrame retaining the highest test score for each student.
    
    """
    # Create a copy of the dataframe    
    new_dataframe = dataframe.copy()
     
        
    # update the datatype of grade column to float
    new_dataframe['grade'] = new_dataframe['grade'].astype(float)
    
    #find the index for the maximum grade for each student
    max_index = new_dataframe.groupby(['research_id'])['grade'].idxmax()
    
    # Return the rows with the maximum grade for each student
    return new_dataframe.loc[max_index]



# Function 5: Drop redundant columns
##############################################################################

def drop_columns(dataframe, col = ['state', 'time_taken']):
    """
    Drops specified columns from the DataFrame.

    Args:
    - dataframe (pandas.DataFrame): The DataFrame to process.
    - col (list): List of column names to drop.

    Returns:
    - pandas.DataFrame: DataFrame with specified columns dropped. 
    
    """
    # Drop specified columns
    return dataframe.drop(columns = col, inplace = False)




# Function 6: Update datatypes
##############################################################################

def update_datatype(dataframe):
    
    """
    Updates data types of selected columns in the DataFrame.

    Args:
    - dataframe (pandas.DataFrame): The DataFrame to process.

    Returns:
    - pandas.DataFrame: DataFrame with updated column data types. 
    
    """
    
    # Create copy of dataframe
    new_dataframe = dataframe.copy()
    
    # Select columns to convert their data types        
    cols_to_convert = new_dataframe.columns[3:]
    
    # Change the data types of selected columns to float
    new_dataframe[cols_to_convert] = new_dataframe[cols_to_convert].astype(float)
    
    return new_dataframe



# Function 7: Grade Standardization
##############################################################################

def grade_standardisation(dataframe):
    """
    Standardizes students' grades in the DataFrame.

    Args:
    - dataframe (pandas.DataFrame): The DataFrame containing student grades.

    Returns:
    - pandas.DataFrame: DataFrame with standardized student grades. 
    
    """
    
    # Create copy of dataframe
    new_dataframe = dataframe.copy()
  
       
    # Application of standardization to scores    
    # Identify the maximum value in selected columns
    max_score = new_dataframe.drop(['research_id', 'started_on', 'completed'], axis = 1).max()
    
    # standardized the columns
    for score in max_score.index:
        new_dataframe[score] = (new_dataframe[score]/max_score[score]) *100
        
    # Round off the scores to 1 decimal place
    new_dataframe[new_dataframe.columns[3:]] = new_dataframe[new_dataframe.columns[3:]].round(1)
    
    
    return new_dataframe 

# Function 8: Create SQLite3 Database
##############################################################################


# Create SQL Database
def create_db(db = 'CWDatabase.db' ):
    """
    Creates a SQLite3 database.

    Args:
    - db (str): The name of the database to be created.

    Returns:
    - None
    
    """
    
    # Create database connection
    conn = sqlite3.connect(path + db)
    conn.close()
      
    # Success message
    print(f'{db} database has been created successfully')
    

    
    
# Function 9: Create Tables Function
##############################################################################

def create_table(dataframe, table_name):
    """
    Creates a table in the SQLite3 database.

    Args:
    - dataframe (pandas.DataFrame): DataFrame to be created as a table in the database.
    - table_name (str): Name of the table to be created.

    Returns:
    - None
    
    """
        
   # mapping column data types 
    column_map = {
    'research_id' : 'INTEGER',
    'started_on'  : 'TEXT',
    'completed'   : 'TEXT',
    'grade'       : 'REAL',
    'q1'          : 'REAL',
    'q2'          : 'REAL',
    'q3'          : 'REAL',
    'q4'          : 'REAL',
    'q5'          : 'REAL',
    'q6'          : 'REAL',
    'q7'          : 'REAL',
    'q8'          : 'REAL',
    'q9'          : 'REAL',
    'q10'         : 'REAL',
    'q11'         : 'REAL',
    'q12'         : 'REAL',
    'q13'         : 'REAL',
    'programming_education'         : 'TEXT',
    'programming_knowledge'         : 'TEXT',
    'programming_knowledge_level'   : 'TEXT',
    'programming_interest'          : 'TEXT',
    'sci-fi_movies_interes'         : 'TEXT',
    'learning_programming_interest' : 'TEXT',
    'programming_language_tools'    : 'TEXT'    
    
}
         
   
    # Prepare dictionary of data types for specified columns
    k = []
    v = []
    for key, value in column_map.items():
        if key in dataframe.columns:
            k.append(key)
            v.append(value)
            data_types = dict(zip(k,v))
            
    # Connect to the database
    conn = sqlite3.connect(path + 'CWDatabase.db')
    
    # Write to the database
    dataframe.to_sql(table_name, conn, index = False, if_exists = 'replace', dtype = data_types)
    
    # Commit transaction and close connection
    conn.commit()
    conn.close()
    
    # Print success message
    print(f'{table_name} transfered to database successfully')

    
# Function 10: Read From Database Function
##############################################################################
    
def read_database(SQLStr):
    """
    Reads data from the SQLite3 database based on the provided SQL query.

    Args:
    - SQLStr (str): SQL query string to retrieve data from the database.

    Returns:
    - pandas.DataFrame: Dataframe containing the retrieved data.
    
    """
    
    # Connect to the database
    conn = sqlite3.connect(path + 'CWDatabase.db')
    
    # Read data from the database using the provided SQL query
    dataframe = pd.read_sql(SQLStr, conn)
    
    # Close connection
    conn.close()
    
    return dataframe

# Function 11: Fill NAs with zero Function
##############################################################################

def fill_na(dataframe):
    """
    Fills missing values (NaN) in the DataFrame with zeros.

    Args:
    - dataframe (pandas.DataFrame): DataFrame containing missing values to be filled.

    Returns:
    - pandas.DataFrame: DataFrame with missing values filled with zeros.
    
    """
    
    return dataframe.fillna(0, inplace = True)


# Function 12: Read Tables Function
##############################################################################

def read_tables(test_num):
    """
    Reads specific tables from the SQLite3 database based on the provided test number.

    Args:
    - test_num (str): String indicating the specific test table to be retrieved.
        "Test 1": Test_1, "Test 2": Test_2, "Test 3": Test_3, "Test 4": Test_4,
        "Mock Test": Mock_Test, "Summative Test": Summative_Test, "Student Rate": Student_Rating

    Returns:
    - pandas.DataFrame: DataFrame containing the requested table data.
    
    Note:
    If an invalid test number is provided, it prints a message listing the valid test numbers.
    
    """
    try:
        test_table = {
        "Test 1" : "Test_1",
        "Test 2" : "Test_2",
        "Test 3" : "Test_3",
        "Test 4" : "Test_4",
        "Mock Test" : "Mock_Test",
        "Summative Test" : "SumTest",
        "Student Rate" : "Student_Rating"
        }
        
        if test_num in test_table:
            SQLStr = f"SELECT * FROM {test_table[test_num]}"
            
        else:
            print("You entered the wrong test number\n\
        Try again with below correct test number\n\
        1) Test 1\n\
        2) Test 2\n\
        3) Test 3\n\
        4) Test 4\n\
        5) Mock Test\n\
        6) Summative Test\n\
        7) Student Rate")
            
        # Read table from database
        test_result = read_database(SQLStr)
        
        # Fill Na with Zero
        fill_na(test_result)
        
       
        return test_result
    
    # Exception handling
    except UnboundLocalError as e:
        print("")
        
    except ValueError as err:
        print('You entered the wrong input data type. Only integers is acceptable')
        
    except Exception as er:
        print(f'This error occured: {er}')
    

# Read Image for Menu wallpaper
def read_image(file):
    """
    Read the contents of an image file and return the content as a string.

    Args:
    - file (str): The name or path of the image file to be read.

    Returns:
    - bytes: The content of the image file as bytes.
    
    """
    try:
        with open(path + file, "rb") as file:
            image = file.read()
        return image
    except Exception as er:
        print(f'This error occured: {er}')

        



#Function Testing
##############################################################################

if __name__=="__main__":
#     # testing create table function 
   
    df1 = read_tables("Test 1")
    display(df1)
    
    
    
    
    
    
    
    
