import json

def serialize(dizionario: dict, percorso_file: str):
    dizionario_stringa = json.dumps(dizionario)
    try:
        with open(percorso_file, 'w') as file:
            file.write(dizionario_stringa)
        return True
    except Exception as e:
        return False

def deserialize(percorso_file: str):
    try:
        with open(percorso_file, 'r') as file:
            dizionario = json.load(file)
        return dizionario
    except Exception as e:
        return None

def analize_quiz(dati):
    domande_totali = 0
    opzioni_totali = 0
    domande_matematica = 0
    
    for categoria, domande in dati['quiz'].items():
        for info_domanda in domande.values():
            domande_totali += 1
            opzioni_totali += len(info_domanda['options'])
            if categoria == 'maths':
                domande_matematica += 1
    
    if domande_totali != 0:
        risultato = opzioni_totali / domande_totali
    else:
        risultato = 0

    media_opzioni = risultato
    
    return domande_totali, media_opzioni, domande_matematica

def print_list(lData, sRoot):
    for element in lData:
        if isinstance(element, str):
            print("\t" + element)
        elif isinstance(element, dict):
            print_dictionary(element, sRoot)
        elif isinstance(element, list):
            print_list(element, sRoot)

def print_dictionary(dData, sRoot):
    for keys, values in dData.items():
        if sRoot != "":
            print("Trovata chiave " + sRoot + "." + keys)
        else:
            print("Trovata chiave " + keys)

        if isinstance(dData[keys], dict):
            if sRoot != "":
                print_dictionary(dData[keys], sRoot + "." + keys)
            else:
                print_dictionary(dData[keys], keys)
        elif isinstance(dData[keys], list):
            if sRoot != "":
                print_list(dData[keys], sRoot + "." + keys)
            else:
                print_list(dData[keys], keys)


percorso_file = "/home/user/Scrivania/PythonProjects/quiz.json"

dati_quiz = deserialize(percorso_file)

if dati_quiz:
    print("Esplorazione della struttura JSON:")
    print_dictionary(dati_quiz, "")

    domande_totali, media_opzioni, domande_matematica = analize_quiz(dati_quiz)
    
    print(f"\nTotale domande: {domande_totali}")
    print(f"Numero medio di risposte possibili: {media_opzioni:.2f}")
    print(f"Domande di matematica: {domande_matematica}")
else:
    print("Impossibile caricare i dati dal file JSON.")
