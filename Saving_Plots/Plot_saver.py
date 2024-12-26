class Plotsaver:
     
     @staticmethod
     
     def save_plot(plt_object, filename):
          try:
               plt_object.savefig(filename)
               print(f"plot save as filename {filename}")
               
          except Exception as e:
               print(f"Error saving plot: {e}")
               