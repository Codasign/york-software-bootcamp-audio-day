import os
from scikits.audiolab import Sndfile
from scikits.audiolab import Format

# get the current working directory
path = os.getcwd()

# get all file names in the current directory
files = os.listdir(path)

# for each file name
for filename in files:
    
    # if the file ends with a .wav extension
    if filename.endswith('.wav'):
        
        # create a Sndfile instance for the file
        f_in = Sndfile(filename, 'r')
        
        # extract the number of frames
        numframes = f_in.nframes

        # read all audio samples into 'data'
        data = f_in.read_frames(numframes)

        # extract the name (without extension from the file name)
        name,extension = os.path.splitext(filename)

        # create a new filename with a .aiff extension
        new_filename = name + '.aiff'

        # create the new format based on aiff
        format = Format('aiff')
        
        # create a new Sndfile instance for the output file
        f_out = Sndfile(new_filename, 'w', format, f_in.channels, f_in.samplerate)

        # write out audio samples to the new file
        f_out.write_frames(data[:numframes])

        # close the audio file
        f_out.close()

        
