# Desafio 021/ Aula8
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
from pygame import init,mixer,event
init()
mixer.init()

mixer.music.load("metal-pipe-sound.mp3")
mixer.music.play()
event.wait()