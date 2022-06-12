# %%

import json
from os.path import join

# %%

fnin = join('..', 'data', 'captioned', 'meta_raw.json')

fnout = join('..', 'data', 'captioned', 'meta_clean.json')

rep = [
    ('\u00b0', ''),
    ('\u00a0', ' '),
    ('\n\r\n', ' '),
    ('\n\n', ' '),
    ('\n\r', ' '),
    ('\n', ' '),
    ('\u201c', ''),
    ('\u201d', ''),
    ('\u2019', "'"),
    ('\u0092', "'"),
    ('\u0093', ''),
    ('\u0094', ''),
    ('\u2014', ', '),
    ('\u0097', ', '),
    ('\u2013', '-'),
    ('\u2018', "'"),
    ('\u00e8', 'e'),
    ('\u00e9', 'e'),
    ('\u009d', ''),
    ('\u0096',', '),
    ('\u00e2', ''),
    ('\u0080', ''),
    ('\u0099', "'"),
    ('\u0091', "'"),
    ('\u00edmsv\u00f6', 'imsvo'),
    ('\"', ''),
    ('  ', ' ')
]
# %%

with open(fnin, 'r') as ifile:
    meta = json.load(ifile)

for k in meta:
    d = meta[k]
    for h in d:
        s = d[h]
        for (a,b) in rep:
            s = s.replace(a,b)
        d[h] = bytes(s, 'utf-8').decode('utf-8', 'igore')

with open(fnout, 'w') as ofile:
    json.dump(meta, ofile, ensure_ascii=True, indent=True)
# %%
