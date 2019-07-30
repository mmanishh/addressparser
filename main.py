from addressparser import AddressParser

if __name__ == "__main__":
    #print(AddressParser("model/model_combined_9730").parse_address('Cibadak Kec. Astanaanyar Kota Bandung, Jawa Barat 40241 Jl. Jend. Sudirman No.198'))
    AddressParser().parse_csv(file_path='data/2018-01-03.csv',cols=['receiver_address','sender_address']).to_csv('parsed.csv',index=False)