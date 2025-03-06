# Test Result Functions

# it is a Python module which contains functions used to ask for student ID and display all test results of the student

# Writen By: F315284
# Date: January, 2024

import pandas as pd
import DAFunction as func
import matplotlib.pyplot as plt

# SQL Statement to retrieve all students' test scores from different test tables and combine them
##############################################################################

SQLStr = """SELECT A.RESEARCH_ID, A.GRADE AS 'summative_test', mock_test, test_1, test_2, test_3, test_4 FROM SumTest AS A
LEFT JOIN (SELECT RESEARCH_ID, GRADE AS 'mock_test' FROM Mock_Test) AS B 
ON A.RESEARCH_ID = B.RESEARCH_ID
LEFT JOIN (SELECT RESEARCH_ID, GRADE AS 'test_1' FROM Test_1) AS C 
ON A.RESEARCH_ID = C.RESEARCH_ID
LEFT JOIN (SELECT RESEARCH_ID, GRADE AS 'test_2' FROM Test_2) AS D 
ON A.RESEARCH_ID = D.RESEARCH_ID
LEFT JOIN (SELECT RESEARCH_ID, GRADE AS 'test_3' FROM Test_3) AS E 
ON A.RESEARCH_ID = E.RESEARCH_ID
LEFT JOIN (SELECT RESEARCH_ID, GRADE AS 'test_4' FROM Test_4) AS F 
ON A.RESEARCH_ID = F.RESEARCH_ID"""



# Function 1: # Test Results
##############################################################################

def test_result(research_id):    
    """
    Displays the test results and a bar chart representation of scores for a specific student based on their research_id.

    Args:
    - research_id: Unique identifier for a student.

    Displays:
    - Test results as a dataframe for the given student.
    - Bar chart representation of test scores for the student.
    """
    
    # Read from the database
    test_Results = func.read_database(SQLStr)        
       
    # Fill NAs with zero
    func.fill_na(test_Results)
    
    # Display test results for the inputed research_id
    if research_id in test_Results['research_id'].values:
        output = test_Results.loc[test_Results['research_id'] == research_id,
                                  test_Results.columns[1:]]
                
        
        # Set subplots       
        fig, axs = plt.subplots(2, 1, figsize=(14, 8))
        
        # Plot Table
        plt.subplot(2, 1, 2)
        plt.axis('off')  # Hide axes for DataFrame display
        table = plt.table(cellText = output.values,
                          colLabels = output.columns,
                          loc='center',
                          cellLoc='center')
        
        # Set table font size and cell heights
        table.auto_set_font_size(False)
        table.set_fontsize(18)
        table.scale(1, 4.5)
        
        # Plot Bar Chart
        (output.loc[:, output.columns != 'research_id'].T
         .plot(kind = 'bar', color = 'darkblue', legend = False, ax = axs[0]))
        
        # Set plot title and ticks parameters
        axs[0].set_title('Student Test Scores',
                         fontsize = 26,
                         color ='darkgreen',
                         fontweight = 'bold',
                         fontname ='fantasy')
        
        axs[0].tick_params(axis='both', which='major', labelsize=14)  
        
        # Show plot
        plt.tight_layout()
        plt.show()      
           
    
    else:
        print('You entered the wrong student_id.\nPlease try again with the correct student_id.')
        
#Function Testing
##############################################################################

if __name__=="__main__":
    test_result(1)
          
    
        