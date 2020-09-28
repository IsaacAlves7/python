import pygame
import playsound
playsound.playsound('whatsapp.mp3') #musica

pygame.init()
pygame.mixer.music.load('C:/Users/user/Desktop/whatsapp.mp3')
pygame.mixer.music.play()
pygame.event.wait()
