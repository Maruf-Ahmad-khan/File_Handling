import pandas as pd
class FileHandlers:
     
     def __init__(self, filename):
          self.filename = filename
          
          
     def read_data(self):
          try:
               data = pd.read_csv(self.filename)
               print("data loaded successfully")
               return data
          
          except FileNotFoundError:
               print(f"Errors: File not found:")
               
          except Exception as e:
               print(f"An Error Occurred: {e}")