
#import pandas

import pandas as pd

import file_loader as fl
import top_insights as ti
import plot as plt
import logging
logging.basicConfig(filename="mylogs.log")

if __name__ == '__main__':

    # 1. Load dataset as dataframe

    loader = fl.Dataset()
    df = loader.load_json(r"C:\Users\USER\PycharmProjects\test1\flipkart_fashion_products_dataset.json")

    # 2. Get toplevel insights for the most popular brand & categories

    topinsights = ti.Insights()
    df = topinsights.brand_null(df)

    topbrands = topinsights.get_top_brands(df)
    print(topbrands.head())

    topcat=topinsights.get_top_categories(df)
    print(topcat.head())


    # 3. plot and save graphs

    plot = plt.Plot()
    plot.plot_pie_chart(topbrands.head(10))



