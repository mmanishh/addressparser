import spacy
import os

class AddressParser:

    def __init__(self,model_path="model/model_combined_9730"):
        model_file_path = os.path.join(os.path.dirname(__file__), model_path)
        self.nlp = spacy.load(model_file_path)
    

    def parse_address(self,addr):
        model = self.nlp
        doc = model(addr.lower())
        result = {}
        # Find named entities, phrases and concepts
        for ent in doc.ents:
            start, end = ent.start_char, ent.end_char
            result[ent.label_] = addr[start:end]

        return result


