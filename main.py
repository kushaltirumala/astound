from pygame import mixer
import librosa 
import numpy as np
import time
import traceback



def play_music(file_name):
    mixer.init()
    mixer.music.load(file_name)
    mixer.music.play()


def stop_music():
    mixer.music.stop()


def load_music(file_name):
    y, sr = librosa.load(file_name)
    tempo, beats = librosa.beat.beat_track(y=y, units='time')
    return y, beats

def display_beats(y, beats):
    
    total_time = librosa.get_duration(y=y)
    start_time = time.time() 
    current_time = (time.time() - start_time) % 60 

    # new_beats = beats.astype(int)

    i = 0
    while current_time < total_time:
        # print "current time: ", int(current_time)
        # print "beats[i]: ", new_beats[i]
        if round(current_time,5) == round(beats[i],5):
            print "beat at time: ", round(current_time, 4)
            i+= 1

        current_time = (time.time() - start_time) % 60 

junky = 'junky_brockhampton.mp3'

try:
    print 'LOADING MUSIC'
    y, beats = load_music(junky)

    print 'STARTING MUSIC'
    play_music(junky)

    print 'STARTING BEAT TRACKING'
    display_beats(y, beats)

    print 'STOPPING MUSIC'
    stop_music()
except Exception as e:
    traceback.print_exc()
    stop_music()