# ESA DVC-E1 (SWT)

*This is a course project, please ignore*

*If you're interested in the game (though I don't see why you would), the real
repo is at https://codeberg.org/Miron/SISF*

## Vorbemerkung

Diese Datei ist meine Dokumentation der Aufgabe. Ich habe hier Programmantworten zitiert,
anstatt Screenshots zu machen, da diese ja auch nur aus Text bestanden hätten.

## Aufgaben 1-2

Die Dateien wurden direkt in GitHub hochgeladen, dann legte ich eine lokale
Kopie mittels `git clone` an.

## Aufgabe 3

Die restlichen Schritte fanden teils in GitHub, teils in der Shell statt:

- `git push` für diese README-Datei. (`add` und `commit` sind implizit.)
- Bearbeiten von SISF.py in GitHub (winzige Änderung).
- `git pull`, um diese Änderung lokal abzurufen.

Antwort von git:

	From https://github.com/MironBHT/SWT-Miron
	d13603b..e230350  main       -> origin/main
	Updating d13603b..e230350
	Fast-forward
	SISF.py | 2 +-
	 1 file changed, 1 insertion(+), 1 deletion(-)

- Nach weiterem lokalen Arbeiten an dieser README-Datei `git status` und `git diff`:

		$ git status
		On branch main
		Your branch is up to date with 'origin/main'.
		Changes not staged for commit:
		(use "git add <file>..." to update what will be committed)
		(use "git restore <file>..." to discard changes in working directory)
		modified:   README.md
		no changes added to commit (use "git add" and/or "git commit -a")
		$ git diff
		diff --git a/README.md b/README.md
		index 91520a5..51875d7 100644
		--- a/README.md
		+++ b/README.md
		@@ -19,4 +19,18 @@ Kopie mittels `git clone` an.
		Die restlichen Schritte fanden teils in GitHub, teils in der Shell statt:
		-1. push 
		+- `git push` für diese README-Datei. (`add` und `commit` sind implizit.)^M
		+- Bearbeiten von SISF.py in GitHub (winzige Änderung)^M
		+- `git pull`, um diese Änderung lokal abzurufen.^M
		+^M
		+(Antwort von git:^M
		+^M
		+> From https://github.com/MironBHT/SWT-Miron^M
		+> d13603b..e230350  main       -> origin/main^M
		+> Updating d13603b..e230350^M
		+> Fast-forward^M
		+>  SISF.py | 2 +-^M
		+>  1 file changed, 1 insertion(+), 1 deletion(-)^M
		+^M
		+)^M
		+

- Hochladen der unnötigen Datei `green.png` in GitHub und wieder Löschen mit lokalen Shell-Befehlen `rm` und `git rm`.
- Ansehen der Commits mit `git log` (muss ich ich nicht weiter dokumentieren, hoffe ich).

## Aufgabe 4

- Setzen eines ersten Tags (v1.1-swt) in GitHub.
- Hochladen der aktuellen README-Datei per `push`, Setzen eines neuen Tags (v1.2-swt) per `git tag v1.2-swt`.
- `git checkout v1.1-swt`:

		Note: switching to 'v1.1-swt'.
		You are in 'detached HEAD' state. You can look around, make experimental
		changes and commit them, and you can discard any commits you make in this
		state without impacting any branches by switching back to a branch.

- Nach einigem Hin- und Herprobieren Wiederherstellen von v1.2-swt und Aktualisieren der README-Datei. (Problem: Beim Checkout wurde der Zustand "HEAD detached" hergestellt, den ich erst nach mehreren Versuchen und letztlich durch Aufgeben und Zurückkehren in den `main`-Branch beheben konnte.)

## Aufgabe 5

- Erstellen des neuen Branches `test` und wechseln zu dem Branch lokal mit `git checkout test`.
- Erneutes Anlegen einer kleinen Änderung in `SISF.py` und Pushen in den `test`-Branch mit `git push --set-upstream origin test`. Überraschend komplizierte Antwort von Git:

		Enumerating objects: 5, done.
		Counting objects: 100% (5/5), done.
		Delta compression using up to 8 threads
		Compressing objects: 100% (3/3), done.
		Writing objects: 100% (3/3), 396 bytes | 396.00 KiB/s, done.
		Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
		remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
		To https://github.com/MironBHT/SWT-Miron
		  9a182b7..2fdc835  test -> test
		Branch 'test' set up to track remote branch 'test' from 'origin'.

- Überprüfen des Zustands in GitHub. In der Tat dort eine Meldung "**test** had recent pushes 3 minutes ago" mit Aufforderung zum Erstellen eines Pull-Requests, die auch beim Wechseln in den `main`-Branch erhalten bleibt.
- Der Aufforderung in GitHub nachgekommen und Bestätigung erhalten: "MironBHT merged commit **d0f5a85** into main now".
- Zum Sichergehen: `git checkout main`:

		Switched to branch 'main'
		Your branch is up to date with 'origin/main'.

## Aufgabe 6

Als Pull-Request habe ich mich den beliebten Kochrezepten angeschlossen. Das ist allerdings tatsächlich ein Familienrezept, das ich sehr empfehlen kann!

SHA: 744f74be2361f76fbfeddb55c647e8f435a13178

## Abschluss

Als letzten Schritt habe ich wieder die letztgültige Version der README-Datei (diese hier) hochgeladen, diesmal direkt in GitHub, um das auch noch mal gemacht zu haben.
