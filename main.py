from addressparser import AddressParser, AddressMatcher

if __name__ == "__main__":
    print(AddressParser("model/model_combined_9730").parse_address('Cibadak Kec. Astanaanyar Kota Bandung, Jawa Barat 40241 Jl. Jend. Sudirman No.198'))
    # AddressParser().parse_csv(file_path='data/2018-01-03.csv',cols=[3]).to_csv('parsed.csv',index=False)
    # query = {'city': 'jakarta'}
    # query2 ={'locality': 'kcp sunter nirwana', 'street': 'jl bismaraya', 'house number': 'blok a 5 no', 'city': 'jakarta utara'}
    #
    # query3 ={'street': 'jl bismaraya', 'city': 'jakarta utara'}
    #
    # results = AddressMatcher(query).match_address(query3)
    # print("Total results:",len(results))
    # for r in results:
    #     print(r)
