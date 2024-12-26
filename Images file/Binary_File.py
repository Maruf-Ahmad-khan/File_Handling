class Binary:
     
     def __init__(self, source_file, destination_file):
          
          self.source_file = source_file
          self.destination_file = destination_file
          
     def Copy_file(self):
          
          with open(self.source_file, 'rb') as rf:
               with open(self.destination_file, 'wb') as wf:
                    wf.write(rf.read())
                    
                    
     def Copyer_Files(self):
          
          with open(self.source_file, 'rb') as rf:
               with open(self.destination_file, 'wb') as wf:
                    wf.write(rf.read())
                    
if __name__ == "__main__":
     file_copier = Binary("Images file/download.png", "Images file/download_copy.png")
     file_copier.Copy_file()
     ans = Binary( "Images file/office_pic.png", "Images file/office_pic_copy.png" )
     file_copier.Copyer_Files()
     