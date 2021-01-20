import random

# pass in a syllable/rhyme lookup dictionary like the one provided by generate_syllable_rhyme_lookup.py
def haiku(syllable_lookup):
    first_line_rhyming = random.choice(list(syllable_lookup[5].keys()))
    second_line_rhyming = random.choice(list(syllable_lookup[7].keys()))
    third_line_rhyming = random.choice(list(syllable_lookup[5].keys()))
    return random.choice(syllable_lookup[5][first_line_rhyming])+"\n"+random.choice(syllable_lookup[7][second_line_rhyming])+"\n"+random.choice(syllable_lookup[5][third_line_rhyming])



