#!/bin/python
import timeit


def parser():
    """A parser provided by the csacademy, basically creates a generator"""
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield (number)


input_parser = parser()  # generator object


def get_word():
    global input_parser
    return next(input_parser)


def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


def identify(length, position):
    """Finds how many letters we are using """

    # Δεν εχει σημασια ποσο μεγαλο ειναι το position, αμα ειναι ενα μονο γραμμα θα ειναι παντα το a
    if length == 1:
        return 'a'

    # occurrence η μεταβλητη στην οποια αποθηκευουμε ποσες φορες θελουμε να εμφανιστει το καθε γραμμα στους συνδιασμους τους
    occurrence = 1
    while True:

        if position < occurrence * (length ** occurrence):
            # return chr(ord('a') + position_to_letter(position, length, occurrence))
            # Αντιμετωπιζουμε το string σαν εναν πινακα
            return chr(97 + position_to_letter(position, length, occurrence))
        # Αφαιρουμε το occurrence*(length**occurrence) γιατι ειναι το πληθος ολων των γραμματων ολων των συνδιασμων
        # και παμε στο επομενο. Επειδη αντιμετωπιζουμε το String Σαν μονοδιαστατη αναπαρασταση δισδιαστου πινακα
        # θελουμε να ξεκιναει παντα απο το 0 το indexing του .
        position -= occurrence * (length ** occurrence)
        occurrence += 1


def position_to_letter(pos, length, occurrence):
    """finds the letter in a table of occurrence columns and length^occurrence rows"""
    row = pos // occurrence
    col = pos % occurrence
    if col == 0:
        return row // length ** (occurrence - 1)
    return row // length ** (occurrence - 1 - col) % length


def main():
    T = get_number()
    # το get_number() ειναι ενα Parser Που δινει το csacademy.
    # δημιουργουμε μια λιστα με περιεχομενο tuples των δυο, που ειναι το B kai X απο το προβλημα που μας δινουν

    data = [(int(get_word()), int(get_word())) for _ in range(T)]

    for t in range(T):
        print(identify(data[t][0], data[t][1]))


if __name__ == '__main__':
    main()
