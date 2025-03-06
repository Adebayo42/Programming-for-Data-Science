# Underperforming Student Functions

# A Python module which contains functions used to view test results of underperforming students.
# Student lowest formative test grade is highlighted in light yellow color
# It filter out student who have been largely inactive and not attempted a significant number of formative tests.
# (i.e students who have not attempted 2 or more tests)
# A student is classified as 'underperforming' if they score below 50 both in their summative online test and their Formative Mock Test


# Writen By: F315284
# Date: January, 2024

import pandas as pd
import DAFunction as func

# Function 1:# Style Function for minimum value
##############################################################################

def highlight_min(s):
    """
    Apply highlighting to the minimum value in a pandas Series.

    Args:
    - s: A pandas Series containing numerical values.

    Returns:
    - A list of styles to highlight the minimum value in the Series with a light yellow background.
      If a value matches the minimum value in the Series, it's highlighted; otherwise, it's not.
      
    """
    minimum_value = s.min()
    style = []
    for value in s:
        if value == minimum_value:
            style.append('background-color: lightyellow') # Highlight the minimum value
        else:
            style.append('') # No highlighting for other values
    return style



# SQL Statement to retrieve all students test score
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

# Function 2:# Underperforming students
##############################################################################


def underperforming():
    """
    Identify underperforming students based on test scores.

    Returns:
    - Displays underperforming students who scored less than 50 in both summative and mock tests,
      highlighting the lowest formative test grade among them in a pandas DataFrame.
    - If the function encounters a ValueError due to incorrect input data type, it prints an error message.
    
    """
    
    try:
        # Read from database
        test_results = func.read_database(SQLStr)
    
        # Fill NAs with zero
        func.fill_na(test_results)
    
        # Filter out inactive students
    
        # Count number of inactive student tests
        test_results['zero_test_cnt'] = test_results[test_results.columns[2:]].apply(lambda x: (x == 0).sum(),axis = 1)
    
        # Exclude the inactive students
        test_results = test_results[test_results['zero_test_cnt']<2].drop('zero_test_cnt', axis = 1)
    
    
        # Sorted test results    
        test_results.sort_values(by = 'summative_test', inplace = True )
    
        # Add lowest test grade column
        test_results['lowest_grade'] = test_results[test_results.columns[2:]].min(axis = 1)
    
        # underperforming_student
        #Underperforming students are students with summative test and formative mock test less than 50
        underperform = test_results[(test_results['summative_test'] < 50) & 
                                       (test_results['mock_test'] < 50) ]
        
        # Set 'research_id' as the new index and drop the existing index
        under_performing = underperform.set_index('research_id', drop=True)
    
    
        #Highlight the lowest formative test grade
        output = under_performing.style.apply(highlight_min, subset =under_performing.columns[1:6], axis = 1 )
        underperforming = output.format('{:.1f}')
        display(underperforming)
        
    except ValueError as err:
        print('You entered the wrong input data type. Only integers is acceptable')

#Function Testing
##############################################################################

if __name__=="__main__":
    underperforming()