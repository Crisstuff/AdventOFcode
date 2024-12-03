#!/
filnavn = "puzzle_input.txt"

# Generell funksjon for å lese filer
def input_data (filnavn):
    data = {}
    try:
        with open(filnavn, 'r') as fil:
            for linje in fil:
                deler = linje.strip().split('-')
                if len(deler) == 2:
                    data[deler[0].strip()] = deler[1].strip()
    except FileNotFoundError:
        print(f"Filen {filnavn} ble ikke funnet.")
    return data

def algorytme(): 

    ; 

def output_data ():
    

