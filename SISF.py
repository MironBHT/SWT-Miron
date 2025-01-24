#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Space Invaders: Special Forces
   See the README.md
"""

__author__ = "Miron Schmidt"
__copyright__ = "Copyright 2025 Miron Schmidt"
__email__ = "s90259@bht-berlin.de"
# The versioning is handled by git

import pygame
import random

pygame.init()

# global settings
dimensions_x = 640
dimensions_y = 480
start_speed = 4
bullet_color = pygame.Color(255, 255, 255)

screen = pygame.display.set_mode((dimensions_x, dimensions_y))
pygame.display.set_caption("SPACE INVADERS: Special Forces")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

keep_going = True

sprite_player = pygame.image.load("player.png")
player_pos = pygame.Vector2(0, 0)
level = 0
sprite_enemy = pygame.image.load("red.png")
enemy_pos = pygame.Vector2(0, 0)
max_bullets = 0      # current max number of bullets at the same time
num_bullets = 0      # current number of bullets
bullet_pos_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # positions of the bullets
bullet_pos_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # same
last_shot_time = 0
sound_shot = pygame.mixer.Sound("slimeball.wav")
sound_enemy = pygame.mixer.Sound("iceball.wav")
sound_player = pygame.mixer.Sound("rlaunch.wav")

# Functions

"""start_level() is called at the start of each level,
   i.e. initially and when the enemy has been killed.
"""
def start_level():
   global level
   global speed
   global max_bullets
   global enemy_pos
   level += 1
   enemy_pos.x = screen.get_width() / 2 - sprite_enemy.get_width() / 2
   enemy_pos.y = 0
   speed += 1
   if max_bullets < 10:
      max_bullets += 1

"""shoot() is called when the player shoots. It checks if there are any
   bullets left and if enough time has passed since the last shot (100 ms),
   and sets the initial bullet position.
"""
def shoot():
   global num_bullets
   global last_shot_time
   if pygame.time.get_ticks() < last_shot_time + 100:    # Don't shoot too often
      return
   if (num_bullets < max_bullets):
      bullet_pos_x[num_bullets] = player_pos.x + sprite_player.get_width() / 2
      bullet_pos_y[num_bullets] = screen.get_height() - sprite_player.get_height()
      num_bullets += 1
      last_shot_time = pygame.time.get_ticks()
      pygame.mixer.Sound.play(sound_shot)

"""move_shots() moves all current bullets and draws them as rects on the
   screen. It also checks for enemy collision and calls to destroy the
   enemy. Finally, it removes bullets if they reach the upper screen border.
"""
def move_shots():
   global num_bullets
   for shot in range(num_bullets):
      bullet_pos_y[shot] -= 2 * speed
      if bullet_pos_y[shot] <= enemy_pos.y + sprite_enemy.get_height():
         if (bullet_pos_x[shot] > enemy_pos.x
         and bullet_pos_x[shot] < enemy_pos.x + sprite_enemy.get_width()):
            num_bullets -= 1
            explode_enemy()
      if bullet_pos_y[shot] < 1:
         num_bullets -= 1
      bullet_to = pygame.Rect(bullet_pos_x[shot] - 2, bullet_pos_y[shot] - 2, 4, 4)
      pygame.draw.rect(screen, bullet_color, bullet_to)

"""explode_enemy() kills the enemy and increases all values by raising the
   level.
"""
def explode_enemy():
   global level
   global keep_going
   start_level()
   pygame.mixer.Sound.play(sound_enemy)

"""explode_player() kills the player and resets the level.
"""
def explode_player():
   global level
   global speed
   global max_bullets
   level = 0
   speed = start_speed
   max_bullets = 0
   start_level()
   pygame.mixer.Sound.play(sound_player)

"""move_enemy() moves the enemy and checks for collision with the player
   object. It calls explode_player() upon collision. Movement is basically
   random, but an enemy moves -50 to 50 pixels in one direction before
   making the next random() call so that it looks a little more
   unpredictable.
"""
def move_enemy():
   enemy_pos.x += 100 * (random.random() - 0.5)    # not very elegant
   enemy_pos.y += speed
   rect_enemy = pygame.Rect(enemy_pos.x, enemy_pos.y, sprite_enemy.get_width(), sprite_enemy.get_height())
   if enemy_pos.x > screen.get_width() - sprite_enemy.get_width():
      enemy_pos.x = screen.get_width() - sprite_enemy.get_width()
   if enemy_pos.x < 0:
      enemy_pos.x = 0
   if enemy_pos.y > screen.get_height():
      enemy_pos.y = 0
   if rect_enemy.colliderect(rect_player):
      explode_player()

clock = pygame.time.Clock()
player_pos.x = (screen.get_width() / 2) - (sprite_player.get_height() / 2)
player_pos.y = screen.get_height() - sprite_player.get_height()
speed = start_speed
start_level()

"""The main loop checks for keypresses and makes sure to call the appropriate
   functions. It also prevents the player from leaving the screen boundaries.
"""
if __name__ == '__main__':
   while keep_going:
      clock.tick(30)    # frame rate

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            keep_going = False

      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT]:
         player_pos.x -= speed
         if player_pos.x < 0:
            player_pos.x = 0
      if keys[pygame.K_RIGHT]:
         player_pos.x += speed
         if player_pos.x > screen.get_width() - sprite_player.get_width():
            player_pos.x = screen.get_width() - sprite_player.get_width()
      if keys[pygame.K_SPACE]:
         shoot()
      if keys[pygame.K_q]:
         keep_going = False

      rect_player = pygame.Rect(player_pos.x, player_pos.y, sprite_player.get_width(), sprite_player.get_height())
      screen.blit(background, (0, 0))
      screen.blit(sprite_player, player_pos)
      screen.blit(sprite_enemy, enemy_pos)
      move_enemy()
      move_shots()
      pygame.display.flip()
