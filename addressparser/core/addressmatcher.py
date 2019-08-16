from elasticsearch import Elasticsearch
from elasticsearch import TransportError
from fuzzywuzzy import fuzz
from collections import defaultdict


def get_default_dict(queries_input):
    queries = defaultdict(str)
    for key in queries_input:
        queries[key] = queries_input[key]
    return queries


class AddressMatcher:

    def __init__(self, uri=None, index='address'):
        self.es = Elasticsearch()
        self.index = index

    def generate_params(self, query):
        # converts each key,value dict to list of dict
        queries_list = [{k: v} for k, v in list(query.items())]

        # convert to elastic search friendly query. In the form :[{"term": {"city": "depok"}}]
        # params = list(map(lambda x: {"term": x}, queries_list))
        params = list(map(lambda x: {"match": x}, queries_list))

        return params

    def search_es(self, query):

        params = self.generate_params(query)

        result = self.es.search(index=self.index, body={
            "from": 0, "size": 50,
            'query': {
                "bool": {
                    "must": params
                }
            }
        })

        '''
        previously used query
        {'query': {
            "bool": {
                "filter": [
                    {
                        "bool": {
                            "must": params
                        }
                    }
                ]
            }
        }}'''

        return result['hits']['hits']

    def compute_score(self, search_results, queries):
        scores = []
        # iterating search results
        for i, result in enumerate(search_results):

            source = result['_source']
            score = 0
            for key in source:
                score += fuzz.ratio(source[key], queries[key])
            source['score'] = score/len(source)
            scores.append(source)

        return scores

    def match_address(self, query):
        # converting to default dict
        query = get_default_dict(query)
        results = self.search_es(query)
        scores = self.compute_score(results, query)

        return scores
