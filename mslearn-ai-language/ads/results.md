# Results of custom-entities.py

A project was created in Azure Language Studio.

Custom Named Entities Recognition service is chosen.

```
python custom-entities.py > ads/results.md

test1.txt
	Entity 'Bluetooth earbuds' has category 'ItemForSale' with confidence score of '0.98'
	Entity '$100' has category 'Price' with confidence score of '0.94'
	Entity 'Sacramento, CA' has category 'Location' with confidence score of '1.0'

test2.txt
	Entity 'Dog harness' has category 'ItemForSale' with confidence score of '1.0'
	Entity '$20' has category 'Price' with confidence score of '0.99'
	Entity 'Tucson, AZ' has category 'Location' with confidence score of '1.0'
```