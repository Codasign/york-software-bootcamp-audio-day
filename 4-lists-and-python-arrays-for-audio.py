import array as array


#################################################
############# PYTHON LISTS FOR AUDIO? ###########
#################################################

# I am a list of audio samples
myAudio = [-0.25,0.0,0.25,0.5]

# turn it up!
myAudio = myAudio*2

# oh dear!
print myAudio

# also, look what got into our array 
myAudio.append("hello!")

# oh dear again! - Python stores type information for every entry? Do we want
# to do that 44100 times a second?
print myAudio


#################################################
############# PYTHON ARRAYS FOR AUDIO? ##########
#################################################

# I am an array of audio samples
myAudio = array.array('d',[-0.25,0.0,0.25,0.5])

# this doesn't work, that's good
# myAudio.append("hello")

# but what about this!
myAudio = myAudio*2

# oh dear oh dear oh dear
print myAudio