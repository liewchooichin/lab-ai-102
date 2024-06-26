from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

import os
# Store connection information
endpoint = os.getenv("AI_SERVICE_ENDPOINT")
key = os.getenv("AI_SERVICE_KEY")

# My notes: Must add this to the url: ?raw=true
#fileUri = "https://github.com/MicrosoftLearning/mslearn-ai-document-intelligence/blob/main/Labfiles/01-prebuild-models/sample-invoice/sample-invoice.pdf?raw=true"
fileUri = "https://github.com/liewchooichin/lab-ai-102/blob/main/mslearn-ai-doc/grocery_receipt.pdf?raw=true"
fileLocale = "en-US"
fileModelId = "prebuilt-invoice"


print(f"\nConnecting to Forms Recognizer at: {endpoint}")
print(f"Analyzing invoice at: {fileUri}")

# Create the client
credential=AzureKeyCredential(key)
document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=credential
 )

# Analyse the invoice
task = document_analysis_client.begin_analyze_document_from_url(
     fileModelId, fileUri, locale=fileLocale
 )

# Display invoice information to the user
receipts = task.result()
for idx, receipt in enumerate(receipts.documents):

    vendor_name = receipt.fields.get("VendorName")
    if vendor_name:
        print(f"\nVendor Name: {vendor_name.value}, with confidence {vendor_name.confidence}.")

customer_name = receipt.fields.get("CustomerName")
if customer_name:
    print(f"Customer Name: '{customer_name.value}, with confidence {customer_name.confidence}.")

invoice_total = receipt.fields.get("InvoiceTotal")
if invoice_total:
    print(f"Invoice Total: '{invoice_total.value.symbol}{invoice_total.value.amount}, with confidence {invoice_total.confidence}.")

    if receipt.fields.get("Items"):
        print("Receipt items:")
        for idx, item in enumerate(receipt.fields.get("Items").value):
            print("...Item #{}".format(idx + 1))
            item_description = item.value.get("Description")
            if item_description:
                print(
                    "......Item Description: {} has confidence: {}".format(
                        item_description.value, item_description.confidence
                    )
                )
            item_quantity = item.value.get("Quantity")
            if item_quantity:
                print(
                    "......Item Quantity: {} has confidence: {}".format(
                        item_quantity.value, item_quantity.confidence
                    )
                )
            item_price = item.value.get("Price")
            if item_price:
                print(
                    "......Individual Item Price: {} has confidence: {}".format(
                        item_price.value, item_price.confidence
                    )
                )
            item_total_price = item.value.get("TotalPrice")
            if item_total_price:
                print(
                    "......Total Item Price: {} has confidence: {}".format(
                        item_total_price.value, item_total_price.confidence
                    )
                )
    subtotal = receipt.fields.get("Subtotal")
    if subtotal:
        print(
            "Subtotal: {} has confidence: {}".format(
                subtotal.value, subtotal.confidence
            )
        )
    tax = receipt.fields.get("TotalTax")
    if tax:
        print("Tax: {} has confidence: {}".format(tax.value, tax.confidence))
    tip = receipt.fields.get("Tip")
    if tip:
        print("Tip: {} has confidence: {}".format(tip.value, tip.confidence))
    total = receipt.fields.get("Total")
    if total:
        print("Total: {} has confidence: {}".format(total.value, total.confidence))
    print("--------------------------------------")

print("\nAnalysis complete.\n")