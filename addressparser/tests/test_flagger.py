from addressparser import AddressFlagger
import pandas as pd


def test_check_valid():
    address = {
        "street": "jl sambiroto",
        "house number": "no 12",
        "locality": "rt 01 rw 06",
        "name": "PARAGITA"
    }
    tags = ['street', 'house number', 'locality']

    assert AddressFlagger().check(address, tags) is True


def test_check_invalid():
    address = {
        "street": "jl sambiroto",
        "house number": "no 12",
        "locality": "rt 01 rw 06",
        "name": "PARAGITA"
    }
    tags = ['street', 'house number', 'loc']

    assert AddressFlagger().check(address, tags) is False


def test_check_csv():
    assert isinstance(AddressFlagger().parse_csv(file_path='data/2018-01-03.csv', cols=[3]), pd.DataFrame)
