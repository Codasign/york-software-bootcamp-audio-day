import numpy as np
from scikits.audiolab import wavread
from scikits.audiolab import Format
from scikits.audiolab import Sndfile

#################################################
######## CREATING A SOUND FILE INSTANCE #########
#################################################

# extract audio from file
samples, fs, enc = wavread('viola.wav')  

#################################################
########## APPLY A DELAY TO THE SAMPLES #########
#################################################

# delay in samples
delay = fs/2

# volume of delayed sound
alpha = 0.75

# create an empty array for the output
out = np.zeros(samples.size)

# for every sample in the array
for i in range(samples.size):

    # if we are safe to apply the delay without negative indexing
    if (i >= delay):
        out[i] = samples[i] + samples[i-delay]*alpha
    else:
        out[i] = samples[i] # hacky


#################################################
########## WRITING TO A NEW AUDIO FILE ##########
#################################################

# create a name for the new file
new_filename = 'delayed_audio.wav'

# Create a Sndfile instance for writing wav files @ 44100 Hz
format = Format('wav')
f = Sndfile(new_filename, 'w', format, 1, 44100)

# Write out the samples to an audio file
f.write_frames(out)

# close the audio file
f.close()

#################################################
#################################################
#################################################
