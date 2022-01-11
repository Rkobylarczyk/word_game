
# Stwórz grę do nauki języka angielskiego, gdzie użytkownik musi przetłumaczyć 5 losowo wybranych haseł z 10 (słownik).
# Weryfikacja odpowiedzi po w czasie, je.
# Maksymalna liczba podejść do jednego hasła to trzy.
# Hasła (z 5) są losowo generowane.
# Użytkownik za poprawne odgadnięcia hasła dostaje punkty, odpowiednio:
# za pierwszym razem 20 pkt
# za drugim razem 10 pkt
# za trzecim razem 5 pkt.
# Maksymalna liczba punktów do zdobycia to 100. Na końcu gry użytkownikowi wyświetla się komunikat o liczbie zdobytych punkt

import random

words = {'kot':'cat', 'pies':'dog', 'woda':'water', 'kawa':'coffee', 'herbata':'tea', 'ptak':'bird'}
no_of_tries = 3
tries = {1:20, 2:10, 3:5}
number_of_point = 0

def choose_word(words_dict, number_of_words):
    random_list = random.sample(words_dict.keys(), number_of_words)
    return random_list


random_dict = choose_word(words, 3)
print(random_dict)
