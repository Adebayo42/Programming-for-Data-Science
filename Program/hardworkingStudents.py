# Hard Working Students Function

# A Python module which contains functions used to list hardworking students. A student is classified as 'hardworking' if their summative online test score exceeds 60, and their self-ratings is categorised as either “Below Beginner” or “Beginner”

# Writen By: F315284
# Date: January, 2024

import pandas as pd
import DAFunction as func

# Assign SQL statement to an object
##############################################################################

# SQL Statement retrieves students' research IDs, summative test scores, and their programming knowledge levels

SQLStr_2 = """SELECT A.RESEARCH_ID, A.GRADE AS 'summative_test', programming_knowledge_level FROM SumTest AS A
LEFT JOIN (SELECT RESEARCH_ID, programming_knowledge_level FROM Student_Rating) AS B 
ON A.RESEARCH_ID = B.RESEARCH_ID
WHERE A.GRADE > 60 AND B.PROGRAMMING_KNOWLEDGE_LEVEL IN ('Beginner', 'Below beginner')"""


# Function 1:# Hardworking_Students
##############################################################################

def hardworking():
    """
    Retrieves and displays information for hardworking students based on their summative test results.

    Output:
    - Displays information about the top-performing students based on the summative test results.
    
    """
    
    try:
    
        # Read from database
        test_results = func.read_database(SQLStr_2)
    
        # Fill NAs with zero
        func.fill_na(test_results)
    
        # Sorted test results    
        test_results.sort_values(by = 'summative_test', ascending = False, inplace = True )
        
        # Set 'research_id' as the new index and drop the existing index
        hardworking_sudent = test_results.set_index('research_id', drop=True)    

        # hardworking_student
          
        display(hardworking_sudent)
        
    except ValueError as err:
        print('You entered the wrong input data type. Only integers is acceptable')
        
#Function Testing
##############################################################################

if __name__=="__main__":
    hardworking()