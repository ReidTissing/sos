import json
import random
import markovify

from pprint import pprint
lyrics = ''
with open('file.json') as f:
    data = json.load(f)

#pprint(data)
for keys,values in data.items():
    lyrics = lyrics + values

# x = random.choice(list(data.values()))
# print(lyrics)
# Print three randomly-generated sentences of no more than 140 characters
# for i in range(3):
#     print(text_model.make_short_sentence(140))
def smithize():
    # Build the model.
    try:
        text_model = markovify.Text(lyrics)
        sents = ""
        #for i in range(3):
        #    print(text_model.make_short_sentence(70))
        # Print five randomly-generated sentences
        #for i in range(2):
        #    sents = sents + " " + text_model.make_sentence()
        sent1 = text_model.make_short_sentence(90)
        for z in range(3):
            sents = sents + "\n" + text_model.make_short_sentence(90)
        #filter(lambda x: x is not None, sents)
        sents = sent1 + '\n' + sents + '\n' + sent1
        sents = sents.lower()

        print("FIRST SENTENCE " + sent1)
        print("ALL SENTS " + sents)
        sents = sents.split('\n')

        #sents = sents.title()
        return sents
    except (TypeError):
        pass
        #return text_model.make_sentence()
print(smithize())
