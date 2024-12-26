import os

class PlotSaver:
    def __init__(self, directory):
        self.directory = directory

    def save_plot(self, plt, file_name):
        try:
            # Construct a valid file path
            if not os.path.exists(self.directory):
                os.makedirs(self.directory)  # Create the directory if it doesn't exist
            path = os.path.join(self.directory, file_name)
            plt.savefig(path)
            print(f"Plot saved at {path}")
        except Exception as e:
            print(f"An error occurred while saving the plot: {e}")
