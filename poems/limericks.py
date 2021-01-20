import json
import random

def remove_short_lines(syllable_lookup, min_length=3):
    for syllable_count in list(syllable_lookup.keys()):
        by_syllable = syllable_lookup[syllable_count]
        for key in list(by_syllable.keys()):
            if len(by_syllable[key]) < min_length:
                del by_syllable[key]
    return syllable_lookup

def limerick(syllable_lookup):
    a_ending_syllables = random.choice(list(syllable_lookup[8].keys()))
    b_ending_syllables = random.choice(list(syllable_lookup[5].keys()))
    a_phrases = random.sample(syllable_lookup[8][a_ending_syllables],3)
    b_phrases = random.sample(syllable_lookup[5][b_ending_syllables],2)
    phrases = [a_phrases[0], a_phrases[1], b_phrases[0], b_phrases[1], a_phrases[2]]
    return "\n".join(phrases)


    

