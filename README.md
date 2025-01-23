# Space Invaders: Special Forces

*ESA DVC-E1 for SWT - this is a course project, please ignore*

This is a greatly simplified version of *Space Invaders* with the twist that
after each kill (or level) the speed of the enemy, the player and the player's
bullets grows, and the player can shoot successively more bullets at once.

## Instructions

Use the left and right keys to move and the space bar to shoot. Q (as well as
closing the window) exits the game.

## Background

The idea behind this game (an assignment for my Python programming course)
was to create a stable simple shooting game and then keep adding more features
until I ran out of time – which unfortunately (and unsurprisingly) happened
sooner than expected.

Also, I struggled with inserting longer actions (like exploding the enemy) in
the main loop and, while I found a way to do it towards the end, added sound
effects instead since the game never ends anyway. The sound effects are a nice
touch, though.

There were some more features planned: mainly the enemy shooting back, and
the enemy spawning more enemies, in addition to  the number of bullets
increasing more slowly. Lower-priority features include enemies landing and
crawling towards the player and the player being able to shoot sideways.
Had I taken two weeks instead of two days for this assignment, it would have
been a great game instead of an acceptable one.

The program structure partially reflects the desire to build on the existing
functions, but ultimately I took shortcuts fairly often as it became clear
that there wouldn't be more features.

There is one tiny bug that is really hardly noticeable in the current state but
would be a bigger problem with more enemies: when a bullet hits the enemy, the
last bullet is removed instead of the one that actually hit.

Dependency: pygame

## Credits

The assets were taken from OpenGameArt.org:

Graphics by Clear_code at
https://opengameart.org/content/assets-for-a-space-invader-like-game licensed
under CC-BY 4.0

Sounds by Michel Baradari at https://opengameart.org/content/4-projectile-launches
licensed under CC-BY 3.0

## Technical description

The game uses a couple of variables to keep track of the state of the game:

  - speed: the current movement speed of both the player and the enemy
  - max_bullets: the currect maximum number of concurrent bullets
  - level: the current level (again, for both the player and the enemy)
  - xyz_pos: position of the objects

The speed, max_bullets and level are increased by 1 every level, so they could
be handled with one variable, but for extensibility I left them separate.

The bullet positions are kept in a list (two really: one for the x and one
for the y values) so they can be iterated to move them.

## Functions

The main loop checks for keypresses and makes sure to call the appropriate
functions. It also prevents the player from leaving the screen boundaries.

start_level() is called at the start of each level, i.e. initially and when
the enemy has been killed.

shoot() is called when the player shoots. It checks if there are any bullets
left and if enough time has passed since the last shot (100 ms), and sets the
initial bullet position.

move_shots() moves all current bullets and draws them as rects on the screen.
It also checks for enemy collision and calls to destroy the enemy. Finally, it
removes bullets if they reach the upper screen border.

explode_enemy() kills the enemy and increases all values by raising the level.

explode_player() kills the player and resets the level.

(Nothing really explodes, but I left the function names to give the appearance
of more action.)

move_enemy() moves the enemy and checks for collision with the player object.
It calls explode_player() upon collision. Movement is basically random, but an
enemy moves -50 to 50 pixels in one direction before making the next random()
call so that it looks a little more unpredictable.
