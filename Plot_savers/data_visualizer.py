import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_payout_distribution(self):
        if self.data is None or self.data.empty:
            print("No data available for visualization.")
            return None  # Handle cases where data is missing or empty

        # Summarize data
        summed_data = self.data.groupby('Campaign_Name')['Payout'].sum().reset_index()
        summed_data.columns = ['Campaign_Name', 'Payout']
        sorted_data = summed_data.sort_values(by='Payout', ascending=False)

        # Create the plot
        fig, ax = plt.subplots(figsize=(25, 15))
        sns.barplot(data=sorted_data, x='Campaign_Name', y='Payout', order=sorted_data['Campaign_Name'], ax=ax)

        # Add data labels on the bars
        for bar, total in zip(ax.patches, sorted_data['Payout']):
            ax.text(
                bar.get_x() + bar.get_width() / 2,  
                bar.get_height() + 0.5,            
                f'{total:.2f}',                    
                ha='center', va='bottom', fontsize=18, weight='bold'  
            )

        # Customize the plot
        ax.set_xticklabels(ax.get_xticklabels(), rotation=85, ha='right', fontsize=15, weight='bold')
        ax.set_yticklabels(ax.get_yticks(), fontsize=15, weight='bold')
        ax.set_title('Total Payout($) by Campaign Names', fontsize=15, weight='bold')
        ax.set_xlabel('Campaign Name', fontsize=15, weight='bold')
        ax.set_ylabel('Total Sales', fontsize=15, weight='bold')
        plt.tight_layout()

        return fig, ax  # Ensure fig and ax are returned
