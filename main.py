from __future__ import print_function
from pygame import mixer
import librosa 
import numpy as np
import time
import traceback
import matplotlib.pyplot as plt
import librosa.display
import matplotlib.style as ms
ms.use('seaborn-muted')
import IPython.display
import sys





def play_music(file_name):
    mixer.init()
    mixer.music.load(file_name)
    mixer.music.play()


def stop_music():
    mixer.music.stop()


def load_music(file_name):
    y, sr = librosa.load(file_name)
    tempo, beats = librosa.beat.beat_track(y=y, units='time')
    return y, sr, beats

def display_beats(y, beats):
    
    total_time = librosa.get_duration(y=y)
    start_time = time.time() 
    current_time = (time.time() - start_time) % 60 

    # new_beats = beats.astype(int)

    i = 0
    while current_time < total_time:
        # print "current time: ", int(current_time)
        # print "beats[i]: ", new_beats[i]
        if round(current_time,4) == round(beats[i],4):
            i+= 1
            sys.stdout.write("\rBEAT NUMBER: %d" % i)

        sys.stdout.flush()

        current_time = (time.time() - start_time) % 60 

def draw_spect(y, sr):
    S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128)
    log_S = librosa.logamplitude(S, ref_power=np.max)
    plt.figure(figsize=(12,4)) 
    librosa.display.specshow(log_S, sr=sr, x_axis='time', y_axis='mel')
    plt.title('mel power spectrogram')
    plt.colorbar(format='%+02.0f dB')
    plt.tight_layout()
    plt.show()






junky = 'junky_brockhampton.mp3'

try:
    print ('LOADING MUSIC')
    y, sr, beats = load_music(junky)

    # draw_spect(y,sr)


    print ('STARTING MUSIC')
    play_music(junky)


    print ('STARTING BEAT TRACKING')
    display_beats(y, beats)


    print ('STOPPING MUSIC')
    stop_music()
except Exception as e:
    traceback.print_exc()
    stop_music()