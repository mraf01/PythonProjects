import requests, json, sys


base_url = "https://127.0.0.1:8080"


def GetDatiCittadino():
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    dataN = input("Inserisci la data di nascita (gg/mm/aaaa): ")
    codF = input("Inserisci il codice fiscale: ")
    datiCittadino = {
        "nome": nome, 
        "cognome": cognome, 
        "data nascita": dataN, 
        "codice fiscale": codF
    }
    return datiCittadino


def GetCodicefiscale():
    cod = input('Inserisci codice fiscale: ')
    return {"codice fiscale": cod}



while True:
    print("\nOperazioni disponibili:")
    print("1. Inserisci cittadino")
    print("2. Richiedi cittadino")
    print("3. Modifica cittadino")
    print("4. Elimina cittadino")
    print("5. Controllo cittadino")
    print("6. Esci")


    try:
        sOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue


    if sOper == 1:
        print("Aggiunta cittadino")
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = GetDatiCittadino()
        response = requests.post(api_url, json=jsonDataRequest, verify=False)

    elif sOper == 2:
        print("Richiesta dati cittadino")
        api_url = base_url + "/read_cittadino"
        jsonDataRequest = GetCodicefiscale()
        response = requests.post(api_url, json= jsonDataRequest, verify=False)
        print(response.json())

    elif sOper == 3:
        print("Modifica cittadino")
        api_url = base_url + "/update_cittadino"
        jsonDataRequest = GetDatiCittadino()
        response = requests.post(api_url, json=jsonDataRequest, verify=False)
        print(response.json())


    elif sOper == 4:
        print("Eliminazione cittadino")
        api_url = base_url + "/elimina_cittadino"
        jsonDataRequest = GetCodicefiscale()
        response = requests.post(api_url, json=jsonDataRequest, verify=False)
        print(response.json())
    
    elif sOper ==5:
        print('controllo cittadino')
        api_url = base_url + '/login_cittadino'
        jsonDataRequest = GetDatiCittadino()
        response = requests.post(api_url, json=jsonDataRequest, verify=False)
        print(response.json())


    elif sOper == 6:
        print("Buona giornata!")
        sys.exit()

    else:
        print("Operazione non disponibile, riprova.")
