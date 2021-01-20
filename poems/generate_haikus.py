import json
from generate_syllable_rhyme_lookup import generate_syllable_rhyme_lookup_from_file
import haikus

source_message_filename = 'fake_messages_with_known_words.json'
outfilename = "fake_haikus.json"
amount_to_generate = 100

results = []

syllable_lookup = generate_syllable_rhyme_lookup_from_file(source_message_filename)
for i in range(0, amount_to_generate):
    results.append(haikus.haiku(syllable_lookup))

open(outfilename,'w').write(json.dumps(results))

