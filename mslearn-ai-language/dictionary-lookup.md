# python dictionary-lookup.py > dictionary-lookup.md

## Dictionary lookup

Source term: aeroplane

```
Number of translation: 2
Translated to: 
飞机
架 飞机
```

## Dictionary examples

```
Source sentence: 
The aeroplane and the radio have brought us closer together.
Target sentence: 
飞机和无线电使我们更为接近。
Source sentence: 
The aeroplane is capable of five days continuous flight.
Target sentence: 
这种飞机能够持续飞翔5天。
Source sentence: 
The aeroplane is flying over the river.
Target sentence: 
飞机从河上飞过。
Source sentence: 
The aeroplane flew above the clouds.
Target sentence: 
飞机在云上面飞行。
Source sentence: 
We could use his aeroplane as one of the obstacles.
Target sentence: 
我们可以用梅的飞机作为障碍物 是的!

```


## Response from dictionary lookup

```
[
    {
        "displaySource": "aeroplane",
        "normalizedSource": "aeroplane",
        "translations": [
            {
                "backTranslations": [
                    {
                        "displayText": "plane",
                        "frequencyCount": 7548,
                        "normalizedText": "plane",
                        "numExamples": 15
                    },
                    {
                        "displayText": "aircraft",
                        "frequencyCount": 5272,
                        "normalizedText": "aircraft",
                        "numExamples": 15
                    },
                    {
                        "displayText": "airplane",
                        "frequencyCount": 2200,
                        "normalizedText": "airplane",
                        "numExamples": 15
                    },
                    {
                        "displayText": "flight",
                        "frequencyCount": 649,
                        "normalizedText": "flight",
                        "numExamples": 15
                    },
                    {
                        "displayText": "jet",
                        "frequencyCount": 330,
                        "normalizedText": "jet",
                        "numExamples": 15
                    },
                    {
                        "displayText": "aeroplane",
                        "frequencyCount": 264,
                        "normalizedText": "aeroplane",
                        "numExamples": 5
                    },
                    {
                        "displayText": "jets",
                        "frequencyCount": 157,
                        "normalizedText": "jets",
                        "numExamples": 5
                    }
                ],
                "confidence": 0.7083,
                "displayTarget": "飞机",
                "normalizedTarget": "飞机",
                "posTag": "NOUN",
                "prefixWord": ""
            },
            {
                "backTranslations": [
                    {
                        "displayText": "plane",
                        "frequencyCount": 1124,
                        "normalizedText": "plane",
                        "numExamples": 15
                    },
                    {
                        "displayText": "aircraft",
                        "frequencyCount": 274,
                        "normalizedText": "aircraft",
                        "numExamples": 15
                    },
                    {
                        "displayText": "airplane",
                        "frequencyCount": 119,
                        "normalizedText": "airplane",
                        "numExamples": 15
                    },
                    {
                        "displayText": "jet",
                        "frequencyCount": 30,
                        "normalizedText": "jet",
                        "numExamples": 11
                    },
                    {
                        "displayText": "aeroplane",
                        "frequencyCount": 18,
                        "normalizedText": "aeroplane",
                        "numExamples": 5
                    }
                ],
                "confidence": 0.2917,
                "displayTarget": "架飞机",
                "normalizedTarget": "架 飞机",
                "posTag": "NOUN",
                "prefixWord": ""
            }
        ]
    }
]
```

## Response from dictionary examples

```
[
    {
        "examples": [
            {
                "sourcePrefix": "The ",
                "sourceSuffix": " and the radio have brought us closer together.",
                "sourceTerm": "aeroplane",
                "targetPrefix": "",
                "targetSuffix": "和无线电使我们更为接近。",
                "targetTerm": "飞机"
            },
            {
                "sourcePrefix": "The ",
                "sourceSuffix": " is capable of five days continuous flight.",
                "sourceTerm": "aeroplane",
                "targetPrefix": "这种",
                "targetSuffix": "能够持续飞翔5天。",
                "targetTerm": "飞机"
            },
            {
                "sourcePrefix": "The ",
                "sourceSuffix": " is flying over the river.",
                "sourceTerm": "aeroplane",
                "targetPrefix": "",
                "targetSuffix": "从河上飞过。",
                "targetTerm": "飞机"
            },
            {
                "sourcePrefix": "The ",
                "sourceSuffix": " flew above the clouds.",
                "sourceTerm": "aeroplane",
                "targetPrefix": "",
                "targetSuffix": "在云上面飞行。",
                "targetTerm": "飞机"
            },
            {
                "sourcePrefix": "We could use his ",
                "sourceSuffix": " as one of the obstacles.",
                "sourceTerm": "aeroplane",
                "targetPrefix": "我们可以用梅的",
                "targetSuffix": "作为障碍物 是的!",
                "targetTerm": "飞机"
            }
        ],
        "normalizedSource": "aeroplane",
        "normalizedTarget": "飞机"
    }
]
```

