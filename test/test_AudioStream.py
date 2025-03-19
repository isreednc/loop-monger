import os
import sys
import pyaudio

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from audio import AudioStream

def test_create_audio_stream():
    audio_stream = AudioStream()
    assert isinstance(audio_stream, AudioStream)
    audio_stream.close()

def test_get_api_info():
    audio_stream = AudioStream()
    api = 'MME'
    api_info, api_index = audio_stream.get_api_info(api)
    assert(api_info is not None)
    assert(api_index >= 0)
    audio_stream.close()

def test_get_output_index():
    output_string = "CABLE Input (VB-Audio Virtual"
    audio_stream = AudioStream()
    api = 'MME'
    output_index = audio_stream.get_output_index(api, output_string)
    assert(output_index >= 0)
    audio_stream.close()

def test_open_stream():
    output_string = "CABLE Input (VB-Audio Virtual"
    audio_stream = AudioStream()
    api = 'MME'
    audio_stream.open_stream(api, output_string)
    assert(audio_stream is not None)
    assert isinstance(audio_stream.stream, pyaudio.PyAudio.Stream)
    audio_stream.close()

def test_play_wav():
    output_string = "CABLE Input (VB-Audio Virtual"
    wf = './test/test_sounds/monobang.wav'
    audio_stream = AudioStream()
    api = 'MME'
    audio_stream.open_stream(api, output_string)   
    audio_stream.play_wav(wf)
    audio_stream.close()

    

    


 