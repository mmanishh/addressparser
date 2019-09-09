from addressparser import AddressFlagger


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
