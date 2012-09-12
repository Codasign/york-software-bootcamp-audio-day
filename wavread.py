from scikits.audiolab import wavread

# specify a file name
filename = "viola3.wav"

# extract audio from file
x, fs, enc = wavread(filename)     

# print out the first 50 samples
print x[0:50]


