# %%

from os.path import join
import json
from pandas import DataFrame, value_counts
from sklearn.feature_extraction.text import *

# %%

with open(join('..', 'data', 'non-captioned', 'meta_clean.json'), 'r') as ifile:
    meta = json.load(ifile)
meta = DataFrame(meta).T

# %%

clean_word = lambda s: ''.join([x for x in s if x.isalnum()])

clean_string = lambda s: ' '.join([clean_word(x.lower()) for x in s.split()])
# %%

counts = value_counts((' '.join(map(clean_string, meta.title))).split())
# %%
