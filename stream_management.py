from music21 import *
from random_notes import *

# Methods that manage measure separation and stream offsets
# Create combinations of measures, add the quarter lengths up to see if they equal a clean 4.0
# If they don't, reroll.

# Features to add:
# Prompt: Ask user to input root note, doubled, highest length, minor, measure_count, and left hand
# Add min_length value
# Prompt differently for left hand
# Add separate score at the end of current score with different settings
# Add chords
# Add rests

def random_score(root_midi, doubled=False, highest_length=4.0, minor=False, measure_count=24, left_hand=False):

    the_score = stream.Score()

    if left_hand == False:
        right_part = random_part(root_midi, doubled, highest_length, minor, measure_count)
        the_score.insert(0, right_part)
    elif left_hand == True:
        right_part = random_part(root_midi, doubled, highest_length, minor, measure_count)
        left_part = random_part(root_midi - 24, doubled, highest_length, minor, measure_count)
        the_score.insert(0, right_part)
        the_score.insert(0, left_part)

    return the_score


def random_part(root_midi, doubled=False, highest_length=4.0, minor=False, measure_count=24):

    counter = 0
    the_part = stream.Part()
    while counter < measure_count:
        the_measure = random_measure(root_midi, doubled, highest_length, minor)
        the_part.append(the_measure)
        counter += 1

    return the_part


def random_measure(root_midi, doubled=False, highest_length=4.0, minor=False):

    is_full = False
    the_measure = stream.Measure()
    
    while not is_full:
        reroll = True
        while reroll:
            the_note = random_note(root_midi, doubled, highest_length, minor)
            if will_measure_overflow(the_measure, the_note):
                the_measure.clear()
            else:
                the_measure.append(the_note)
                reroll = False 
        is_full = is_measure_full(the_measure)

    return the_measure

def will_measure_overflow(the_measure, incoming_note):

    if not len(the_measure) == 0:
        max_offset = 4.0
        incoming_quarter_length = incoming_note.quarterLength
        most_recent_offset = the_measure[-1].offset

        will_overflow = True if (most_recent_offset + incoming_quarter_length > max_offset) else False

        return will_overflow
    
    else:
        return False

def is_measure_full(the_measure):

    offset_sum = 0
    for each_note in the_measure:
        offset_sum += each_note.quarterLength

    if offset_sum == 4.0:
        return True
    else:
        return False

test_score = random_score(71, doubled=True, highest_length=4.0, minor=True, measure_count=120,left_hand=True)
test_score.show()
