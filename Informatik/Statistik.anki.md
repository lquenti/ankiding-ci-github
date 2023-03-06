# Statistik

Statistik hat viele wichtige Formeln, in diesem Dokument werden wir folgende beleuchten:
- Mittelwert
- Median
- Modus
- Standardabweichung
- Varianz

## Mittelwert

Der Mittelwert berechnet naiv das Mittel aller Werte. Dies lässt sich am besten direkt durch die Formel erklären:

> Q: Wie ist die Formel für den Mittelwert?
> A:
> $$\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i$$

## Median

Der Median ist viel simpler, er beschreibt lediglich der mittlere Wert in der sortierten Liste!

> Q: Wie ist die Formel für den Median?
> A: $$\text{median}(x) = \begin{cases}x_{\frac{n+1}{2}}, & \text{if } n \text{ is odd} \\ \frac{x_{\frac{n}{2}}+x_{\frac{n}{2}+1}}{2}, & \text{if } n \text{ is even}\end{cases}$$


> Q: Was ist ausreißerfester? Der Mittelwert oder der Median?
> A:
> Der Median.

> Q: Wieso ist der Median ausreißerfester als der Mittelwert?
> A: Der Median ist ausreißerfester als der Mittelwert, weil er nicht auf extremen Werten im Datensatz reagiert, sondern nur auf die relative Position der Werte.

## Modus

> Q: Was ist der Modus?
> A: Der meistauftretende Wert in der Stichprobe

## Varianz und Standardabweichung

> Q: Wie ist die Formel für die Varianz?
> A: $$\text{Var}(x) = \frac{1}{n-1} \sum_{i=1}^{n}(x_i - \bar{x})^2$$

> Q: Wie ist die Formel für die Standardabweichung?
> A: $$s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n}(x_i - \bar{x})^2}$$

> Q: Wie ist die Relation von der Standardabweichung zur Varianz?
> A: Die Standardabweichung ist die Quadratwurzel der Varianz.

## Übungsaufgaben

> Q: Folgender Array: 1: [6, 4, 4, 0, 7, 2, 0, 7, 3, 7]
> - Mittelwert
> - Median
> - Modus
> - Standardabweichung
> - Varianz
> A: - Mittelwert: 4.0
> - Median: 4.0
> - Modus: 7
> - Standardabweichung: 2.748737083745107
> - Varianz: 7.555555555555555

> Q: Folgender Array: 2: [1, 7, 8, 2, 2, 2, 7, 7, 9, 9]
> - Mittelwert
> - Median
> - Modus
> - Standardabweichung
> - Varianz
> A: - Mittelwert: 5.4
> - Median: 7.0
> - Modus: 2
> - Standardabweichung: 3.2386554137309647
> - Varianz: 10.488888888888887

> Q: Folgender Array: 3: [0, 2, 10, 10, 9, 5, 6, 0, 10, 1]
> - Mittelwert
> - Median
> - Modus
> - Standardabweichung
> - Varianz
> A: - Mittelwert: 5.3
> - Median: 5.5
> - Modus: 10
> - Standardabweichung: 4.295992965026311
> - Varianz: 18.45555555555556

> Q: Folgender Array: 4: [10, 6, 0, 6, 6, 7, 10, 4, 2, 4]
> - Mittelwert
> - Median
> - Modus
> - Standardabweichung
> - Varianz
> A: - Mittelwert: 5.5
> - Median: 6.0
> - Modus: 6
> - Standardabweichung: 3.1710495984067415
> - Varianz: 10.055555555555555

> Q: Folgender Array: 5: [5, 8, 0, 10, 10, 5, 0, 7, 5, 10]
> - Mittelwert
> - Median
> - Modus
> - Standardabweichung
> - Varianz
> A: - Mittelwert: 6.0
> - Median: 6.0
> - Modus: 5
> - Standardabweichung: 3.7712361663282534
> - Varianz: 14.222222222222221
