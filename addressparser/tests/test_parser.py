from addressparser import AddressParser
import pandas as pd


def test_parse_address():
    '''
    tests the parse_address function of AddressParser
    :return:
    '''
    address = ['Cibadak Kec. Astanaanyar Kota Bandung, Jawa Barat 40241 Jl. Jend. Sudirman No.198','',1,1.23,None]
    parser = AddressParser()
    for addr in address:
        result = parser.parse_address(addr)
        assert isinstance(result, dict)


def test_parse_csv():
    '''
    tests the parse_csv function of AddressParser
    :return:
    '''
    result = AddressParser().parse_csv(file_path='data/2018-01-03.csv', cols=[3])
    assert isinstance(result, pd.DataFrame)
