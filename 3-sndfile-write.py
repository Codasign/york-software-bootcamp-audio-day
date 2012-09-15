from scikits.audiolab import Sndfile
from scikits.audiolab import Format
from scikits.audiolab import play

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

# extract and print the encoding format
enc = f.encoding
print "encoding format: ",enc

# extract the number of frames - single samples for
# mono and pairs of samples for stereo
num_samples = f.nframes


#################################################
######## READ AUDIO SAMPLES FROM THE FILE #######
#################################################

# we can read audio samples using the read_frame method
samples = f.read_frames(num_samples)


#################################################
########## WRITING TO A NEW AUDIO FILE ##########
#################################################

# create a name for the new file
new_filename = 'output_file.wav'

# create the output audio data, in this case a simple copy
output_samples = samples

# Create a Sndfile instance for writing wav files @ 44100 Hz
format = Format('wav')
f = Sndfile(new_filename, 'w', format, 1, 44100)

# Write out the first 3 seconds worth of samples (fs*3)
f.write_frames(output_samples)

# close the audio file
f.close()

#################################################
#################################################
#################################################
