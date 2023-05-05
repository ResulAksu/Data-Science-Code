import random as r
import math as m

# guckt ob die Zahl in Range von 10 ist in unserem Beispiel
def inRange(number, prob, sample_size):
    if number >= prob * sample_size:
        cal = number - prob * sample_size
        if 0 <= cal <= 12:
            return True
    if number < prob * sample_size:
        cal = prob * sample_size - number
        if 0 < cal <= 12:
            return True
    return False


def X():
    n = 1000
    # seed
    r.seed(1)

    # function for [a,b) random()*(b-a)+a -> uniform(a,b)
    cases = [
        r.uniform(5, 6),
        r.uniform(6, 7),
        r.uniform(7, 8)
    ]
    five_prob = 4/7
    six_prob = 2/7
    seven_prob = 1/7
    # samples choices (cases, prob, pulls)
    samples = r.choices(cases, [five_prob, six_prob, seven_prob], k=n)
    print(samples)

    # tests
    # floor
    test_floored_samples = []
    five_count = 0
    six_count = 0
    seven_count = 0
    for x in samples:
        floored = m.floor(x)
        test_floored_samples += [floored]
        if floored == 5:
            five_count += 1
        if floored == 6:
            six_count += 1
        if floored == 7:
            seven_count += 1

    five_check = inRange(five_count, five_prob, n)
    six_check = inRange(six_count, six_prob, n)
    seven_check = inRange(seven_count, seven_prob, n)
    print("Floored Samples: ",test_floored_samples)
    print("Vorkommen sortiert nach 5,6,7: ",five_count, six_count, seven_count)
    print("Überprüfung sortiert nach 5,6,7: ",five_check, six_check, seven_check)
    # median 1/2*(list[n/2]+list[n/2+1] for even list size
    sorted_samples = sorted(samples, key=float)
    median = 1 / 2 * float(sorted_samples[n/2] + sorted_samples[(n/2)+1])
    print("Median: ",median)


    # arithmetisches Mittel addieren aller Werte/k
    arithmetic_mean = 0
    for i in samples:
        arithmetic_mean += i
    arithmetic_mean = arithmetic_mean/n
    print("Arithmetisches Mittel: ", arithmetic_mean)


    # erwartungswert, x_1 * P(X=x_1) + ... + x_n * P(X=x_n)
    erwartungswert = 5.0*(five_prob)+6.0*(six_prob)+7.0*(seven_prob)+8.0*(1-(five_prob+six_prob+seven_prob))
    print("Erwartungswert: ",erwartungswert)

    # falsch 
    # stichproben-standradabweichung sqrt(sum(x_i - mu)^2/(n-1)) 
    helper = []
    for i in samples:
        calc = (i-arithmetic_mean)**2
        helper += [calc]
    abweichung = 0
    for i in helper:
        abweichung += i

    # varianz
    varianz = abweichung/n-1
    print("Varianz: ", varianz)


    standardabweichung = m.sqrt(varianz)
    print("Standardabweichung: ", standardabweichung)
    # Abweichungen
    print("Abweichung von Erwartungswert und Median: ", erwartungswert-median)
    print("Abweichung von Erwartungswert und ar.Mittel: ", arithmetic_mean - erwartungswert)
    print("Abweichung von Varianz und SampleStandardabweichung: ", varianz-standardabweichung)
    tupel = (median, arithmetic_mean, erwartungswert, standardabweichung, varianz)
    print("Tupel: ", tupel)
X()
