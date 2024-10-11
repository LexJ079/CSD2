# User input
#“Bij het uitvoeren van het script wordt de default BPM aan de gebruiker getoond. Daarna krijgt de
#gebruiker de mogelijkheid om in de terminal een andere BPM in te voeren die vanaf dat moment gebruikt
#wordt.“
#Denk hierbij ook aan het volgende: wat doet je script wanneer een gebruiker verkeerde input geeft? Wat
#is verkeerde input en met welke input kun je wel iets?

import simpleaudio as sa

def vraag_bpm():
    # Functie om BPM te vragen en te checken
    while True:
        antwoord = input("De default tempo is 120 BPM. Wil je dit aanpassen? [y/n] ").strip().lower()
        if antwoord == "y":
            try:
                bpm = int(input("Vul hier de BPM in: ").strip())
                if bpm > 0:
                    return bpm
                else:
                    print("BPM moet een positief getal zijn.")
            except ValueError:
                print("Ongeldige invoer. Vul een geldig getal in.")
        elif antwoord == "n":
            return 120
        else:
            print("Ongeldige invoer. Voer 'y' of 'n' in.")

#load sample
rimSample = sa.WaveObject.from_wave_file("rimSample.wav")

# Functie om de durations van kwartnoten om te zetten naar timestamps in zestienden
def durationsToTimestamps16th(srcSeq, bpm):
    # Bereken de duur van een zestiende noot in seconden
    sixteenth_duration = 60 / (bpm * 4)
    timestamps = []
    current_time = 0.0

    # Bereken de timestamps voor elke duur in srcSeq
    for duration in srcSeq:
        timestamps.append(current_time)
        current_time += duration * 4 * sixteenth_duration

    return timestamps

# Vraag de BPM aan de gebruiker
bpm = vraag_bpm()
print("De BPM is nu:", bpm)


# Ritmische sequence in kwartnoten
noteDurSeq = [1, 1.5, 0.5, 1]

# Roep de functie aan om de timestamps te berekenen
timestamps = durationsToTimestamps16th(noteDurSeq, bpm)
print("Tijdstempels in zestienden:", timestamps)
