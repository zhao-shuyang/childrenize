# Installation
pip install -r requirements.txt

# Usage
- Parameters can be randomly generalized according to children speech statistics:
```
python childrenize.py <input audo> <output audio>
```

- Parameters can be also specified, like follows:
```
python childrenize.py -f 300 <input audo> <output audio>
```
Above command will specify a target F0 of 300 Hz, meanwhile keeping spectral warping factor and vowel stretching factor randomized.

# Example audio files
```
utterance/male.wav: an original male speech
utterance/female.wav: an original female speech
utterance/male.childrenized.wav: Childrenized male speech with randomized parameters
utterance/female.childrenized.wav: Childrenized female speech with randomized parameters
```



