import librosa
import librosa.display as display
import matplotlib.pyplot as pyplot
import numpy
import time
import simpleaudio
import random

import helpers.audio_helper as audio_helper


def run_mono_audio():
    ## mono file
    nutcracker, nutcracker_sample_rate = librosa.load(librosa.ex("nutcracker"), duration=60)

    print("Playing the Nutcracker")
    audio_helper.play_audio_file(nutcracker, nutcracker_sample_rate, 60)

    print("Playing the Nutcracker at double the sample rate")
    audio_helper.play_audio_file(nutcracker, nutcracker_sample_rate * 2, 30)

    print(f"Total number of samples: {nutcracker.shape[0]}")
    print(f"Sample rate: {nutcracker_sample_rate}")
    print(f"Duration in seconds: {librosa.get_duration(y=nutcracker, sr=nutcracker_sample_rate)}")

    pyplot.title("Waveform of the Nutcracker")
    pyplot.plot(nutcracker)
    pyplot.show()

    pyplot.title("Waveform of the Nutcracker (Zoomed in)")
    pyplot.plot(nutcracker[21000:22000])
    pyplot.show()

    # spectrogram
    nutcracker_stft = librosa.stft(nutcracker)
    nutcracker_stft_db = librosa.amplitude_to_db(numpy.abs(nutcracker_stft), ref=numpy.max)
    display.specshow(nutcracker_stft_db)
    pyplot.title("Spectrogram of the Nutcracker")
    pyplot.show()

    # log-frequency power spectrogram
    pyplot.figure(figsize=(10, 5))
    display.specshow(nutcracker_stft_db, sr=nutcracker_sample_rate, x_axis="time", y_axis="log")
    pyplot.colorbar(format="%+2.0f dB")
    pyplot.title("Log-frequency power spectrogram")
    pyplot.show()

    # mel spectrogram
    # calculate the mel spectrogram
    mel_spectrogram = librosa.feature.melspectrogram(y=nutcracker, sr=nutcracker_sample_rate)
    mel_spectrogram_db = librosa.power_to_db(mel_spectrogram, ref=numpy.max)
    # display the mel spectrogram
    pyplot.figure(figsize=(10, 5))
    display.specshow(mel_spectrogram_db, x_axis="time", y_axis="mel", sr=nutcracker_sample_rate)
    pyplot.colorbar(format="%+2.0f dB")
    pyplot.title("Mel spectrogram")
    pyplot.show()


def run_stereo_audio():
    audio_options = ["brahms", "choice", "fishin", "humpback", "libri1"]
    audio_choice = random.choice(audio_options)
    chosen_audio, chosen_audio_sample_rate = librosa.load(librosa.ex(audio_choice), mono=False, duration=60)
    audio_helper.play_audio_file(chosen_audio, chosen_audio_sample_rate, 60)

    chosen_audio_stft = librosa.stft(chosen_audio)
    chosen_audio_stft_db = librosa.amplitude_to_db(numpy.abs(chosen_audio_stft), ref=numpy.max)

    fig, ax = pyplot.subplots(2, 1, figsize=(10, 10), sharex=True)
    chosen_audio_linear_spectrogram = librosa.display.specshow(
        chosen_audio_stft_db, sr=chosen_audio_sample_rate, x_axis="s", y_axis="linear", ax=ax[0]
    )
    ax[0].set(title="Linear-frequency power spectrogram")
    ax[0].label_outer()

    display.specshow(chosen_audio_stft_db, sr=chosen_audio_sample_rate, x_axis="s", y_axis="log", ax=ax[1])
    ax[1].set(title="Log-frequency power spectrogram")
    ax[1].label_outer()
    fig.colorbar(chosen_audio_linear_spectrogram, ax=ax, format="%+2.0f dB")
    pyplot.show()


def main():
    run_mono_audio()
    run_stereo_audio()

    print("Completed Lesson 1")
