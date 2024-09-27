# User input
#“Bij het uitvoeren van het script wordt de default BPM aan de gebruiker getoond. Daarna krijgt de
#gebruiker de mogelijkheid om in de terminal een andere BPM in te voeren die vanaf dat moment gebruikt
#wordt.“
#Denk hierbij ook aan het volgende: wat doet je script wanneer een gebruiker verkeerde input geeft? Wat
#is verkeerde input en met welke input kun je wel iets?

antwoord = input("De default tempo is 120 BPM. Wil je dit aanpassen? [y/n] ")

if antwoord =="y" :
    bpm = int(input("Vul hier de BPM in: "))
    print("de BPM nu: " , bpm )

if antwoord =="n" :
    print("de BPM nu: 120  ")
    bpm = 120
