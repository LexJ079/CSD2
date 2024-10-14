#event based sequencer

#Opdracht: Maak een sequencer die een percussieve loop van minimaal 16 events afspeelt op
#de momenten die worden aangegeven door hun timestamps. Gebruik drie verschillende
#samples. Experimenteer met gelijktijdige en sequentiële events.
#Maak een functie die één event afhandelt en roep deze aan op het moment dat door de
#timestamp van de event wordt aangegeven. Zo’n functie wordt een event handler genoemd

import simpleaudio as sa
import time

# laad samples
kick = sa.WaveObject.from_wave_file("kick.wav")
snare = sa.WaveObject.from_wave_file("snare.wav")
hihat = sa.WaveObject.from_wave_file("hihat.wav")


# events in ms
events = [
    {"timestamp": 0, "instrument": "kick", "velocity": 100, "duration": 100},
    {"timestamp": 250, "instrument": "hihat", "velocity": 100, "duration": 100},
    {"timestamp": 375, "instrument": "snare", "velocity": 100, "duration": 100},
    {"timestamp": 500, "instrument": "kick", "velocity": 100, "duration": 100},
    {"timestamp": 750, "instrument": "snare", "velocity": 100, "duration": 100},
    {"timestamp": 1125, "instrument": "hihat", "velocity": 100, "duration": 100},
    {"timestamp": 1250, "instrument": "kick", "velocity": 100, "duration": 100},
    {"timestamp": 1500, "instrument": "kick", "velocity": 100, "duration": 100},
    {"timestamp": 1750, "instrument": "snare", "velocity": 100, "duration": 100},
    {"timestamp": 2000, "instrument": "kick", "velocity": 100, "duration": 100},
    {"timestamp": 2250, "instrument": "hihat", "velocity": 100, "duration": 100},
    {"timestamp": 2375, "instrument": "snare", "velocity": 100, "duration": 100},
    {"timestamp": 2500, "instrument": "kick", "velocity": 100, "duration": 100},
    {"timestamp": 2750, "instrument": "snare", "velocity": 100, "duration": 100},
    {"timestamp": 3125, "instrument": "hihat", "velocity": 100, "duration": 100},
    {"timestamp": 3250, "instrument": "snare", "velocity": 100, "duration": 100},
    {"timestamp": 3375, "instrument": "snare", "velocity": 100, "duration": 100},
    {"timestamp": 3500, "instrument": "kick", "velocity": 100, "duration": 100},
    {"timestamp": 3750, "instrument": "snare", "velocity": 100, "duration": 100},
]

# functie om juiste instrument te spelen per event
def eventHandler(event):
    instrument = event["instrument"]
    if instrument == "kick":
        kick.play()
    elif instrument == "snare":
        snare.play()
    elif instrument == "hihat":
        hihat.play()

# Sequencer: play events based on their timestamps
def playSequence(events):
    startTime = time.time()  # Get the current time
    for event in events:

        # Calculate how much time to wait before playing the event (hier heb ik hulp gevraagd aan ChatGPT)

        waitTime = event["timestamp"] / 1000.0  # Convert to seconds
        currentTime = time.time()
        elapsedTime = currentTime - startTime

        # If we're ahead of schedule, wait until it's time to play the event
        if waitTime > elapsedTime:
            time.sleep(waitTime - elapsedTime)

        # Handle the event (play the sound)
        eventHandler(event)

# Start the sequencer
playSequence(events)

