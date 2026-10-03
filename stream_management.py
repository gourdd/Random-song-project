from music21 import *
from random_notes import *

# Methods that manage measure separation and stream offsets
# Create combinations of measures, add the quarter lengths up to see if they equal a clean 4.0
# If they don't, reroll.

def random_measure(root_midi, doubled=False, highest_length=4.0, minor=False):

    max_offset = 4.0
    length_check = 0
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

        # measure_space_left = max_offset - most_recent_offset
        # print("last note offset: " + str(the_measure[-1].offset))
        # print("incoming ql: "+ str(incoming_quarter_length))
        # print("space left: " +str(measure_space_left))
        # print("subtracted: " + str(incoming_quarter_length + measure_space_left))

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

test_score = stream.Score()

for i in range(20):
    test_score.append(random_measure(60, doubled=True, highest_length=0.25))

for one_note in test_score[0]:
    print(one_note.duration.type)

test_score.show()
