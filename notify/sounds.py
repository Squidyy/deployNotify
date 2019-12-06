import os


# play sound
def play_sound(sound_file):
    file_path = f'assets/sounds/{sound_file}'
    os.system(f'ffplay -nodisp -autoexit {file_path} >/dev/null 2>&1')
