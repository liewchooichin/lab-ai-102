# It analyzes an image file and detects any faces it contains, including 
# attributes for occlusion, blur, and the presence of spectacles. The 
# details of each face are displayed, including a unique face identifier
# that is assigned to each face; and the location of the faces is indicated
# on the image using a bounding box.

from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt

# Import namespaces
# Import namespaces
from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import FaceAttributeType
from msrest.authentication import CognitiveServicesCredentials

def main():

    global face_client

    try:
        # Get Configuration Settings
        #load_dotenv()
        cog_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        cog_key = os.getenv('AI_SERVICE_KEY')

        # Authenticate Face client
        # Authenticate Face client
        credentials = CognitiveServicesCredentials(cog_key)
        face_client = FaceClient(cog_endpoint, credentials)

        # Menu for face functions
        print('Enter a number to detect faces.\nAny other key to quit')
        print('1: people.jpg')
        print('2: people2.jpg')
        print('3: person1.jpg')
        print('4: person2.jpg')
        command = input('Enter a number:')
        # Original code
        #if command == '1':
            #DetectFaces(os.path.join('images','people.jpg'))
        # Match the number to the images to be analyzed
        # This is version 3.9 on Debian in the .devcontainer.
        # match is only supported in python >= 3.10.
        if command == 1:
                DetectFaces(os.path.join('images','people.jpg'))
        elif command == 2:
                DetectFaces(os.path.join('images','people2.jpg'))
        elif command == 3:
                DetectFaces(os.path.join('images','person1.jpg'))
        elif command == 4:
                DetectFaces(os.path.join('images','person2.jpg'))
        else:
             print("Exit")
    except Exception as ex:
        print(ex)

def GetFaces(image_file, features):
    # Get faces
    with open(image_file, mode="rb") as image_data:
        detected_faces = face_client.face.detect_with_stream(image=image_data,
                                                            return_face_attributes=features,                     return_face_id=False)

    if len(detected_faces) > 0:
        print(len(detected_faces), 'faces detected.')

        # Prepare image for drawing
        fig = plt.figure(figsize=(8, 6))
        plt.axis('off')
        image = Image.open(image_file)
        draw = ImageDraw.Draw(image)
        color = 'lightgreen'
        face_count = 0

        # Draw and annotate each face
        for face in detected_faces:

            # Get face properties
            face_count += 1
            print('\nFace number {}'.format(face_count))

            detected_attributes = face.face_attributes.as_dict()
            if 'blur' in detected_attributes:
                print(' - Blur:')
                for blur_name in detected_attributes['blur']:
                    print('   - {}: {}'.format(blur_name, detected_attributes['blur'][blur_name]))
                    
            if 'occlusion' in detected_attributes:
                print(' - Occlusion:')
                for occlusion_name in detected_attributes['occlusion']:
                    print('   - {}: {}'.format(occlusion_name, detected_attributes['occlusion'][occlusion_name]))

            if 'glasses' in detected_attributes:
                print(' - Glasses:{}'.format(detected_attributes['glasses']))

            # Draw and annotate face
            r = face.face_rectangle
            bounding_box = ((r.left, r.top), (r.left + r.width, r.top + r.height))
            draw = ImageDraw.Draw(image)
            draw.rectangle(bounding_box, outline=color, width=5)
            annotation = 'Face number {}'.format(face_count)
            plt.annotate(annotation,(r.left, r.top), backgroundcolor=color)

        # Save annotated image
        plt.imshow(image)
        outputfile = 'detected_faces.jpg'
        fig.savefig(outputfile)

        print('\nResults saved in', outputfile)

def DetectFaces(image_file):
    print('Detecting faces in', image_file)

    # Specify facial features to be retrieved
    # Specify facial features to be retrieved
    features = [FaceAttributeType.occlusion,
                FaceAttributeType.blur,
                FaceAttributeType.glasses]

    # Get faces
    GetFaces(image_file, features)

if __name__ == "__main__":
    main()