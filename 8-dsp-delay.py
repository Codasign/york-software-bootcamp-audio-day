import numpy as np
from scikits.audiolab import Sndfile
from scikits.audiolab import Format

#################################################
######## CREATING A SOUND FILE INSTANCE #########
#################################################

# create Sndfile instance with our example audio file
f = Sndfile('viola.wav', 'r')


#################################################
######## EXTRACTING AUDIO FILE META-DATA ########
#################################################

# extract and print sample rate
fs = f.samplerate
print "sample rate: ",fs

# extract and print the number of channels
nc = f.channels
print "number of channels: ",nc

# extract the number of samples
nsamples = f.nframes


#################################################
######## READ AUDIO SAMPLES FROM THE FILE #######
#################################################

# we can read audio samples using the read_frame method
data = f.read_frames(nsamples)


#################################################
########## APPLY A DELAY TO THE SAMPLES #########
#################################################

# delay in samples
delay = fs/2

# volume of delayed sound
alpha = 0.75

# create an empty array for the output
out = np.zeros(data.size)

# for every sample in the array
for i in range(data.size):

    # if we are safe to apply the delay without negative indexing
    if (i >= delay):
        out[i] = data[i] + data[i-delay]*alpha
    else:
        out[i] = data[i] # hacky


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
