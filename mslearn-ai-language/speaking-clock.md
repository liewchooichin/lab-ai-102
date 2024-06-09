# Text to speech and vice versa

`python speaking-clock.py`

The audio file is setup to be run from reading
the input "audio/time.wav". The output is stored in
"audio/tell-time.wav".


```
Ready to use speech service in: eastus
Processing audio input: ./audio/time.wav
speech.properties
{<PropertyId.SpeechServiceResponse_JsonResult: 5000>: '{"Id":"8fc6c3a9db4e485787f0150dfcbb48fb","RecognitionStatus":"Success","DisplayText":"What time is it?","Offset":5500000,"Duration":12000000,"Channel":0}', <PropertyId.SpeechServiceResponse_RecognitionLatencyMs: 5002>: '2070'}
Reason: ResultReason.RecognizedSpeech
Text from the speech:
What time is it?
Speech output file: ./audio/tell-time.wav
Text to speech
Reasons: ResultReason.SynthesizingAudioCompleted
Reason: ResultReason.SynthesizingAudioCompleted
The time is 14:23
```