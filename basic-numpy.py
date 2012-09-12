import numpy as np


#################################################
############# NUMPY ARRAYS FOR AUDIO? ###########
#################################################

# I am a numpy array containing some audio
myAudio = np.array([-0.25,0.0,0.25,0.5])

# turn it up!
myAudio = myAudio*2.

# great!
print myAudio


# what can we find out about our numpy audio?


print "Dimensions: ",myAudio.ndim

print "Size of each dimension: ",myAudio.shape

print "Total number of elements: ", myAudio.size # this is product of shape dimensions

print "Data type: ",myAudio.dtype # ...or dtype.name

print "Bytes per element: ",myAudio.itemsize 

print "Second element: ",myAudio[1]

print "All elements up to (but not including) 2: ",myAudio[:2]

print "All elements from index 2 to end: ",myAudio[2:]

print "Abs!: ",np.abs(myAudio)

print "Min: ",np.min(myAudio)

print "Max: ",np.max(myAudio)

print "Sum: ",np.sum(myAudio)

print "Sqrt: ",np.sqrt(9)

print "FFT!: ",np.fft.fft(myAudio)

print "Random!: ",np.random.random(4)

print "Ones: ",np.ones(4)

print "Zeros: ",np.zeros(4)
