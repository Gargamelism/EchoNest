import numpy
import simpleaudio
import time

import helpers.input_helper as input_helper


def librosa_to_audio_buffer(librosa_loaded):
    return (librosa_loaded * 32767).astype(numpy.int16)


def play_audio_file(librosa_audio_file, sample_rate, duration=None):
    audio_buffer = librosa_to_audio_buffer(librosa_audio_file)
    player = simpleaudio.play_buffer(audio_buffer, 1, 2, sample_rate)

    stop_playing = False
    while not stop_playing and player.is_playing():
        time.sleep(0.1)
        stop_playing = input_helper.input_with_timeout("Press 's' to skip playing", timeout=duration) == "s"
    player.stop()

    print("Finished playing audio")
