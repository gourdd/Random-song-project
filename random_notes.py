from music21 import *
import random

# Methods that deal with random note generation

def random_note(root_midi, doubled=False, highest_length=4.0, minor=False):

    the_pitch = random_pitch(root_midi, doubled, minor)
    the_note = note.Note(midi=the_pitch)

    the_note.duration.quarterLength = random_length(highest_length)

    return the_note

def random_pitch(root_midi, doubled=False, minor=False):

    the_scale = generate_major_scale(root_midi, doubled, minor)
    the_pitch = random.choice(the_scale)
    
    return the_pitch

def random_length(highest_length):

    length_ranges = [0.25, 0.5, 1.0, 2.0, 4.0] 

    if highest_length in length_ranges:
        length_index = length_ranges.index(highest_length)
        clear_from = length_index + 1
        while length_ranges[-1] != highest_length:
            length_ranges.pop(clear_from)
        the_length = random.choice(length_ranges)
        return the_length
    else:
        the_length = random.choice(length_ranges)
        return the_length 

def generate_major_scale(root_midi=60, doubled=False, minor=False):

    the_scale = []

    if minor == False:
        the_scale.append(root_midi)
        the_scale.append(root_midi + 2)
        the_scale.append(root_midi + 4)
        the_scale.append(root_midi + 5)
        the_scale.append(root_midi + 7)
        the_scale.append(root_midi + 9)
        the_scale.append(root_midi + 11)
    elif minor == True:
        the_scale.append(root_midi)
        the_scale.append(root_midi + 2)
        the_scale.append(root_midi + 3)
        the_scale.append(root_midi + 5)
        the_scale.append(root_midi + 7)
        the_scale.append(root_midi + 8)
        the_scale.append(root_midi + 10)

    if doubled == True:
        stored_minor = minor
        doubled_scale = generate_major_scale(root_midi + 12, minor=stored_minor)
        for doubled_note in doubled_scale:
            the_scale.append(doubled_note)

    return the_scale