# How to Play Game

- open terminal window
- cd into kenneth_alien_invasion
- python3 alien_invasion.py
- Enjoy! =)

# DEVNOTES.md

##### Wednesday, November 21, 2018

End Point: 

Adding Rows Complete
Ended at Try It Yourself 13-1 Stars:

<!-- Need to work 13-1, 13-2 -->

Ending the Game.
p. 287


Traceback (most recent call last):
  
[] GameStats function in game_stats.py

  File "alien_invasion.py", line 41, in <module>
    run_game()
  
  [x] File "alien_invasion.py", line 37, in run_game
    gf.update_aliens(ai_settings, ship, aliens, screen, stats, bullets)
  
  [x] File "/Volumes/sdMemory/FullStackDeveloper/kenneth_alien_invasion/game_functions.py", line 171, in update_aliens
    check_fleet_edges(ai_settings, aliens)
  
  [x] File "/Volumes/sdMemory/FullStackDeveloper/kenneth_alien_invasion/game_functions.py", line 124, in check_fleet_edges
    for alien in aliens.sprites():

AttributeError: 'GameStats' object has no attribute 'sprites'



