# Divide And Conquer

## Einführung

Divide and Conquer ist ein Paradigma zum Algorithmenentwurf. Es basiert darauf, dass man ein Problem oftmals einfacher lösen kann indem man es in kleinere Teilprobleme aufteilt.

> Q: Wie nennt sich Divide and Conquer auf Deutsch?
> A: Teile-und-herrsche

Auf einer abstrakten Ebene lässt sich jeder Divide and Conquer Algorithmus in 3 Schritte aufteilen

> Q: In welche 3 Schritte lässt sich jeder Divide and Conquer Algorithmus aufteilen?
> A:
> 1. Divide: Teile das Problem auf
> 2. Conquer: Löse das Grundproblem (Rekursionsbasisfall)
> 3. Combine: Führe kleinere Teillösungen zu einer größeren Lösung zusammen

Divide and Conquer, anhand dieser Bescheibung, lässt sich offensichtlich einer größeren Algorithmenklasse zuordnen:

> Q: Welcher Algorithmenklasse lassen sich D&C Algorithmen zuordnen?
>
> Tipp: Es geht um die Formelart des mathematischen Problems.
> A: Es ist eine Untermenge der __rekursiven__ Problemen

Es gibt viele Probleme die sich mit besser Rekursiv durch Divide and Conquer Algorithmen lösen lassen. Hier ein paar Beispiele:

> Q: Welche Suchalgorithmen benutzen Divide and Conquer?
> Beschreibe zusätzlich ob die Arbeit eher im Divide oder eher im Combine liegt
> A:
> **Quick Sort**: Es wird links und rechts vom Pivotelement aufgeteilt.
>
> Die Arbeit liegt im Divide, da alle Elemente um das Pivot verschoben werden müssen.
>
> **Merge Sort**: Es wird das Problem aufgeteilt, um es dann nach zwei-Finger-Prinzip zu mergen.
>
> Die Arbeit liegt im Combine-Arbeitsschritt, da beim Aufteilen noch gar keine Arbeit erbracht wurde.

Aber auch außerhalb der reinen Informatik finden sich Divide and Conquer Probleme. Zum Beispiel ist der wichtigste Algorithmus der Naturwissenschaften auch ein D&C Algorithmus!

> Q: Welche naturwissenschaftlich relevante mathematische Operation wird mit Divide and Conquer berechnet?
>
> A: Die Fast-Fourier-Transformation (FFT)

## Laufzeiten

Die Laufzeiten von Divide and Conquer Algorithmen weisen ein bestimmtes Muster auf. Hier ein paar Beispiele:

> Q: Wie ist die durchschnittliche Laufzeit für Quick Sort?
> A: $$O(n\log n)$$

> Q: Wie ist die durchschnittliche Laufzeit für Merge Sort?
> A: $$O(n\log n)$$

> Q: Wie ist die durchschnittliche Laufzeit für einen Binary Search?
> A: $$O(\log n)$$

> Q: Wie ist die Laufzeit von Cooley-Tukeys FFT?
> A: $$O(n\log n)$$

> Q: Was ist ein verräterisches Anzeichen in Zeitkomplexitätsformeln, dass es sich um ein D&C Algorithmus handelt?
>
> A: Der Logarithmus

> Q: Woher kommt der Logarithmus in den Formeln?
> A: Dadurch, dass die Tiefe eines balancierten Baums der Logarithmus des Branching Factors ist.
