import sys
import os
import pyaudio

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import mixer

def test_get_input_device():
    output_device = "CABLE Input (VB-Audio Virtual"

    # Modify as needed
    expected_index = 21

    p = pyaudio.PyAudio()

    assert mixer.get_input_device(p, output_device) == expected_index

    

