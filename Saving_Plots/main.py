from file_handlers import FileHandlers
from Plot_creator import Plotcreator
from Plot_saver import Plotsaver

file_handler = FileHandlers(r"C:\Users\mk744\Downloads\Partnerize dataset.csv")
data = file_handler.read_data()


if data is not None:
     plt_object = Plotcreator.Create_bar_chart(data, "Campaign_Name", "Payout")
     Plotsaver.save_plot(plt_object, "campaign_payout_chart.png")