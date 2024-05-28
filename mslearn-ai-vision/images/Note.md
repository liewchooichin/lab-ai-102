# OCR Read text

## Note.jpg
```
python read-text.py

1: Use Read API for image (Lincoln.jpg)
2: Read handwriting (Note.jpg)
Any other key to quit

Enter a number:2
```

## Results

```
Text:
  Shopping List
   Bounding Polygon: ((231, 141), (693, 147), (691, 245), (230, 240))
    Word: 'Shopping', Bounding Polygon: ((240, 141), (535, 149), (531, 245), (234, 234)), Confidence: 0.9630
    Word: 'List', Bounding Polygon: ((554, 149), (689, 147), (686, 244), (550, 245)), Confidence: 0.8300
  Non- Fat milk
   Bounding Polygon: ((149, 302), (633, 297), (633, 374), (150, 378))
    Word: 'Non-', Bounding Polygon: ((150, 303), (309, 301), (310, 378), (153, 378)), Confidence: 0.5770
    Word: 'Fat', Bounding Polygon: ((324, 301), (438, 300), (437, 378), (325, 378)), Confidence: 0.8420
    Word: 'milk', Bounding Polygon: ((476, 299), (620, 298), (617, 374), (475, 377)), Confidence: 0.9940
  Bread
   Bounding Polygon: ((138, 400), (382, 399), (383, 472), (138, 474))
    Word: 'Bread', Bounding Polygon: ((152, 400), (366, 400), (368, 471), (151, 475)), Confidence: 0.9950
  Eggs
   Bounding Polygon: ((146, 517), (351, 526), (348, 605), (146, 609))
    Word: 'Eggs', Bounding Polygon: ((149, 517), (342, 519), (341, 610), (148, 609)), Confidence: 0.9920

  Results saved in images/text.jpg
```