import matplotlib.pyplot as plt
import logging
logging.getLogger().setLevel(logging.INFO)


class Plot:

    def plot_pie_chart(self, insight_df, graph_name):
        logging.info("Generating Pie plot")
        plt.figure(figsize= (15,7))
        if graph_name.lower() in "brand":
            col_name = "brand"
            title_type = "Top brands"

        elif graph_name.lower() in "category":
            col_name = "category"
            title_type = "Top categories"
        else:

            logging.info("Unknown field passed")
            exit()

        plt.pie(insight_df["count_items"], labels=insight_df[col_name], autopct="%1.1f%%", startangle=180)
        plt.title(title_type)
        plt.savefig(f"{graph_name}.png");
        plt.show();
        logging.info("Saving Pie plot")
        return


