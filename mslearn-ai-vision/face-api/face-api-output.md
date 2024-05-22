# Using Face API

It analyzes an image file and detects any faces it contains, including attributes for occlusion, blur, and the presence of spectacles. The details of each face are displayed, including a unique face identifier that is assigned to each face; and the location of the faces is indicated on the image using a bounding box.

## people.jpg
Enter a number:1
Detecting faces in images/people.jpg
2 faces detected.

Face number 1
 - Blur:
   - blur_level: Low
   - value: 0.0
 - Occlusion:
   - forehead_occluded: False
   - eye_occluded: False
   - mouth_occluded: False
 - Glasses:noGlasses

Face number 2
 - Blur:
   - blur_level: Low
   - value: 0.0
 - Occlusion:
   - forehead_occluded: False
   - eye_occluded: False
   - mouth_occluded: False
 - Glasses:readingGlasses

Results saved in detected_people.jpg

## people2.jpg
Enter a number:2
Detecting faces in images/people2.jpg
2 faces detected.

Face number 1
 - Blur:
   - blur_level: Low
   - value: 0.09
 - Occlusion:
   - forehead_occluded: False
   - eye_occluded: False
   - mouth_occluded: False
 - Glasses:readingGlasses

Face number 2
 - Blur:
   - blur_level: Low
   - value: 0.0
 - Occlusion:
   - forehead_occluded: False
   - eye_occluded: False
   - mouth_occluded: False
 - Glasses:noGlasses

Results saved in detected_people2.jpg