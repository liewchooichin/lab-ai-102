from dotenv import load_dotenv
from datetime import datetime
import os

# Import namespaces
# Import namespaces
import azure.cognitiveservices.speech as speech_sdk

def main():
    try:
        global speech_config
        global translation_config

        # Get Configuration Settings
        #load_dotenv()
        ai_key = os.getenv('SPEECH_KEY')
        ai_region = "eastus" #os.getenv('SPEECH_REGION')

        # Configure translation
        # Configure translation
        translation_config = speech_sdk.translation.SpeechTranslationConfig(ai_key, ai_region)
        translation_config.speech_recognition_language = 'en-US'
        translation_config.add_target_language('zh')
        print(f'Ready to translate from {translation_config.speech_recognition_language}')
        print(f'to target language {translation_config.target_languages}')

        # Configure speech
        # Configure speech
        speech_config = speech_sdk.SpeechConfig(ai_key, ai_region)

        # Get user input
        # For simplicity, I use only one language in this lab.
        targetLanguage = 'zh'
        Translate(targetLanguage)
        # Skip this

        #while targetLanguage != 'quit':
        #    targetLanguage = input('\nEnter a target language\n zh = Mandarin\n ja = Japanese\n Enter anything else to stop\n').lower()
        #    if targetLanguage in translation_config.target_languages:
        #        Translate(targetLanguage)
        #    else:
        #        targetLanguage = 'quit'
                

    except Exception as ex:
        print(ex)

def Translate(targetLanguage):
    translation = ''

    # Translate speech
    # Translate speech
    audioFile = './audio/station.wav'
    audio_config = speech_sdk.AudioConfig(filename=audioFile)
    translator = speech_sdk.translation.TranslationRecognizer(translation_config, audio_config = audio_config)
    print(f"Getting speech from file {audioFile}")
    result = translator.recognize_once_async().get()
    print(f'Reason: {result.reason}')
    print('Translating "{}"'.format(result.text))
    targetLanguage = 'zh-Hans'
    translation = result.translations[targetLanguage]
    print(translation)

    # Synthesize translation
    # Synthesize translation
    # Speech output file
    outputFile = "./audio/station-zh-CN-XiaoxiaoNeural.wav"
    audio_config = speech_sdk.audio.AudioConfig(filename=outputFile)
    print(f"Speech output file: {outputFile}")
    voices = {
            "zh-Hans": "zh-CN-XiaoxiaoNeural",
    }
    print(f'Voices of translated speech: {voices["zh-Hans"]}')
    speech_config.speech_synthesis_voice_name = voices.get(targetLanguage)
    speech_synthesizer = speech_sdk.SpeechSynthesizer(
        speech_config=speech_config, audio_config=audio_config)
    speak = speech_synthesizer.speak_text_async(translation).get()
    print(f"Reason: {speak.reason}")
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)


if __name__ == "__main__":
    main()