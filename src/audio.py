import os
import sys
import pyaudio
import wave

class AudioStream:
    def __init__(self):
        self.p = pyaudio.PyAudio()
        self.stream = None

    def open_stream(self, output_api, output_string, channels=1, rate=44100, format=pyaudio.paInt16):
        device_index = self.get_output_index(output_api, output_string)

        if self.stream is None:
            self.stream = self.p.open(format=format,
                                      channels=channels,
                                      rate=rate,
                                      output=True,
                                      output_device_index=device_index)

    def play_wav(self, file, chunk_size=512):
        try:
            wf = wave.open(f'./src/sounds/{file}', 'rb')
        except FileNotFoundError as e:
            print(f"Error: The file '{file}' was not found. {e}")
            return
        except wave.Error as e:
            print(f"Error: Could not open the WAV file. {e}")
            return
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return

        data = wf.readframes(chunk_size)

        try:
            print("playing...")
            while data:
                self.stream.write(data)
                data = wf.readframes(chunk_size)
        except Exception as e:
            print(f"An error occurred during playback: {e}")
            return False
        finally:
            wf.close()

        return True

    def close(self):
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()
    
    def get_output_index(self, output_api, output_string):
        device_index = -1

        # for i in range(paudio.get_device_count()):
        #     info = paudio.get_device_info_by_index(i)
        #     if device_name in info['name']:
        #         device_index = info['index']

        api_info, api_index = self.get_api_info(output_api)
        api_name = api_info['name']
        if api_name != output_api:
            print(f'[WARNING] "{output_api}" not available on this system, '
                f'going with "{api_name}" instead')

        numdevices = api_info.get('deviceCount')
        for i in range(numdevices):
            dev_info = self.p.get_device_info_by_host_api_device_index(api_index, i)
            dev_id = dev_info.get('index')
            dev_name = dev_info.get('name')
            if dev_info.get('maxOutputChannels') == 0:
                continue
            # print("Output Device id ", dev_id, " - ", dev_name)
            if output_string in dev_name:
                device_index = dev_id

        print(device_index)
        return device_index

    def get_api_info(self, output_api):
        api_info, api_index = None, -1
        for i in range(self.p.get_host_api_count()):
            current_api_info = self.p.get_host_api_info_by_index(i)
            if current_api_info['name'] == output_api:
                api_info, api_index = current_api_info, i
                break
        return api_info, api_index
    
