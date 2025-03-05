import pyaudio
import wave

OUTPUT_DEVICE = "CABLE Input (VB-Audio Virtual"
PREFERRED_HOST_API_NAME = 'MME'

def get_api_info(p: pyaudio.PyAudio):
    api_info, api_index = None, 0
    for i in range(p.get_host_api_count()):
        current_api_info = p.get_host_api_info_by_index(i)
        if i == 0:
            api_info = current_api_info
        else:
            if current_api_info['name'] == PREFERRED_HOST_API_NAME:
                api_info, api_index = current_api_info, i
                break
    return api_info, api_index

def main():
    # file = "../sounds/boom48khz.wav"  # 48000
    file = "../sounds/monobang.wav" # 44100
    p = pyaudio.PyAudio()

    play_wav(p, file, OUTPUT_DEVICE)

    return 0

def play_wav(player, file_path, output):
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

    chunk_size = 512  # Number of frames per buffer 

    p = player
    device_index = get_input_device(p, output)
    
    # testing with a known device that works for me
    # device_index = 18

    # headphones, so the user can also hear the file
    headphone_index = 11

    print(device_index)

    print(wf.getnchannels())

    print(wf.getsampwidth())

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
            # headphone_output_stream.write(data)
            data = wf.readframes(chunk_size)
    except Exception as e:
        print(f"An error occurred during playback: {e}")
    finally:
        # Stop and close the stream
        output_stream.stop_stream()
        output_stream.close()
        p.terminate()
        wf.close()
    
# for analyzing all the devices available to pyaudio
def print_devices(paudio):
    # for i in range(paudio.get_device_count()):
    #     info = paudio.get_device_info_by_index(i)
    #     print(f"Device {info['index']}: {info['name']} (Input Channels: {info['maxInputChannels']}, Output Channels: {info['maxOutputChannels']})")

    api_info, api_index = get_api_info(paudio)
    print(api_info)
    api_name = api_info['name']
    if api_name != PREFERRED_HOST_API_NAME:
        print(f'[WARNING] "{PREFERRED_HOST_API_NAME}" not available on this system, '
            f'going with "{api_name}" instead')

    numdevices = api_info.get('deviceCount')
    for i in range(numdevices):
        dev_info = paudio.get_device_info_by_host_api_device_index(api_index, i)
        # if dev_info.get('maxOutputChannels') == 0:
        #     continue
        print("Output Device id ", dev_info.get('index'), " - ", dev_info.get('name'), " - ", api_name)
        # print(dev_info)

def get_input_device(paudio, device_name):
    device_index = -1

    # for i in range(paudio.get_device_count()):
    #     info = paudio.get_device_info_by_index(i)
    #     if device_name in info['name']:
    #         device_index = info['index']

    api_info, api_index = get_api_info(paudio)
    api_name = api_info['name']
    if api_name != PREFERRED_HOST_API_NAME:
        print(f'[WARNING] "{PREFERRED_HOST_API_NAME}" not available on this system, '
            f'going with "{api_name}" instead')

    numdevices = api_info.get('deviceCount')
    for i in range(numdevices):
        dev_info = paudio.get_device_info_by_host_api_device_index(api_index, i)
        dev_id = dev_info.get('index')
        dev_name = dev_info.get('name')
        if dev_info.get('maxOutputChannels') == 0:
            continue
        # print("Output Device id ", dev_id, " - ", dev_name)
        if device_name in dev_name:
            device_index = dev_id

    print(device_index)
    return device_index

if __name__ =="__main__":
    main()
