# User input
#“Bij het uitvoeren van het script wordt de default BPM aan de gebruiker getoond. Daarna krijgt de
#gebruiker de mogelijkheid om in de terminal een andere BPM in te voeren die vanaf dat moment gebruikt
#wordt.“
#Denk hierbij ook aan het volgende: wat doet je script wanneer een gebruiker verkeerde input geeft? Wat
#is verkeerde input en met welke input kun je wel iets?

import simpleaudio as sa

antwoord = input("De default tempo is 120 BPM. Wil je dit aanpassen? [y/n] ")

if antwoord =="y" :
    bpm = int(input("Vul hier de BPM in: "))
    print("de BPM is nu: " , bpm )

if antwoord =="n" :
    print("de BPM is nu: 120  ")
    bpm = 120

if bpm <0 :
    print("geen geldige BPM")
    bpm = int(input("Vul hier een ander BPM in: "))
    print("de BPM is nu: " , bpm )




# create a list with ‘note timestamps' in 16th at which we should play the sample
# create a list with possible note durations: sixteenth, eighth and a quarter note
timestamps16th = [0, 2, 4, 8, 11]
noteDurations = [0.25, 0.5, 1]


