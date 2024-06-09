# The audio file is setup to be run from reading
# the input "audio/time.wav". The output is stored in
# "audio/tell-time.wav".

#from dotenv import load_dotenv
from datetime import datetime
import os

# Import namespaces
# Import namespaces
import azure.cognitiveservices.speech as speech_sdk

def main():
    try:
        global speech_config

        # Get Configuration Settings
        #load_dotenv()
        ai_key = os.getenv('SPEECH_KEY')
        ai_region = "eastus" #os.getenv('SPEECH_REGION')

        # Configure speech service
        # Configure speech service
        speech_config = speech_sdk.SpeechConfig(ai_key, ai_region)
        print('Ready to use speech service in:', speech_config.region)

        # Get spoken input
        command = TranscribeCommand()
        if command.lower() == 'what time is it?':
            TellTime()

    except Exception as ex:
        print(ex)

def TranscribeCommand():
    command = ''

    # Configure speech recognition
    # Configure speech recognition
    inputFile = './audio/time.wav'
    audio_config = speech_sdk.AudioConfig(filename=inputFile)
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
    print(f'Processing audio input: {inputFile}')

    # Process speech input
    # Process speech input
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        print("speech.properties")
        print(speech.properties)
        print(f"Reason: {speech.reason}")
        print("Text from the speech:")
        command = speech.text
        print(command)
    else:
        print(speech.reason)
        if speech.reason == speech_sdk.ResultReason.Canceled:
            cancellation = speech.cancellation_details
            print(cancellation.reason)
            print(cancellation.error_details)

    # Return the command
    return command


def TellTime():
    now = datetime.now()
    response_text = 'The time is {}:{:02d}'.format(now.hour,now.minute)

    # Speech output file
    outputFile = "./audio/tell-time.wav"
    audio_config = speech_sdk.audio.AudioConfig(filename=outputFile)
    print(f"Speech output file: {outputFile}")

    # Configure speech synthesis
    # Configure speech synthesis
    # To use other voices: change this 'en-GB-LibbyNeural' 
    speech_config.speech_synthesis_voice_name = "en-GB-RyanNeural"
    speech_synthesizer = speech_sdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config)

    # Synthesize spoken output
    # Synthesize spoken output
    speak = speech_synthesizer.speak_text_async(response_text).get()
    print("Text to speech")
    print(f"Reasons: {speak.reason}")
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)
    # Using SSML
    # Synthesize spoken output
    responseSsml = " \
        <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'> \
            <voice name='en-GB-LibbyNeural'> \
                {} \
                <break strength='weak'/> \
                Time to end this lab! \
            </voice> \
        </speak>".format(response_text)
    speak = speech_synthesizer.speak_ssml_async(responseSsml).get()
    print(f"Reason: {speak.reason}")
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)

    # Print the response
    print(response_text)


if __name__ == "__main__":
    main()