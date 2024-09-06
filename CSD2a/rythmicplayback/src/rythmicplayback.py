import simpleaudio as sa

# Vraagt hoe vaak het geluid moet worden afgespeeld
numPlaybackTimes = int(input("Hoe vaak moet het geluid afspelen? "))

# Laadt de audio file (synth.wav)
wave_obj = sa.WaveObject.from_wave_file("synth.wav")

# Speelt het geluid het opgegeven aantal keren af
for i in range(numPlaybackTimes):
    play_obj = wave_obj.play()  # Speelt de audio af
    play_obj.wait_done()  # Wacht tot de audio is afgelopen
   


