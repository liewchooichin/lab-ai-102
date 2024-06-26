# Using SAS (Share Access Signature)

A shared access signature (SAS) is a URI that grants restricted access to an Azure Storage container. Use it when you want to grant access to storage account resources for a specific time range without sharing your storage account key.

## Blob SAS Token

sp=rwl&st=2024-06-26T05:19:48Z&se=2024-06-26T13:19:48Z&spr=https&sv=2022-11-02&sr=c&sig=CtANYX7UknvD7iymXNKfoki6BRw%2F%2BPjfNdcJ62B3B5o%3D

## Blob SAS URL

https://storagelcc002.blob.core.windows.net/heroforms?sp=rwl&st=2024-06-26T05:19:48Z&se=2024-06-26T13:19:48Z&spr=https&sv=2022-11-02&sr=c&sig=CtANYX7UknvD7iymXNKfoki6BRw%2F%2BPjfNdcJ62B3B5o%3D

## Sample of SAS from the portal

![shared access signature](./shared_token.PNG)

## To Use

That's all. Create the SAS from the portal. Then, use the code as normal. For example, the `custom-model.py` only needs to specify endpoint and service key. No need to specify any SAS url or token.