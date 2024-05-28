# Classify hemlock or cherry plant
# From
# https://learn.microsoft.com/en-us/azure/ai-services/Custom-Vision-Service/quickstarts/image-classification?tabs=linux%2Cvisual-studio&pivots=programming-language-python

from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

# retrieve environment variables
ENDPOINT = os.environ["TRAININGENDPOINTVISION"]
training_key = os.environ["TRAININGKEYVISION"]
prediction_key = os.environ["PREDICTIONKEYVISION"]
prediction_resource_id = os.environ["PREDICTION_RESOURCE_ID_VISION"]

# authenticate the client
credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
trainer = CustomVisionTrainingClient(ENDPOINT, credentials)
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

# create a new custom vision project
publish_iteration_name = "hemlock-classifier"

#credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
#trainer = CustomVisionTrainingClient(ENDPOINT, credentials)

# Create a new project
print ("Creating project...")
#project_name = uuid.uuid4()
#project = trainer.create_project(project_name)
project = trainer.create_project(
    name="hemlock-classifier",
    description="Hemlock and Japanese Cherry",
    classification_type="Multiclass"
)

# add tags
# Make two tags in the new project
hemlock_tag = trainer.create_tag(project.id, "hemlock")
cherry_tag = trainer.create_tag(project.id, "japanese_cherry")

# Upload and tag images
base_image_location = os.path.join (os.path.dirname(__file__), "Images")

print("Adding images...")

image_list = []
# Total 10 images. The range is from (1, 11) because the 11 is not included in the range.
# Directory structure:
#    Images - Hemlock
#           - Japanese_Cherry
for image_num in range(1, 11):
    file_name = "hemlock_{}.jpg".format(image_num)
    with open(os.path.join (base_image_location, "Hemlock", file_name), "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[hemlock_tag.id]))

for image_num in range(1, 11):
    file_name = "japanese_cherry_{}.jpg".format(image_num)
    with open(os.path.join (base_image_location, "Japanese_Cherry", file_name), "rb") as image_contents:
        image_list.append(ImageFileCreateEntry(name=file_name, contents=image_contents.read(), tag_ids=[cherry_tag.id]))

upload_result = trainer.create_images_from_files(project.id, ImageFileCreateBatch(images=image_list))
if not upload_result.is_batch_successful:
    print("Image batch upload failed.")
    for image in upload_result.images:
        print("Image status: ", image.status)
    exit(-1)

# train the project
print ("Training...")
iteration = trainer.train_project(project.id)
while (iteration.status != "Completed"):
    iteration = trainer.get_iteration(project.id, iteration.id)
    print ("Training status: " + iteration.status)
    print ("Waiting 10 seconds...")
    time.sleep(10)

# Tip
# Train with selected tags
# You can optionally train on only a subset of your applied tags. You may want to do this if you haven't
# applied enough of certain tags yet, but you do have enough of others. In the train_project call, set the 
# optional parameter selected_tags to a list of the ID strings of the tags you want to use. The model will
# train to only recognize the tags on that list.

# Publish the current iteration
# An iteration is not available in the prediction endpoint until it is published. The following code makes 
# the current iteration of the model available for querying.

# publish_iteration_name is also known as model name. 
# Above the model name is defined as below:
#     publish_iteration_name = "hemlock-classifier"
# The iteration is now trained. Publish it to the project endpoint
trainer.publish_iteration(project.id, iteration.id, publish_iteration_name, prediction_resource_id)
print ("Done!")

# Now there is a trained endpoint that can be used to make a prediction
#prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
#predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

# Make sure that the path is correct for Test/test_image.jpg
# Test with prediction endpoint
with open(os.path.join (base_image_location, "Test/test_image.jpg"), "rb") as image_contents:
    results = predictor.classify_image(
        project.id, publish_iteration_name, image_contents.read())

    # Display the results.
    for prediction in results.predictions:
        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))

