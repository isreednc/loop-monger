import pyaudio
import mixer

def main():
    p = pyaudio.PyAudio()

    print_host_apis(p)

    # mixer.print_devices(p)

def print_host_apis(paudio):
    num_host_apis = paudio.get_host_api_count()

    for i in range(num_host_apis):
        host_api_info = paudio.get_host_api_info_by_index(i)
        print(f"Host API {i}:")
        print(f"  Name: {host_api_info['name']}")
        print(f"  Type: {host_api_info['type']}")
        print(f"  Device Count: {host_api_info['deviceCount']}")
        print(f"  Default Input Device: {host_api_info['defaultInputDevice']}")
        print(f"  Default Output Device: {host_api_info['defaultOutputDevice']}")
        print(f"Devices:")
        for j in range(host_api_info['deviceCount']):
            device_info = paudio.get_device_info_by_host_api_device_index(i, j)
            print(f"    Device {device_info['index']}:")
            print(f"      Name: {device_info['name']}")
            print(f"      Max Input Channels: {device_info['maxInputChannels']}")
            print(f"      Max Output Channels: {device_info['maxOutputChannels']}")
            print(f"      Default Sample Rate: {device_info['defaultSampleRate']}")
            print()

if __name__ == "__main__":
    main()