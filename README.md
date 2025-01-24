# Space Invaders: Special Forces

*ESA DVC-E1 for SWT - this is a course project, please ignore*

*If you're interested in the game (though I don't see why you would), the real
repo is at https://codeberg.org/Miron/SISF*

This is a greatly simplified version of *Space Invaders* with the twist that
after each kill (or level) the speed of the enemy, the player and the player's
bullets grows, and the player can shoot successively more bullets at once. I
created it for another course.

Thus ends the documentation and the German course part begins. 

## Dokumentation

Die Dateien wurden direkt in GitHub hochgeladen, dann legte ich eine lokale
Kopie mittels `git clone` an.

Die restlichen Schritte fanden teils in GitHub, teils in der Shell statt:

- `git push` für diese README-Datei. (`add` und `commit` sind implizit.)
- Bearbeiten von SISF.py in GitHub (winzige Änderung)
- `git pull`, um diese Änderung lokal abzurufen.

Antwort von git:

	From https://github.com/MironBHT/SWT-Miron
	
	d13603b..e230350  main       -> origin/main
	
	Updating d13603b..e230350
	
	Fast-forward
	
	SISF.py | 2 +-
	
	 1 file changed, 1 insertion(+), 1 deletion(-)

- Nach weiterem lokalen Arbeiten an dieser README-Datei `git status` und `git diff`:

> miron@Thalion:~/Work/Studium/SWT/ESAs/ESA 9/SISF/SWT-Miron$ git status

> On branch main

> Your branch is up to date with 'origin/main'.

> Changes not staged for commit:

>   (use "git add <file>..." to update what will be committed)

>   (use "git restore <file>..." to discard changes in working directory)

> 	modified:   README.md

> no changes added to commit (use "git add" and/or "git commit -a")

> miron@Thalion:~/Work/Studium/SWT/ESAs/ESA 9/SISF/SWT-Miron$ git diff

> diff --git a/README.md b/README.md

> index 91520a5..51875d7 100644

> --- a/README.md

> +++ b/README.md

> @@ -19,4 +19,18 @@ Kopie mittels `git clone` an.

>  Die restlichen Schritte fanden teils in GitHub, teils in der Shell statt:

> -1. push 

> +- `git push` für diese README-Datei. (`add` und `commit` sind implizit.)^M

> +- Bearbeiten von SISF.py in GitHub (winzige Änderung)^M

> +- `git pull`, um diese Änderung lokal abzurufen.^M

> +^M

> +(Antwort von git:^M

> +^M

> +> From https://github.com/MironBHT/SWT-Miron^M

> +> d13603b..e230350  main       -> origin/main^M

> +> Updating d13603b..e230350^M

> +> Fast-forward^M

> +>  SISF.py | 2 +-^M

> +>  1 file changed, 1 insertion(+), 1 deletion(-)^M

> +^M

> +)^M

> +

