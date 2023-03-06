# Insertion Sort

Insertion Sort ist ein simpler, stabiler in-place Sortieralgorithmus.

> Q: Was macht einen Sortieralgorithmus **stabil**?
> A: Ein Sortieralgorithmus ist stabil, wenn die Reihenfolge von gleichwertigen Elementen im sortierten Array beibehalten wird.

> Q: Ist Insertion Sort stabil?
> A: Ja

> Q: Was ist ein **In-Place** Algorithmus?
> A: Ein In-Place-Algorithmus bearbeitet die Eingabe direkt, ohne zusätzlichen Speicherplatz zu verwenden, d.h. er arbeitet auf demselben Speicherbereich wie die Eingabe.

## Funktionsweise

Hier ein Beispiel wie es funktioniert.

![Visualisierendes Bild](https://upload.wikimedia.org/wikipedia/commons/4/42/Insertion_sort.gif)

> Q: Wie funktioniert Insertion Sort konzeptuell?
> A:
> - Der Algorithmus beginnt mit dem zweiten Element des Arrays und vergleicht es mit dem ersten Element.
> - Wenn das zweite Element kleiner ist, wird es an die erste Position verschoben, andernfalls bleibt es an seiner Position.
> - Der Algorithmus geht dann zum dritten Element über und vergleicht es mit den ersten beiden Elementen und platziert es entsprechend an der richtigen Stelle.
> - Der Algorithmus arbeitet sich so durch das gesamte Array und sortiert es durch das Einfügen jedes Elements an die richtige Stelle.


## Laufzeit

> Q: Welche Laufzeiten hat Insertion Sort?
> A:
> - Im besten Fall (bereits sortiertes Array): O(n)
> - Im durchschnittlichen Fall: O(n^2)
> - Im schlechtesten Fall (umgekehrt sortiertes Array): O(n^2)
