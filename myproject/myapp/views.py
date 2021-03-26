from django.shortcuts import render
import spacy
import xml.etree.ElementTree as ET
import pandas_read_xml as pdx
import os
from django.conf import settings
from myproject.settings import BASE_DIR

nlp = spacy.load("en_core_web_trf")
print("nlp loaded")


# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    testquery = str(request.GET['testquery'])

    nouns = getNouns(testquery)
    result = conditionsFromMedicalTerms(nouns)

    return render(request, 'result.html', {'result': result})

def getNouns(sentence):
            # nlp = spacy.load("en_core_web_trf")
            nlpSentence = nlp(sentence)
            nouns = []
            for token in nlpSentence:
                if token.pos_ == "NOUN":
                    nouns.append(token)
            # print("nouns...", nouns)        
            return nouns  

def conditionsFromMedicalTerms(nouns):
    # root = ET.parse('./phenotypes.xml').getroot()
    print(os.getcwd())
    file_path = os.path.join(BASE_DIR, 'model/phenotypes.xml')
    df = pdx.read_xml(file_path, ['JDBOR', 'HPODisorderSetStatusList'],encoding='cp1252')
    possibleDiseases = []
    for noun in nouns:
        # check if noun is in sympton, if yes then get its corresponding disease and add to diseases
        for i in range(len(df)):
            if 'Disorder' in df.iloc[i]['HPODisorderSetStatus']:
                if 'HPODisorderAssociationList' in df.iloc[i]['HPODisorderSetStatus']['Disorder']:
                    if 'HPODisorderAssociation' in df.iloc[i]['HPODisorderSetStatus']['Disorder']['HPODisorderAssociationList']:
                        symptom = df.iloc[i]['HPODisorderSetStatus']['Disorder']['HPODisorderAssociationList']['HPODisorderAssociation'][0]['HPO']['HPOTerm']
                        # TODO loop over j
                        if noun.text in symptom:
                            # print("symptom found!")
                            diseaseName = df.iloc[i]['HPODisorderSetStatus']['Disorder']['Name']['#text']
                            possibleDiseases.append(diseaseName)
                        # df.iloc[i]['HPODisorderSetStatus']['Disorder']['HPODisorderAssociationList']['HPODisorderAssociation'][j]['HPO']['HPOTerm']
                        # i - Diseases, j - symptoms
    return possibleDiseases
