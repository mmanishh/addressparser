import spacy
import os
import pandas as pd


class AddressParser:

    def __init__(self, model_path="model/model_combined_9730"):
        model_file_path = os.path.join(os.path.dirname(__file__), model_path)
        self.nlp = spacy.load(model_file_path)

    def parse_address(self, addr):
        """
        Function to parse single string address
        Params:
        addr = string address to parse
        Returns: parsed address in json format
        """
        if addr is None:
            return {'other': 'null'}
        model = self.nlp
        addr = str(addr)
        doc = model(str(addr).lower())
        result = {}
        # Find named entities, phrases and concepts
        for ent in doc.ents:
            start, end = ent.start_char, ent.end_char
            result[ent.label_] = addr[start:end]

        return result

    def parse_csv(self, file_path, cols, nrows=1000, seperator=';'):
        """
        function to parse whole csv file for the specified cols
        params:
        nrows = no. of rows to load in dataframe
        file_path = file path of csv file
        cols = list of column index/col name to parse  
        returns : Parsed DataFrame
        """
        df = pd.read_csv(file_path, nrows=nrows, sep=seperator)

        for col in cols:
            if isinstance(col, int):
                new_col = colname = df.columns[col] + '_parsed'
                df[new_col] = df.iloc[:, col].apply(self.parse_address)
            else:
                new_col = colname = col + '_parsed'
                df[new_col] = df[col].apply(self.parse_address)

        return df
