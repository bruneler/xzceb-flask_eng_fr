import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('8_33R81Fms2tqlD2wFaatoltfGr3oheXuG1WUsZKwqD5')

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/0288ba7e-e219-4349-8105-2f4ba1139c9b')


def englishToFrench(englishtext):
    translation = language_translator.translate(text=englishtext, model_id="en-fr").get_result()
    frenchtext = translation['translations'][0]['translation']
    return frenchtext


def frenchToEnglish(frenchtext):
    translation = language_translator.translate(text=frenchtext, model_id="fr-en").get_result()
    englishtext = translation['translations'][0]['translation']
    return englishtext
