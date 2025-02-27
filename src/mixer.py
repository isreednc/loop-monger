import pyaudio
import wave

OUTPUT_DEVICE = "Voicemeeter Input (VB-Audio Voicemeeter VAIO)"

def main():
    file = "../sounds/Boom.wav"
    play_wav(file, OUTPUT_DEVICE)

    # p = pyaudio.PyAudio()
    # print_devices(p)

    return 0

def play_wav(file_path, output):
    try:
        wf = wave.open(file_path, 'rb')
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except wave.Error as e:
        print(f"Error: Could not open the WAV file. {e}")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # sample_rate = 44100  # Sample rate
    chunk_size = 1024  # Number of frames per buffer 

    p = pyaudio.PyAudio()
    device_index = get_input_device(p, output)
    device_index = 18

    # headphones
    headphone_index = 11

    print(device_index)

    print(wf.getframerate())
    
    try:
        output_stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True,
                            output_device_index=device_index)

        headphone_output_stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate=wf.getframerate(),
                            output=True,
                            output_device_index=headphone_index)

        print(output_stream)

        data = wf.readframes(chunk_size)

        while data:
            output_stream.write(data)
            headphone_output_stream.write(data)
            data = wf.readframes(chunk_size)
    except Exception as e:
        print(f"An error occurred during playback: {e}")
    finally:
        # Stop and close the stream
        output_stream.stop_stream()
        output_stream.close()
        p.terminate()
        wf.close()
    
def print_devices(paudio):
    for i in range(paudio.get_device_count()):
        info = paudio.get_device_info_by_index(i)
        print(f"Device {info['index']}: {info['name']} (Input Channels: {info['maxInputChannels']}, Output Channels: {info['maxOutputChannels']})")

def get_input_device(paudio, device_name):
    device_index = -1

    for i in range(paudio.get_device_count()):
        info = paudio.get_device_info_by_index(i)
        if device_name in info['name']:
            device_index = info['index']

    return device_index

if __name__ =="__main__":
    main()
