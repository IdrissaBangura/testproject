
#import pandas

import pandas as pd

import logging
logging.getLogger().setLevel(logging.INFO)



class Dataset:

    def load_json(self, file_path):
        logging.info("loading dataset")
        with open(file_path, 'r') as f:
            df = pd.read_json(f)
            logging.info("Dataframe created")
        return df

