#!/usr/bin/env python3

textfile = "sample.txt"
fw = open(textfile, "w")
fw.write("""
Tomorrow, and tomorrow, and tomorrow,
Creeps in this petty pace from day to day,
To the last syllable of recorded time;
And all our yesterdays have lighted fools
The way to dusty death. Out, out, brief candle!
Life's but a walking shadow, a poor player,
That struts and frets his hour upon the stage,
And then is heard no more. It is a tale
Told by an idiot, full of sound and fury,
Signifying nothing.
""")
fw.close()

count = 0
fr = open(textfile, "r")
data = fr.read().replace(" ", "")
for char in data: 
    count += 1
print("There are " + str(count) + " characters in " + textfile)
