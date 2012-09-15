import numpy as np
from scikits.audiolab import Sndfile
from scikits.audiolab import Format
import pylab as plt


#################################################
############ CREATE SOME RANDOM NOISE ###########
#################################################

# set our sampling frequency
fs = 44100

# create a numpy array that can hold 3 seconds of sound
noise = np.empty(3*fs)

# set each element to a random value (noise)
for i in range(noise.size):
    # generate random value and turn it down!
    noise[i] = np.random.random()*0.2

#################################################
########## WRITING NOISE TO AUDIO FILE ##########
#################################################

# create a name for the new file
new_filename = 'noise.wav'

# Create a Sndfile instance for writing wav files @ 44100 Hz
format = Format('wav')
f = Sndfile(new_filename, 'w', format, 1, fs)

# Write out the samples to the file
f.write_frames(noise)

# close the audio file
f.close()


#################################################
############### PLOTTING THE NOISE ##############
#################################################

plt.plot(noise[0:512])
plt.show()
