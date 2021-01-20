# fun with markov chains and chat messages

currently configured to use a newline-separated list of training messages. by default, the scripts look for this file called "content.txt" in the root of this project.

the scripts contain variables that can be changed to look for this file elsewhere.

scripts exist to:

- generate fake messages based on patterns in the training set
- generate fake messages that contain only words known to a pronunciation tool.
- use messages with known words to generate syllable/rhyme structures like limericks and haikus
- bring a smile to your face


primary dependencies of these scripts are `pronouncing` and `markovify`. Developed and tested using python3.7

perhaps make a virtualenv and pip install using the provided requirements.txt
