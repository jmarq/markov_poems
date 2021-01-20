import markovify
import pronouncing
import json

# this file is for generating markov chain messages
#  that only contain words known to the cmu pronunciation dictionary.
#  with such messages, we can gather data about their syllable count and rhymes.
#  these messages are useful for generating random "poems".

training_filename = "../content.txt"
output_filename = 'fake_messages_with_known_words.json'
amount_to_generate = 1000

def fake_is_valid(sentence):
    if not sentence:
        return False
    words = sentence.split()
    if not len(words):
        return False
    return all_words_are_known(words)

# verify that the words are all in pronunciation dictionary
def all_words_are_known(word_list):
    for word in word_list:
        if word not in pronouncing.lookup:
            return False
    return True


def write_fakes_to_file(filename, count):
    fake_messages = []
    outfile = open(filename, 'w')
    i = 0
    while i < count:
        # report progress every so often
        if i > 0 and i % 100 == 0:
            print("done with " + str(i))
        # generate a line
        new_sentence = text_model.make_sentence()
        # check that the message contains known words
        if fake_is_valid(new_sentence):
            i += 1
            fake_messages.append(new_sentence)
    # prepare json structure and save to file
    json_string = json.dumps(fake_messages)
    outfile.write(json_string)
    outfile.close()
    print("Done generating fake messages with known words")

if __name__ == "__main__":
    # initialize the dictionary used to test words
    pronouncing.init_cmu()

    # get training text as newline-separated string
    with open(training_filename) as f:
        text = f.read()

    # build the model using the training text
    text_model = markovify.NewlineText(text)

    # generate and save fake messages to json file
    write_fakes_to_file(output_filename, amount_to_generate)
