import simpleaudio as sa
import time



# vragen naar hoeveelheden en tijden
numRepeats = int(input("Hoevaak wil je het ritme horen?: "))

numNotes = int(input("Hoeveel noten in het ritme? "))

noteDurs = []
for i in range(numNotes):
    noteDur = float(input(f"Welke tijdwaarde heeft noot nummer {i + 1}? "))
    noteDurs.append(noteDur)

bpm = float(input("Please enter the bpm: "))



# verandert de nootwaarden in tijdwaarden
quarternoteDur = 60 / bpm
timeDurs = []
for noteDur in noteDurs:
    timeDurs.append(noteDur * quarternoteDur)



# sample laden en herhalen
sample = sa.WaveObject.from_wave_file("sample.wav")

for _ in range(numRepeats):
    for tDur in timeDurs:
        sample.play().wait_done()
        time.sleep(tDur)
