# studentPerformance functions

# Python module which contains functions used to ask for student ID and the test number to determines a student's performance on each test question. Both the student's relative and absolute performances is calculated and suitably visualised for each question.

# Writen By: F315284
# Date: January, 2024

import pandas as pd
import DAFunction as func
import matplotlib.pyplot as plt


# Function 1: # Relative grade function
##############################################################################


def relative_grade(dataframe):
    """
    Calculates the relative grades for each test question based on the provided dataframe.

    Args:
    - dataframe: DataFrame containing test scores for each student and each test question.

    Returns:
    - DataFrame: DataFrame with relative grades computed by subtracting the average score for each test question
                 from individual test scores. The columns represent each test question's relative grade.
    
    """
        
    # Create new dataframe
    new_dataframe = dataframe.copy()
    
    # Create a new dataframe for ralative grade
    relative_dataframe = new_dataframe.drop(new_dataframe.columns[3:], axis = 1)
    
    # Average score for each test questions
    avg_grade = new_dataframe.drop(['research_id', 'started_on', 'completed'], axis = 1).mean().round(1)
    
    # Create Relative grade
    for cols in new_dataframe.columns[3:]:
        relative_dataframe[f'{cols}'] = new_dataframe[cols] - avg_grade[cols]
    
    return relative_dataframe

# Function 2: # Student Performance
##############################################################################


def student_performance(research_id, test_num):
    """
    Displays the absolute and relative test grades for a specific student based on their research_id
    and test number.

    Args:
    - research_id: Unique identifier for a student.
    - test_num: Test name to retrieve grades from the database.

    Displays:
    - Absolute grade results and relative grade results as separate dataframes for the given student.
    - Bar chart representations for both absolute and relative grades. The bar colors indicate positive (dark green)
      and negative (dark red) relative grades for each test question.
    
    """
    
    try:
        
        # Reade table from database
        clean_test_Results = func.read_tables(test_num)
        
        # Add relative grade columns
        formated_test_result = relative_grade(clean_test_Results)
    
        # Display test results for the inputed research_id
        if research_id in clean_test_Results['research_id'].values:
            
            # Retrieve student absolute test grades
            absolute = clean_test_Results.loc[clean_test_Results['research_id'] == research_id]
            formatted_absolute = absolute.drop(['research_id', 'started_on', 'completed'], axis = 1).T
            formatted_absolute.rename(columns= {formatted_absolute.columns[0] : 'absolute'}, inplace = True)
            
                    
            # Retrieve student relative test grades
            relative = formated_test_result.loc[formated_test_result['research_id'] == research_id]
            formatted_relative = relative.drop(['research_id', 'started_on', 'completed'], axis = 1).T
            formatted_relative.rename(columns= {formatted_relative.columns[0] : 'relative'}, inplace = True)

            # Display Concantenated dataframe
            concantenatted_df = pd.concat([formatted_absolute, formatted_relative], axis = 1)        
            display(concantenatted_df)          


            #Plot the grades        
            # Set subplots       
            fig, axs = plt.subplots(1, 2, figsize=(12, 6))
        
            # Plot Bar Chart for absolute         
            formatted_absolute.plot(kind = 'bar', color ='darkblue', legend = False, ax=axs[0])
            axs[0].set_title('Absolute Grade', fontsize=20, color='darkblue', fontweight='bold', fontname='fantasy')
            axs[0].tick_params(axis='both', which='major', labelsize=14)
                       
        
            # Plotting the bar chart for relative grade with conditional colors      
            bars_formatted_relative = formatted_relative.plot(kind='bar',  legend=False, ax=axs[1])
            axs[1].set_title('Relative Grade', fontsize=20, color='darkgreen', fontweight='bold', fontname='fantasy')
            axs[1].tick_params(axis='both', which='major', labelsize=14)
                    
            # Color each bar individually based on its value
            for bar, values in zip(bars_formatted_relative.patches, formatted_relative.values):
                if values > 0:
                    bar.set_color('darkgreen')
                else:
                    bar.set_color('darkred')
      
           # Show Plot
            plt.tight_layout()
            plt.show()        
        
        else:
            print('You entered the wrong student_id.\nPlease try again with the correct student_id.')
            
    except AttributeError as e:
        print('')
        
    except ValueError as err:
        print('You entered the wrong input data type. Only integers is acceptable')
        
    except Exception as er:
        print(f'This error occured: {er}')
        

#Function Testing
##############################################################################

if __name__=="__main__":
    student_performance(50, 'Summative Test')
          