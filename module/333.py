# -*- coding: utf-8 -*-
import wave
from Sonic import *
import functools
import numpy
from scipy import signal
import wave
import pylab
from WavFileReader import *

def wav_file_block_read(test, block_size=None):
    # 打开WAV文档
    wav_file = wave.open(test, "rb")
    # 读取格式信息
    wave_parameter = wav_file.getparams()
    #声道数, 量化位数（byte单位）, 采样频率, 采样点数, 压缩类型, 压缩类型的描述。wav非压缩，因此忽略最后两个信息
    # (wave_channels, sample_width, sample_frequency, sample_length, compress_type, compress_comment)
    wave_channels, sample_width, sample_frequency, sample_length = wave_parameter[:4]
    sonic_conf = {
        'channels':wave_channels,
        'sample_width':sample_width,
        'sample_frequency':sample_frequency
    }
    sonic = Sonic(**sonic_conf)

    # readframes：读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位），readframes返回的是二进制数据
    if not block_size:
        block_size = sample_length
    wave_bin_data = wav_file.readframes(block_size)
    while wave_bin_data:
        sonic.update_wave_data(wave_bin_data, block_size)
        yield sonic
        wave_bin_data = wav_file.readframes(block_size)
    else:
        wav_file.close()

def wav_file_read(test):
    # 打开WAV文档
    wav_file = wave.open(test, "rb")
    # 读取格式信息
    wave_parameter = wav_file.getparams()
    #声道数, 量化位数（byte单位）, 采样频率, 采样点数, 压缩类型, 压缩类型的描述。wav非压缩，因此忽略最后两个信息
    # (wave_channels, sample_width, sample_frequency, sample_length, compress_type, compress_comment)
    wave_channels, sample_width, sample_frequency, sample_length = wave_parameter[:4]
    # readframes：读取声音数据，传递一个参数指定需要读取的长度（以取样点为单位），readframes返回的是二进制数据
    wave_bin_data = wav_file.readframes(sample_length)
    wav_file.close()
    sonic_conf = {
        'channels':wave_channels,
        'sample_width':sample_width,
        'sample_frequency':sample_frequency,
        'sample_length':sample_length,
        'wave_bin_data' : wave_bin_data
    }
    sonic = Sonic(**sonic_conf)
    return sonic
print("aaaaaa")
def wave_plotting(sonic, block=False):
    if isinstance(sonic.wave_bin_data, list):
        bin_buffer = bytearray()
        for data in sonic.wave_bin_data:
            bin_buffer.extend(data)
        sonic.wave_bin_data = bytes(bin_buffer)
    elif not isinstance(sonic.wave_bin_data, bytes):
        raise Exception("Type of bin_data need bytes!")

    #接下来需要根据声道数和量化单位，将读取的二进制数据转换为一个可以计算的数组
    wave_data = numpy.fromstring(sonic.wave_bin_data, dtype=number_type.get(sonic.sample_width))
    #现在我们得到的wave_data是一个一维的short类型的数组，但是因为我们的声音文件是双声道的，
    # 因此它由左右两个声道的取样交替构成：LRLRLRLR....LR（L表示左声道的取样值，R表示右声道取样值）。修改wave_data的sharp
    wave_data.shape = (sonic.sample_length, sonic.channels)
    wave_data = wave_data.T
    time = numpy.arange(0, sonic.sample_length) * (1.0 / sonic.sample_frequency)

    # 绘制波形
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    pylab.figure()
    for index in range(0, sonic.channels):
        pylab.subplot(sonic.channels, 1, index + 1)
        pylab.plot(time, wave_data[index], colors[index % len(colors)])
    pylab.ylabel("quantization")
    pylab.xlabel("time (seconds)")
    pylab.ion()
    if block:
        pylab.ioff()
    pylab.show()


def wav_file_plotting(filename, *args, **kwargs):
    sonic = wav_file_read(filename)
    wave_plotting(sonic, *args, **kwargs)
print("aaaaaa")
def polynomials_filter(polynomial_creater):
    @functools.wraps(polynomial_creater)
    def filter_creater(*args, **kwargs):
        iir_polynomial = polynomial_creater(*args, **kwargs)
        def bandpass_filter(data):
            filtered_data = signal.lfilter(data, *iir_polynomial)
            return filtered_data
        return bandpass_filter
    return filter_creater

@polynomials_filter
def butter_bandpass(low_cut, high_cut, sample_frequency, order=6):
    nyquist_f = 0.5 * sample_frequency
    low_point = low_cut / nyquist_f
    high_point = high_cut / nyquist_f
    b, a = signal.butter(order, (low_point, high_point), btype='bandpass')
    iir_polynomial = (b, a)
    return iir_polynomial

@polynomials_filter
def cheby1_bandpass(low_cut, high_cut, sample_frequency, order=6, rp=0.1):
    nyquist_f = 0.5 * sample_frequency
    low_point = low_cut / nyquist_f
    high_point = high_cut / nyquist_f
    b, a = signal.cheby1(order, rp, (low_point, high_point), btype='bandpass')
    iir_polynomials = (b, a)
    return iir_polynomials


