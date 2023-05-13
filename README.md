# Installation
pip install -r requirements.txt

# Usage
- Parameters can be randomly generalized according to children speech statistics
python childrenize.py <input audo> <output audio>

- Parameters can be also specified
python childrenize.py -f 300 <input audo> <output audio>

Above command will specify a target F0 of 300 Hz, meanwhile keeping spectral warping factor and vowel stretching factor randomized.
