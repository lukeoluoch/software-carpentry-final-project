class Log_Entry:
    '''
    This class carries creates a Log Entry object.
    
    It has attributes for a user's nutritional data, the date, their food entries, and their workout entries
   
    '''

    def __init__(self, user_data, date, food_entries, workout_entries): #has to be reversed as we view the coordinate system differently to how numpy does
        """This function initializes the an instance of the Log_Entry Object
        Args:
            user_data (list): The User's Caloric and Macronutritional Data
            date (str): The Date
            food_entries (list): The User's Food Entries on that date
            workout_entries (list): The User's workout entries in that date
        """
        self.user_data = user_data
        self.date = date
        self.food_entries = food_entries
        self.workout_entries = workout_entries
        


    def to_String(self):
        """This function converts all its information into a string, perfect for writing onto text files for storage

        Returns:
            string: A string representation of the Log_Entry attributes
        """
        string = str(self.date)  + ":" + str(self.user_data) +":" + str(self.food_entries) + ":" + str(self.workout_entries)
        return string


