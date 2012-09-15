import numpy as np
import pylab as plt
from scikits.audiolab import Sndfile
from scikits.audiolab import Format


#################################################
############## CREATE A SINE TONE ###############
#################################################

# set our sampling frequency
fs = 44100

# create a numpy array that can hold 3 seconds of sound
tone = np.zeros((3*fs,2))

# set frequency to 440Hz
freq = 440

# set volume to 0.3
amp = 0.3

# set values of each channel
for i in range(tone.shape[0]):
    
    # calculate phase value
    phaseVal = np.float(i)/np.float(fs)
    
    # generate tone and set volume for left and right
    tone[i][0] = np.sin(2*np.pi*freq*phaseVal)*amp
    tone[i][1] = np.sin(2*np.pi*(freq*2)*phaseVal)*amp


#################################################
########## WRITING TONES TO AUDIO FILE ##########
#################################################

# create a name for the new file
new_filename = 'tone.wav'

# Create a Sndfile instance for writing wav files @ 44100 Hz
format = Format('wav')
f = Sndfile(new_filename, 'w', format, 2, fs)

# Write out the samples to the file
f.write_frames(tone)

# close the audio file
f.close()


#################################################
############### PLOT USING PYLAB ################
#################################################   

toneL = tone[:,0]
toneR = tone[:,1]

plt.subplot(211)
plt.plot(toneL[0:200])
plt.subplot(212)
plt.plot(toneR[0:200])
plt.show()
