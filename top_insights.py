
import pandas as pd
import logging
logging.getLogger().setLevel(logging.INFO)

class Insights:
    def brand_null(self, df):
        logging.info("Products with brand name null assigned to unbranded")
        df["brand"].loc[df["brand"].str.len()==0] = "unbranded"
        return df

    def get_top_brands(self, df):
        logging.info("Gathering top 25 brands")
        brand = df.groupby("brand")["pid"].count()
        brand = brand.reset_index()
        brand = brand.rename(columns={"pid": "count_items"})
        top50 = brand.sort_values(by="count_items", ascending=False).head(25)
        return top50

    def get_top_categories(self, df):
        logging.info("Gathering top 4 categories")
        cat = df.groupby("category")["pid"].count()
        cat = cat.reset_index()
        cat = cat.rename(columns={"pid": "count_items"})
        top50cat = cat.sort_values(by="count_items", ascending=False)
        return top50cat

