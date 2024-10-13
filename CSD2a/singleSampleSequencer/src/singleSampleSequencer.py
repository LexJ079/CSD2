import simpleaudio as sa
import time

def vraag_bpm():
    # Functie om BPM te vragen en te checken
    while True:
        antwoord = input("De default tempo is 120 BPM. Wil je dit aanpassen? [y/n] ").strip().lower()
        if antwoord == "y":
            try:
                bpm = int(input("Vul hier de BPM in: "))
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

# Laad sample
rimSample = sa.WaveObject.from_wave_file("rimSample.wav")

# Functie om de durations van kwartnoten om te zetten naar timestamps in zestienden
def durationsToTimestamps16th(srcSeq, bpm):

    # Bereken de duur van een zestiende noot in seconden
    sixteenthDuration = 60 / (bpm * 4)
    timestamps = []
    currentTime = 0.0

    # Bereken de timestamps voor elke duur in srcSeq
    for duration in srcSeq:
        timestamps.append(currentTime)
        currentTime += duration * 4 * sixteenthDuration

    return timestamps

# Functie om zestienden timestamps om te zetten naar seconden
def timestampsToSeconds(timestamps, bpm):

    # Bereken de duur van een zestiende noot in seconden
    sixteenthDuration = 60 / (bpm * 4)
    return [ts * sixteenthDuration for ts in timestamps]

# Functie om de sample af te spelen op basis van tijdstempels
def playSequence(timestampsInSeconden):
    for timestamp in timestampsInSeconden:
        time.sleep(timestamp)  # Wacht tot de juiste tijd
        rimSample.play()  # Speel de sample af
        time.sleep(0.001)  # Kleine pauze om overlap te voorkomen

bpm = vraag_bpm()
print("De BPM is nu:", bpm)

# Ritmische sequence in kwartnoten
noteDurSeq = [1, 1.5, 0.5, 1]

# Roep de functie aan om de timestamps te berekenen
timestamps = durationsToTimestamps16th(noteDurSeq, bpm)
print("Timestamps in zestienden:", timestamps)

# Zet de timestamps in zestienden om naar tijd in seconden
timestampsInSeconden = timestampsToSeconds(timestamps, bpm)
print("Timestamps in seconden:", timestampsInSeconden)

playSequence(timestampsInSeconden)

