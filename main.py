from addressparser import AddressParser, AddressMatcher

if __name__ == "__main__":
    # print(AddressParser("model/model_combined_9730").parse_address('Cibadak Kec. Astanaanyar Kota Bandung, Jawa Barat 40241 Jl. Jend. Sudirman No.198'))
    # AddressParser().parse_csv(file_path='data/2018-01-03.csv',cols=[3]).to_csv('parsed.csv',index=False)
    query = {'name_company': 'menara bank danamon', 'house number': 'lt16', 'street': 'jl hr rasuna said', 'locality': 'kav c10', 'village': 'kuningan', 'city': 'jakarta selatan'}
    print((AddressMatcher(query).match_address(query)))
