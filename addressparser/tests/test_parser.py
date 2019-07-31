from addressparser import AddressParser
import pandas as pd


def test_parse_address():
    '''
    tests the parse_address function of AddressParser
    :return:
    '''
    address = 'Cibadak Kec. Astanaanyar Kota Bandung, Jawa Barat 40241 Jl. Jend. Sudirman No.198'
    parser = AddressParser()
    result = parser.parse_address(address)
    assert isinstance(result, dict)


def test_parse_csv():
    '''
    tests the parse_csv function of AddressParser
    :return:
    '''
    result = AddressParser().parse_csv(file_path='data/2018-01-03.csv', cols=[3])
    assert isinstance(result, pd.DataFrame)
