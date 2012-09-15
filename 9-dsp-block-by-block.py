import numpy as np
import pylab as plt
from scikits.audiolab import wavread

#################################################
############ EXTRACT AUDIO FROM FILE ############
#################################################

x, fs, enc = wavread("viola.wav")


#################################################
####### CALCULATE RMS OF EACH AUDIO BLOCK #######
#################################################

hop_size = 512                             # set hop size
frame_size = hop_size*2                     # set frame size
frame = np.zeros(frame_size)                # initialise frame with zeros
window = np.hanning(frame_size)             # create window of the same length as the hop size

# create empty numpy array to hold our 
rms = np.array([])

# run through signal frame by frame 
for n in range(0,x.size-hop_size,hop_size):
    
    # extract a segment of length hop_size
    frame = x[n:n+hop_size]                               
        
    # calculate RMS
    rms_val = np.sqrt(np.power(frame,2).mean())
    
    # add amplitude to our numpy array
    rms = np.append(rms,rms_val)

print rms

""" I AM THE OVERLAP VERSION
# run through signal frame by frame 
for n in range(0,x.size-hop_size,hop_size):
    
    # extract a segment of length hop_size
    buffer = x[n:n+hop_size]                               
    
    # add new segment to frame, shifting back samples of frame
    frame = np.append(frame[hop_size:frame_size],buffer)  
    
    # calculate RMS
    rms_val = np.sqrt(np.power(frame,2).mean())
    
    # add amplitude to our numpy array
    rms = np.append(rms,rms_val)

print rms
"""

plt.plot(rms)
plt.title("RMS")
plt.xlabel("time")
plt.ylabel("value")
plt.show()
                                   
 