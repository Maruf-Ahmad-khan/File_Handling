import matplotlib.pyplot as plt

class Plotcreator:
     
     @staticmethod
     
     def Create_bar_chart(data, x_col, y_col):
          plt.figure(figsize=(10, 6))
          plt.bar(data[x_col], data[y_col], color = 'darkblue')
          plt.xlabel(x_col)
          plt.ylabel(y_col)
          plt.title(f"{y_col} by {x_col}")
          plt.xticks(rotation = 45)
          plt.tight_layout()
          return plt