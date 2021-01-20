# takes a newline separated list of phrases (corpus_filename)
# generates markov chain
# spits out a given number of "fake" messages generated with the chain
# output comes in the form of a json file (output_filename)

import markovify
import json

corpus_filename = "content.txt"
output_filename = 'fake_messages.json'


def write_fakes_to_file(filename, count, word_limit=False):
  fake_messages = []
  outfile = open(filename, 'w');
  for i in range(count):
    # report progress every 100 messages
    if i % 100 == 0:
      print(i)
    done = False
    message = ""
    while not done:
      message = text_model.make_sentence()
      if not word_limit:
        done = True
        break
      else:
        new_message_length = len(message.split())
        if message and new_message_length <= word_limit and new_message_length > 0:
          done = True
    fake_messages.append(message)
  json_string = json.dumps(fake_messages)
  outfile.write(json_string)
  outfile.close()
  print("Finished generating messages")


if __name__ == "__main__":
  # read in newline separated training messages
  with open(corpus_filename) as f:
    text = f.read()
  # Build the model based on those messages
  text_model = markovify.NewlineText(text)
  write_fakes_to_file(output_filename, 500, 10)