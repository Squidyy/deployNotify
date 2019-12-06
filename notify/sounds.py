import os


def play_sound(file_name):
    """
    call `ffplay` on given file
    TODO: load dynamic path
    TODO: load remote sound file

    Parameters
    ----------
    file_name : str
        name (with extension) of file to play
    """
    file_path = f'assets/sounds/{file_name}'
    os.system(f'ffplay -nodisp -autoexit {file_path} >/dev/null 2>&1')
