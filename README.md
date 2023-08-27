# Introduction 
This code repository includes an implementation of voice conversion method to generate childlike speech based on WORLD vocoder. It maps adult speech characteristics into children ones, modifications are made based on a children acoustic study \cite{DBLP:journals/jasa/Lee1999}. The original motivation was data augmentation to improve ASR performance on children speakers. 

## Corresponding paper
```
Data augmentation for children ASR and child-adult speaker classification using voice conversion methods
Zhao S., M. Singh, A. Woubie, R. Karhila
24th INTERSPEECH Conference, Dublin, Ireland, 4593-4597
```

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



