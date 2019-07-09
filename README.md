# Module for Indonesian Address Parser

It is based on spacy NER model, you can find the models under the root/model dir.

--------

## Examples



`parser = AddressParser(PATH_TO_MODEL)`

`address = 'Cibadak Kec. Astanaanyar Kota Bandung, Jawa Barat 40241 Jl. Jend. Sudirman No.198'`

`print(address.parse_address(address))`

Output:

`{'village': 'Cibadak', 'district': 'Kec. Astanaanyar', 'city': 'Kota Bandung', 'province': 'Jawa Barat', 'postal code': '40241', 'street': 'Jl. Jend. Sudirman', 'house number': 'No.198'}`



### Scope of Address parser

- street
- house number
- locality
- village
- district
- city
- postal code
- province
- other
- regency
- name_company