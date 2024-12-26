from data_reader import DataReader
from data_visualizer import DataVisualizer
from plot_savers import PlotSaver

# Load data
reader = DataReader(r"C:\Users\mk744\Downloads\Partnerize dataset.csv")
data = reader.load_data()

# Visualize data and save the plot
if data is not None:  # Ensure data is loaded successfully
    visualizer = DataVisualizer(data)
    result = visualizer.plot_payout_distribution()  # Get the result

    if result is not None:  # Check if the visualization was successful
        fig, ax = result  # Unpack fig and ax
        plot_saver = PlotSaver("plots")
        plot_saver.save_plot(fig, "payout_distribution_plot.png")
    else:
        print("Failed to create the plot.")
else:
    print("Failed to load data.")




