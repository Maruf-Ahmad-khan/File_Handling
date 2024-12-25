class Read_Write():
     
     def __init__(self, filename):
          self.filename = filename
          
          
     def Write(self, content):
          with open(self.filename, 'w') as file:
               file.write(content)
               
               
     def Read(self):
          with open(self.filename, 'r') as file:
               return file.read()
          
if __name__ == "__main__":
     files = Read_Write("Demo.txt")
     files.Write("\nHello world i am writing in a file !")
     print("Contents in a file is : \n", files.Read())