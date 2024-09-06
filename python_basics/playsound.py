import simpleaudio as sa

# Vraagt hoe vaak het geluid moet worden afgespeeld
times = int(input("Hoe vaak moet het geluid afspelen? "))

# Laadt de audio file (synth.wav)
wave_obj = sa.WaveObject.from_wave_file("/Users/lex/HKU/Jaar2/CSD2/python_basics/synth.wav")

# Speelt het geluid het opgegeven aantal keren af
for i in range(times):
    play_obj = wave_obj.play()  # Speelt de audio af
    play_obj.wait_done()  # Wacht tot de audio is afgelopen
   


 # deze installen bij segmentation fault: pip install -U --force git+https://github.com/cexen/py-simple-audio.git
