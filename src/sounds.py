import os

base_dir = os.path.dirname(os.path.abspath(__file__))
sounds_dir = os.path.join(base_dir, 'sounds')

sounds = []

def get_sounds():
    for sound in os.listdir(sounds_dir):
        if sound.endswith('.wav'):
            sounds.append(sound)
    return sounds

if __name__ == "__main__":
    print(get_sounds())