# ExtensionAdder
Got some files without extensions? ExtensionAdder will add extensions to their names. Just like that

### hOI!
One day I decided to bulk rename some of my files and I screwed up.

They got renamed to numbers 1 through 150 without keeping their extensions.

I could have spent 20 minutes renaming them one by one, but I decided to spend 2 hours to write this, since I didn't find anything with this functionality.

### Good things to know
+ I have no idea which extensions YOU need. If you need something - feel free to look up the mime type and add a mime:extension pair in the dictionary. How? Same as everything else, just use your brain. Just a bit.
+ This tool doesn't touch any files with extensions.

### Dependencies
+ Python (I use 3.6.something)
+ python-magic from pip (I use 0.4.16)

### How to install
Come on, you know the drill

First you install `python-magic`

`pip3 install python-magic`

Thn you clone this repository

`git clone https://github.com/kotek14/extensionadder`

### How to run
`./extensionadder.py <name_of_your_file>`

You can also use wildcards.
