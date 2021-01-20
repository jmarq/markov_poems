import syllables
import json

messages_with_known_words_filename = 'fake_messages_with_known_words.json'


def generate_syllable_rhyme_lookup_from_list(messages):
    by_count = {}

    for message in messages:
        if not message:
            continue
        count = syllables.sentence_syllables(message)
        last_2_syllables = "+".join(syllables.vowel_phones_for_last_n_syllables(message,2))
        if count in by_count:
            if last_2_syllables in by_count[count]:
                by_count[count][last_2_syllables].append(message)
            else:
                by_count[count][last_2_syllables] = [message]
        else:
            by_count[count] = {}
            by_count[count][last_2_syllables] = [message]
    return by_count

def generate_syllable_rhyme_lookup_from_file(input_filename=messages_with_known_words_filename):
    messages = json.load(open(input_filename, 'r'))
    return generate_syllable_rhyme_lookup_from_list(messages)