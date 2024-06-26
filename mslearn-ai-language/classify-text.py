from dotenv import load_dotenv
import os

# Import namespaces
# import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def main():
    try:
        # Get Configuration Settings
        #load_dotenv()
        ai_endpoint = os.getenv('LANG_ENDPOINT')
        ai_key = os.getenv('LANG_KEY')
        #PROJECT = "ClassifyLab"
        #DEPLOYMENT = "articles"
        project_name = "ClassifyLab" #os.getenv('PROJECT')
        deployment_name = "articles" #os.getenv('DEPLOYMENT')

        # Create client using endpoint and key
        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        ai_client = TextAnalyticsClient(endpoint=ai_endpoint, credential=credential)

        # Read each text file in the articles folder
        batchedDocuments = []
        articles_folder = 'articles_test'
        files = os.listdir(articles_folder)
        for file_name in files:
            # Read the file contents
            text = open(os.path.join(articles_folder, file_name), encoding='utf8').read()
            batchedDocuments.append(text)

        # Get Classifications
        # Get Classifications
        operation = ai_client.begin_single_label_classify(
            batchedDocuments,
            project_name=project_name,
            deployment_name=deployment_name
        )
        # Get the batched documents from the language client
        document_results = operation.result()

        for doc, classification_result in zip(files, document_results):
            if classification_result.kind == "CustomDocumentClassification":
                classification = classification_result.classifications[0]
                print("{} was classified as '{}' with confidence score {}.".format(
                    doc, classification.category, classification.confidence_score)
                )
            elif classification_result.is_error is True:
                print("{} has an error with code '{}' and message '{}'".format(
                    doc, classification_result.error.code, classification_result.error.message)
                )


    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()