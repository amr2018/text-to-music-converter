# convert text to music
import mido
import random

# load text
def load_text():
    file = open('test.txt', 'r', errors='ignore')
    return file.read().strip().lower().replace('\n', '')

# encode text
def encode_text(text):
    encodings = []
    for i in text:
        code = ord(i)
        if code <= 127:
            encodings.append(code)

    return encodings


# convert encodings to midi or music
def convert_encodings_to_midi(encodings):
    # create midi file
    midiFile = mido.MidiFile()
    track = mido.MidiTrack()

    # add track to midi file
    for _ in range(len(encodings)):
        midiFile.tracks.append(track)

    # add notes in all tracks
    for track, note in zip(midiFile.tracks, encodings):
        track.append(mido.Message(
            type = 'note_on',
            note = note,
            velocity = 64,
            time = 120
        ))

    # save midi file
    midiFile.save('out.midi')



encodings = encode_text(text = load_text()[random.randint(0, 10):])
convert_encodings_to_midi(encodings = encodings)
