import sys
import heifer_generator
from dragon import Dragon

def main():
    cow_string = ''
    arguments = sys.argv[1:]
    cows = heifer_generator.get_cows()

    if not arguments:
        print("No arguments provided.")

    elif '-l' == arguments[0]:
        for cow in cows:
            cow_string += cow.name + ' '
        print(f'Cows available: {cow_string}')

    elif '-n' == arguments[0]:
        valid = False
        for cow in cows:
            if cow.name in arguments:
                speech = ''
                for word in arguments[2:]:
                    speech += word
                    speech += ' '
                print(speech[:-1])
                print(cow.image)
                if isinstance(cow, Dragon):
                    check = cow.can_breath_fire()
                    if check:
                        print('This dragon can breathe fire.')
                    else: print('This dragon cannot breathe fire.')
                valid = True
                break
        if not valid:
            print(f'Could not find {arguments[1]} cow!')


    else:
        speech = ''
        for word in arguments:
            speech += word
            speech += ' '
        print(speech)
        print(cows[0].image)

if __name__ == "__main__":
    main()