import json
import limericks
from generate_syllable_rhyme_lookup import generate_syllable_rhyme_lookup_from_file

source_message_filename = 'fake_messages_with_known_words.json'
outfile = "fake_limericks.json"
count = 100

syllable_lookup = generate_syllable_rhyme_lookup_from_file(source_message_filename)
syllable_lookup = limericks.remove_short_lines(syllable_lookup)
results = []
for i in range(0, count):
    results.append(limericks.limerick(syllable_lookup))

open(outfile,'w').write(json.dumps(results))