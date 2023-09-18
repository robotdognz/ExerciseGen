from itertools import combinations
import random
import re
from enum import Enum

class Instrument(Enum):
    GUITAR = 1
    BASS = 2
    UKULELE = 3

def get_formulas_with_length(n):
    functions = ["1", "2b", "2", "3b", "3", "4", "5b", "5", "6b", "6", "7b", "7"]
    """Get all formulas of a given length 1-12."""
    if n > 12 or n < 1:
        print("Can only make formulas with between 1 and 12 functions.")
        return

    # Keep the first string
    first_string = functions[0]
    
    # Take combinations of the rest
    formulas = [[first_string] + list(comb) for comb in combinations(functions[1:], n-1)]
    return random.choice(formulas)
    
def get_random_key():
    keys = ["Db", "Ab", "Eb", "Bb", "F", "C", "G", "D", "A", "E", "B", "F#/Gb (Evil)"]
    """Return a random key."""
    return random.choice(keys)
    
def get_random_zone():
    zones = ["1-4", "2-5", "3-6", "4-7", "5-8", "6-9", "7-10", "8-11", "9-12", "10-13", "11-14", "12-15"]
    """Return a random zone."""
    return random.choice(zones)
    
def get_random_technique():
    zones = ["Notes", "Root and intervals"]
    """Return a random technique."""
    return random.choice(zones)
    
def reorder_starting_with(value, array):
    if value not in array:
        raise ValueError(f"'{value}' not found in the array")
    
    index = array.index(value)
    
    # Split the array into two parts and recombine
    return array[index:] + array[:index]

def formula_to_notes(key, formula):
    # Get sorted notes
    raw_notes = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
    if "F#" in key or "Gb" in key:
        key = "Gb" # does this do anything funky?
    raw_notes = reorder_starting_with(key, raw_notes)
    
    output_notes = []
    
    # Convert formula to notes
    functions = ["1", "2b", "2", "3b", "3", "4", "5b", "5", "6b", "6", "7b", "7"]
    for function in formula:
        note_index = functions.index(function)
        output_notes.append(raw_notes[note_index])
        
    return output_notes

def note_to_fret(note, string_note):
    raw_notes = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
    raw_notes = reorder_starting_with(string_note, raw_notes)
    fret_number = raw_notes.index(note)
    return fret_number

def fret_to_note(fret, string_note):
    raw_notes = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
    raw_notes = reorder_starting_with(string_note, raw_notes)
    raw_notes += raw_notes
    fret_note = raw_notes[fret]
    return fret_note

def get_first_digit(s):
    match = re.search(r'\d{1,2}', s)  # Matches 1 or 2 digits
    if match:
        return int(match.group())
    return None
    
def position_notes_to_frets(notes, zone, strings):
    start_fret = get_first_digit(zone)
    end_fret = start_fret + 3

    for string_note in strings:
        output_string = " " + string_note + ": "
        current_fret = start_fret
        while current_fret <= end_fret:
            current_note = fret_to_note(current_fret, string_note)
            if current_note in notes:
                output_string = output_string + current_note + " "
            else:
                output_string = output_string + "- "
            current_fret += 1
        print(output_string)

def get_string_notes(instrument):
    gitar_notes = ["E", "B", "G", "D", "A", "E"]
    bass_notes = ["G", "D", "A", "E"]
    ukulele_notes = ["A", "E", "C", "G"]
    if instrument == Instrument.GUITAR:
        return gitar_notes
    elif instrument == Instrument.BASS:
        return bass_notes
    elif instrument == Instrument.UKULELE:
        return ukulele_notes

print("\n...Creating exercise...\n")

# User choices
instrument = Instrument.GUITAR
formula_length = 3

# Generate and print exercise
formula = get_formulas_with_length(formula_length)
key = get_random_key()
zone = get_random_zone()

print(" Formula:   " + ' '.join(formula))
print(" Key:       " + key)
print(" Zone:      " + zone)
print(" Technique: " + get_random_technique())

# Generate and answers
print_answers = input("\nDo you want the answer? (yes/no): ")

if print_answers.lower() == "yes":
    notes = formula_to_notes(key, formula)
    strings = get_string_notes(instrument)

    print("")
    print(" Notes:     " + ' '.join(notes))
    print("")
    print(" Fretboard: ")
    position_notes_to_frets(notes, zone, strings)

print("\n...Exercise complete...")