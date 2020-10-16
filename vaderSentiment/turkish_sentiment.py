import pandas as pd
import json
import string
import time
from tqdm import tqdm
vader_lexicon = pd.read_csv('vader_lexicon.txt', sep='\t', header=None)
#turkishlanguagevader_lexicon = []
#vader_lexicon