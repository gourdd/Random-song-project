from music21 import *
import random_notes

# Methods that manage measure separation and stream offsets

def random_measure(root_midi, doubled=False, highest_length=4.0, minor=False):

    max_offset = 4.0
    the_measure = stream.Measure()
    is_full_bool = False

    while not is_full_bool:
        the_note = random_notes.random_note(root_midi, doubled, highest_length, minor)
        if is_measure_full(the_measure, the_note):
            the_note.quarterLength = max_offset - the_measure[-1].offset
            the_measure.append(the_note)
            is_full_bool = True
        else:
            the_measure.append(the_note)

    return the_measure

def is_measure_full(the_measure, next_note):

    if not len(the_measure) == 0:
        capacity_check = the_measure[-1].offset + next_note.quarterLength
    else:
        return False

    if capacity_check > 4.0:
        return True
    else:
        return False

measure_test = random_measure(60)
measure_test.show()