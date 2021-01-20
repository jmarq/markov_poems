# import syllables
import json
import random

# fakes = json.load(open('fake_messages_with_known_words.json', 'r'))


# by_count = {}

# eight_by_last_2_syllables = {}
# five_by_last_2_syllables = {}
# for fake in fakes:
#     if not fake:
#         continue
#     count = syllables.sentence_syllables(fake)
#     last_2_syllables = "+".join(syllables.vowel_phones_for_last_n_syllables(fake,2))

#     if(count == 8):
#         if last_2_syllables in eight_by_last_2_syllables:
#             eight_by_last_2_syllables[last_2_syllables].append(fake)
#         else:
#             eight_by_last_2_syllables[last_2_syllables] = [fake]
#     if(count == 5):
#         if last_2_syllables in five_by_last_2_syllables:
#             five_by_last_2_syllables[last_2_syllables].append(fake)
#         else:
#             five_by_last_2_syllables[last_2_syllables] = [fake]


# remove lines that are less than 3 words

def remove_short_lines(syllable_lookup, min_length=3):
    for syllable_count in list(syllable_lookup.keys()):
        by_syllable = syllable_lookup[syllable_count]
        for key in list(by_syllable.keys()):
            if len(by_syllable[key]) < min_length:
                del by_syllable[key]
    return syllable_lookup

# for key in five_by_last_2_syllables.keys():
#     if len(five_by_last_2_syllables[key]) < 3:
#         del five_by_last_2_syllables[key]




def limerick(syllable_lookup):
    a_ending_syllables = random.choice(list(syllable_lookup[8].keys()))
    b_ending_syllables = random.choice(list(syllable_lookup[5].keys()))
    a_phrases = random.sample(syllable_lookup[8][a_ending_syllables],3)
    b_phrases = random.sample(syllable_lookup[5][b_ending_syllables],2)
    phrases = [a_phrases[0], a_phrases[1], b_phrases[0], b_phrases[1], a_phrases[2]]
    return "\n".join(phrases)


    

