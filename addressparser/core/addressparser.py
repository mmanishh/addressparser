import spacy
import os
import pandas as pd
from pandas.errors import ParserError
from .. import config


class AddressParser:

    def __init__(self, model_path="model/model_combined_9730"):
        model_file_path = os.path.join(os.path.dirname(__file__), model_path)
        self.nlp = spacy.load(model_file_path)

    def parse_address(self, addr):
        """
        Function to parse single string address
        Params:
        addr = string address to parse
        lang = language for tag, id : indonesian
        Returns: parsed address in json format
        """
        if addr is None:
            return {'other': 'null'}
        model = self.nlp
        addr = str(addr)
        doc = model(str(addr).lower())
        result = {}

        # change the tag name according to lang
        if config.LANG == 'id':
            # Find named entities, phrases and concepts
            for ent in doc.ents:
                start, end = ent.start_char, ent.end_char
                if ent.label_ == 'street':
                    result['jalan'] = addr[start:end]
                elif ent.label_ == 'other':
                    result['lainnya'] = addr[start:end]
                elif ent.label_ == 'house number':
                    result['nomor_rumah'] = addr[start:end]
                elif ent.label_ == 'locality':
                    result['lokalitas'] = addr[start:end]
                elif ent.label_ == 'name_company':
                    result['nama_perusahaan'] = addr[start:end]
                elif ent.label_ == 'postal code':
                    result['kode_pos'] = addr[start:end]
                elif ent.label_ == 'village':
                    result['desa'] = addr[start:end]
                elif ent.label_ == 'district':
                    result['distrik'] = addr[start:end]
                elif ent.label_ == 'city':
                    result['kota'] = addr[start:end]
                elif ent.label_ == 'regency':
                    result['kabupaten'] = addr[start:end]
                elif ent.label_ == 'province':
                    result['provinsi'] = addr[start:end]
                else:
                    result[ent.label_] = addr[start:end]
        else:
            for ent in doc.ents:
                start, end = ent.start_char, ent.end_char
                result[ent.label_] = addr[start:end]

        return result

    def parse_csv(self, file_path, cols, nrows=1000, seperator=','):
        """
        function to parse whole csv file for the specified cols
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
                df[new_col] = df.iloc[:, col].apply(self.parse_address)
            else:
                new_col = col + '_parsed'
                df[new_col] = df[col].apply(self.parse_address)

        return df
