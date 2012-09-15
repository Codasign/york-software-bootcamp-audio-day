from scikits.audiolab import wavread
from scikits.audiolab import play

# specify a file name
filename = "viola.wav"

# extract audio from file
samples, fs, enc = wavread(filename)     

# print out the first 50 samples
print samples[0:50]


#################################################
############# PLAYING AN AUDIO FILE #############
#################################################

# play the audio file data in 'data' at 44100Hz
play(samples,fs=44100)


#################################################
#################################################
#################################################