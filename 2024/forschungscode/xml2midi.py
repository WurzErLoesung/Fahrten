from music21 import converter
from midi2audio import FluidSynth


fs = FluidSynth()


xml_path = "./notes.musicxml"
midi_path = "C:/Users/Sevi/Desktop/Stuff/Python/Fahrten/2024/forschungscode/output.mid"

# Parse the MusicXML file
score = converter.parse(xml_path)

# Show the MIDI file
score.write('midi', fp=midi_path)
fs.midi_to_audio(midi_path, 'output.wav')