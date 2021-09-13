# Hirday pal Singh
# eigen rekenmachine maken

def main():
    print()
# input selecteren
    operation = input('''
    selecteer uw optie:
    * - om te vermenigvuldigen
    / - om te delen
    + - om te optellen
    - - om te aftrekken
    % - om te staardelen
    ''')
# getallen invoeren
    number_1 = float(input("Voer uw nummer in: "))
    number_2 = float(input("Voer uw nummer in: "))
# functie om getallen bij elkaar op te tellen
    if operation == '+':
        print('{} + {} = ' .format(number_1, number_2))
        print(number_1 + number_2)
# functie om getallen te aftrekken
    elif operation == '-':
        print('{} - {} = ' .format(number_1, number_2))
        print(number_1 - number_2)
# functie om getallen te delen
    elif operation == '/':
        print('{} / {} = ' .format(number_1, number_2))
        print(number_1 / number_2)
# functie om getallen te vermeningvuldigen
    elif operation == '*':
        print('{} * {} = ' .format(number_1, number_2))
        print(number_1 * number_2)
# functie om te staardelen
    elif operation == '%':
        print('{} % {} = ' .format(number_1, number_2))
        print(number_1 % number_2)
# functie als er iets ander wordt ingevowr dan: *, -, +, /, %
    else:
        print("U heeft geen geldige teken ingevoerd, probeer opwnieuw")


if __name__ == "__main__":
# functie om de code vaker te gebruiken
    while True:
        main()
