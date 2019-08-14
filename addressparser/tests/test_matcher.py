from addressparser import AddressMatcher


def test_get_params():
    es = AddressMatcher()

    query = {'city': 'depok', 'village': 'cimanggis', 'locality': 'rt'}

    dummies = [{
        "term": {
            "city": "depok"
        }
    },
        {
            "term": {
                "village": "cimanggis"
            }
        },
        {
            "term": {
                "locality": "rt"
            }
        }]

    assert dummies == es.generate_params(query)
