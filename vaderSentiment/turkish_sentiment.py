import pandas as pd
import json
import string
import time
from tqdm import tqdm
vader_lexicon = pd.read_csv('vader_lexicon.txt', sep='\t', header=None)
#turkishlanguagevader_lexicon = []
#vader_lexicon
#translation with google 
from googletrans import Translator
translator = Translator()
# translate from English to Turkish
def translate_to_turkish(english_word):
    turkish_word = translator.translate(english_word, src="en", dest="tr")
#    print(f"{english_word}: {turkish_word.text}")
    time.sleep(2)
    return turkish_word
# translate from Turkish to English
def translate_from_turkish(turkish_word):
    english_word = translator.translate(turkish_word, src="tr", dest="en")
#    print(f"{english_word}: {turkish_word.text}")
    time.sleep(2)
    return english_word
# skip translation for punctuations and numbers
#print(string.punctuation)
#print(string.digits)
try:
    english_turkish_cache = json.load(open("english_turkish_cache.json"))
    turkishlanguagevader_lexicon = pd.read_csv('turkishlanguagevader_lexicon.txt', sep='\t', header=None)
except Exception as e:
    print(e)
    english_turkish_cache = {}
    turkishlanguagevader_lexicon = []
for i, row in tqdm(vader_lexicon.iterrows(), total=len(vader_lexicon)):
    print(type(row))
    row = dict(row)
#    print(type(row))
#    print()
    english_word = row[0].strip()
    if english_word in english_turkish_cache:
        continue
    else:
        try:
            if english_word[0] in string.punctuation or english_word[0] in string.digits:
                continue
            else:     
                turkish_word = translate_to_turkish(english_word) 
                english_turkish_cache[english_word] = turkish_word.text
                if turkish_word is not None:
                    row[0] = turkish_word.text
                    turkishlanguagevader_lexicon.append(row)
        except Exception as err:
            print(err)
json.dump(english_turkish_cache, open("english_turkish_cache.json", "w", encoding='utf8'), ensure_ascii=False)
df_turkish_lexicon = pd.DataFrame(turkishlanguagevader_lexicon)
df_turkish_lexicon.to_csv('turkishlanguagevader_lexicon.txt', sep='\t', index = False, header=False)
# and read back once file exists
#df_turkish_lexicon = pd.read_csv('turkishlanguagevader_lexicon.txt', sep='\t', header=None)
#df_turkish_lexicon
english_turkish_lexicon = []
english_turkish_lexicon = vader_lexicon.append(df_turkish_lexicon, ignore_index=True)
print(english_turkish_lexicon)
print()
print(len(english_turkish_lexicon))
