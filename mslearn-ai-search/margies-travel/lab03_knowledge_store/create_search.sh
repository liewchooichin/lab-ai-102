#!/bin/sh

echo Creating data source, skillset, index and indexer

# In the curl command line below, the @data_source.json is the 
# prefix for json file.

# Set values for your Search service
url=$SEARCH_ENDPOINT
admin_key=$SEARCH_ADMIN_KEY

echo -----
#echo Creating the data source...
# margies-data has already been created in my storage container.
# The margies-data container was created from the previous lab exercise.
#curl -X POST $url/datasources?api-version=2020-06-30 -H "Content-Type: application/json" -H "api-key: $admin_key" -d @data_source.json

echo -----
echo Creating the skillset...
curl -X PUT $url/skillsets/margies-knowledge-skillset?api-version=2020-06-30 -H "Content-Type: application/json" -H "api-key: $admin_key" -d @skillset.json

echo -----
echo Creating the index...
curl -X PUT $url/indexes/margies-knowledge-index?api-version=2020-06-30 -H "Content-Type: application/json" -H "api-key: $admin_key" -d @index.json

# wait
timeout 3 echo wait

echo -----
echo Creating the indexer...
curl -X PUT $url/indexers/margies-knowledge-indexer?api-version=2020-06-30 -H "Content-Type: application/json" -H "api-key: $admin_key" -d @indexer.json