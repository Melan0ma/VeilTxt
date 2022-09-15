# VeilTxt
A python based steganographic tool to hide text messages within a .WAV audio file!

EMBEDDING A TEXT MESSAGE TO A .WAV FILE
----------------------------------------
VeilTxt.py --veil --wav="<PATH TO THE .WAV FILE>" --swav="<OUTPUT PATH TO THE NEW .WAV FILE WITH EMBEDDED TEXT MESSAGE>" --message="SECRET MESSAGE GOES HERE!"


READING A HIDDEN TEXT MESSAGE FROM A .WAV FILE
-----------------------------------------------
VeilTxt.py --unveil --wav="<PATH TO THE .WAV FILE WITH HIDDEN TEXT MESSAGE>"



NOTE : Embedding a text message would not affect the audio content of the .WAV file in any way.
