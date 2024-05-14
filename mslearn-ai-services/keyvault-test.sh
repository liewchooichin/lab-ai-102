#!/bin/sh
mykey=4a44f2f5ab424bbbbe46354043889fa1
myendpoint=https://lcclab002.cognitiveservices.azure.com/
curl -X POST "$myendpoint/text/analytics/v3.1/languages?'" -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: $mykey" --data-ascii "{'documents':[{'id':1,'text':'bonjour'}], 'kind': 'LanguageDetection'}"