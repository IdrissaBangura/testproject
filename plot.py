import matplotlib.pyplot as plt
import logging
logging.getLogger().setLevel(logging.INFO)


class Plot:

    def plot_pie_chart(self, insight_df):
        logging.info("Generating Pie plot")
        plt.figure(figsize= (15,7))
        plt.pie(insight_df["count_items"], labels=insight_df["brand"], autopct="%1.1f%%", startangle=180)
        plt.title("Top 25 brands")
        plt.show();
        return


