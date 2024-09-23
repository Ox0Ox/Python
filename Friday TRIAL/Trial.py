from pocketsphinx import LiveSpeech
hmm = 'en-us'
lm = 'en-us.lm.bin'
dict = 'cmudict-en-us.dict'
for phrase in LiveSpeech(): print(phrase)