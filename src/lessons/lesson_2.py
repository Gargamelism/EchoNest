import matplotlib.pyplot as pyplot
import numpy
import scipy.io.wavfile as wavfile
import os
from pprint import pprint

import helpers.audio_helper as audio_helper


def main():
    # create_a_simple_waveform()
    # read_audio_to_computer()
    # synthesize_flute_waveform()
    adding_waves_together()

    print("Completed Lesson 2")


def setup_graph(title="", x_label="", y_label="", fig_size=None):
    fig = pyplot.figure()
    if fig_size:
        fig.set_size_inches(fig_size[0], fig_size[1])
    ax = fig.add_subplot(111)  # 1x1 grid, first subplot
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)


def create_a_simple_waveform():
    frequency = 6
    amplitude = 1.7
    length_in_seconds = 2
    sample_rate = 30
    num_samples = sample_rate * length_in_seconds

    signal_base = numpy.linspace(0, length_in_seconds, num_samples)
    pprint(signal_base)
    signal = [amplitude * numpy.sin(2 * numpy.pi * frequency * i) for i in signal_base]

    setup_graph("time domain", x_label="time (s)", y_label="amplitude")
    pyplot.plot(signal_base, signal)
    pyplot.show()


def read_audio_to_computer():
    current_path = os.path.dirname(os.path.abspath(__file__))
    audio_path = f"{current_path}/../../assets/audio/Bm_Flute_01_685.wav"
    print(f"Opening audio from: {audio_path}")
    sample_rate, audio = wavfile.read(audio_path)
    print(f"Sample rate: {sample_rate}, Audio: {audio}")

    setup_graph("Audio", x_label="time (samples)", y_label="amplitude")
    pyplot.plot(audio)
    pyplot.show()

    pyplot.plot(audio[20000:21000])
    pyplot.show()


def synthesize_flute_waveform(out_sample_rate=44100):
    period = 1000.0 / 17.25
    frequency = 1.0 / period

    synthesized_waveform = 15000 * numpy.sin(2 * numpy.pi * frequency * numpy.linspace(0, 59999, 60000))
    pyplot.plot(synthesized_waveform[20000:21000])
    wavfile.write("out/flute_out.wav", out_sample_rate, synthesized_waveform.astype(numpy.int16))
    pyplot.show()

    env = numpy.ones(synthesized_waveform.shape)
    env[0:50000] = numpy.linspace(0, 1, 50000)
    synthesized_waveform_env = synthesized_waveform * env
    pyplot.plot(synthesized_waveform_env)
    pyplot.show()

    wavfile.write("out/flute_out_env.wav", out_sample_rate, synthesized_waveform_env.astype(numpy.int16))

    pyplot.plot(synthesized_waveform_env[20000:21000])
    pyplot.plot(synthesized_waveform_env[11100:12100])
    pyplot.plot(synthesized_waveform_env[1500:2500])
    pyplot.show()


def adding_waves_together():
    x_axis = numpy.linspace(0, 2 * numpy.pi, 100)
    one_cycle_y = 5 * numpy.sin(x_axis)
    zero_cycle_y = 0 * numpy.sin(2 * x_axis)
    three_cycle_y = 3 * numpy.sin(3 * x_axis)
    four_cycle_y = 2 * numpy.sin(4 * x_axis)

    _, ax_arr = pyplot.subplots(4, sharex=True, sharey=True, figsize=(12, 6))
    ax_arr[0].plot(x_axis, one_cycle_y)
    ax_arr[1].plot(x_axis, zero_cycle_y)
    ax_arr[2].plot(x_axis, three_cycle_y)
    ax_arr[3].plot(x_axis, four_cycle_y)
    pyplot.show()

    setup_graph("Adding Waves Together", x_label="time (s)", y_label="amplitude", fig_size=(12, 6))
    convoluted_wave = one_cycle_y + zero_cycle_y + three_cycle_y + four_cycle_y
    pyplot.plot(x_axis, convoluted_wave)
    pyplot.show()

    second_three_cycle_y = numpy.sin(3 * x_axis)
    reversed_three_cycle_y = numpy.flip(second_three_cycle_y)
    bit_offset_three_cycle_y = -1 * numpy.sin(3 * x_axis + 0.25)

    # phase cancellation
    _, ax_arr = pyplot.subplots(4, sharex=True, sharey=True, figsize=(12, 6))
    ax_arr[0].plot(x_axis, second_three_cycle_y)
    ax_arr[1].plot(x_axis, reversed_three_cycle_y)
    ax_arr[2].plot(x_axis, second_three_cycle_y + reversed_three_cycle_y)
    ax_arr[3].plot(x_axis, bit_offset_three_cycle_y + second_three_cycle_y)
    pyplot.show()
