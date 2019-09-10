import pandas as pd
from pandas.errors import ParserError

from .addressparser import AddressParser
from .. import config


class AddressFlagger:

    def __init__(self):
        self.parser = AddressParser()

    def check(self, address, tags=None):
        if tags is None:
            if config.LANG == 'en':
                tags = ['street']
            else:
                tags = ['jalan']
        if isinstance(address, dict):
            return 'good' if all(elem in list(address.keys()) for elem in tags) else 'bad'
        else:
            raise TypeError("address param should be dictionary.")

    def parse_csv(self, file_path, cols, nrows=1000, seperator=','):
        """
        function to parse whole csv file for the specified cols and flagged good bad address
        params:
        nrows = no. of rows to load in dataframe
        file_path = file path of csv file
        cols = list of column index/col name to parse
        returns : Parsed DataFrame
        """
        try:
            df = pd.read_csv(file_path, nrows=nrows, sep=seperator)
        except ParserError:
            df = pd.read_csv(file_path, nrows=nrows, sep=';')
        for col in cols:
            if isinstance(col, int):
                new_col = df.columns[col] + '_parsed'
                df[new_col] = df.iloc[:, col].apply(self.parser.parse_address)
                col_flag = df.columns[col] + '_flag'
                df[col_flag] = df[new_col].apply(self.check)
            else:
                new_col = col + '_parsed'
                df[new_col] = df[col].apply(self.parser.parse_address)
                col_flag = col + '_flag'
                df[col_flag] = df[new_col].apply(self.check)

        return df
