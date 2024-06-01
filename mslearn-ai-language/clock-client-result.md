# Conversational language understanding

A simple clock project on telling time, date and day of week. 

```
python clock-client.py 

Enter some text ("quit" to stop)
what time in singapore?
view top intent:
        top intent: GetTime
        category: GetTime
        confidence score: 0.92562836

view entities:
        category: Location
        text: singapore
        confidence score: 1
query: what time in singapore?
23:11

Enter some text ("quit" to stop)
what is the date ing Singapore?
view top intent:
        top intent: GetDate
        category: GetDate
        confidence score: 0.91984046

view entities:
        category: Location
        text: Singapore
        confidence score: 1
query: what is the date ing Singapore?
06/01/2024

What is day on 01/06/2024?
view top intent:
        top intent: GetDay
        category: GetDay
        confidence score: 0.9773884

view entities:
        category: date
        text: 01/06/2024
        confidence score: 1
query: What is day on 01/06/2024?
Saturday
```