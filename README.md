# Module for Indonesian Address Parser

It is based on spacy NER model, you can find the models under the root/core/model dir.

--------

### Directory Structure

- /addressparser
   - /core : contains core code of the module
     - /model : contains all models used
  	- /tests : contains test files





## Examples

#### Parse the String address

```python
from addressparser import AddressParser

parser = AddressParser(PATH_TO_MODEL)

address = 'Cibadak Kec. Astanaanyar Kota Bandung, Jawa Barat 40241 Jl. Jend. Sudirman No.198'

print(parser.parse_address(address))
```



Output:

```json
{'village': 'Cibadak', 'district': 'Kec. Astanaanyar', 'city': 'Kota Bandung', 'province': 'Jawa Barat', 'postal code': '40241', 'street': 'Jl. Jend. Sudirman', 'house number': 'No.198'}
```



#### Parse the CSV File

```
from addressparser import AddressParser

parser = AddressParser(PATH_TO_MODEL)

parsed_df = parser.parse_csv(file_path='data/2018-01-03.csv',cols=[3])
```





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