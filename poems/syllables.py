import pronouncing
pronouncing.init_cmu()

def equal_list(l):
    # is every element in the list the same?
    return l.count(l[0]) == len(l)


def strip_punc(s):
    return s.strip(".").strip("?").strip(",").strip("!").strip()


def word_syllables(word):
    word = strip_punc(word.lower())
    if word:
        phones = pronouncing.phones_for_word(word)
        if len(phones):
            count = pronouncing.syllable_count(phones[0])
        else:
            count = 0
        return count
    else:
        return 0


def sentence_syllables(sentence):
    words = sentence.lower().strip().split()
    syllable_counts = [word_syllables(word) for word in words]
    return sum(syllable_counts)


def same_number_of_syllables(sentence_list):
    sentence_list = list(sentence_list)
    syllable_count_list = map(sentence_syllables, sentence_list)
    return equal_list(syllable_count_list)


def phones_for_phrase(phrase):
    words = phrase.lower().strip().split()
    phones_for_words = [pronouncing.phones_for_word(strip_punc(word))[
        0] for word in words]
    joined_phones = " ".join(phones_for_words)
    return joined_phones


def vowel_phones_only(phones_string):
    phones = phones_string.split()
    vowel_phones = filter(lambda p: p[-1].isdigit(), phones)
    return list(vowel_phones)


def vowel_phones_for_phrase(phrase):
    return vowel_phones_only(phones_for_phrase(phrase))


def vowel_phones_for_last_n_syllables(phrase, n):
    return vowel_phones_for_phrase(phrase)[-n:]


def vowel_rhyme(phrase_list, num_syllables=2):
    ending_vowel_phones = map(
        lambda p: vowel_phones_for_last_n_syllables(p, num_syllables), phrase_list)
    return equal_list(ending_vowel_phones)


def rhyme_and_syllables_match(phrase_list, num_syllables=2):
    syllable_counts = map(lambda p: sentence_syllables(p), phrase_list)
    if not equal_list(syllable_counts):
        return False
    return vowel_rhyme(phrase_list, num_syllables)
