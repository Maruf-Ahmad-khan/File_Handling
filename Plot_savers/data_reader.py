import pandas as pd

class DataReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_data(self):
        try:
            data = pd.read_csv(self.file_name)
            print("Data loaded successfully.")
            return data
        except FileNotFoundError:
            print("Error: File not found.")
        except pd.errors.ParserError:
            print("Error: File is corrupted or improperly formatted.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
