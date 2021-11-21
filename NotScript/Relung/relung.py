import math
import sys
import os

# all conversion is to meter squared
is_not_area = ['meter', 'kaki', 'ela', 'relung', 'jempa', 'depa']
area_conversion = {
    'meter': 1,
    'kaki': .0929,
    'ela': .836,
    'relung': 2877.8,
    'jempa': 5.9456,
    'ekar': 4046.86,
    'hektar': 10000,
    'rood': 1011.7,
    'pole': 25.293,
    'depa': 3.3445
}


def ukuq_relung(unit1, unit2, val):
    unit1_to_mtr = val * area_conversion.get(unit1, 1)
    mtr_to_unit2 = unit1_to_mtr / area_conversion.get(unit2, 1)
    return mtr_to_unit2


def print_output(unit1, unit2, val):
    u1, u2 = unit1, unit2
    if unit1 in is_not_area:
        u1 += ' persegi'
    if unit2 in is_not_area:
        u2 += ' persegi'
    nilai = ukuq_relung(unit1, unit2, val)
    print()
    print(f'{val} {u1} = {nilai} {u2}')
    print()

if __name__ == '__main__':
    unit1 = unit2 = val = None
    filename = os.path.basename(sys.argv[0])
    if sys.argv[1:]:
        print('kaedah penggunaan: ')
        print(f'{filename} nilai unit1 unit2')
        print('contoh: ')
        print(f'{filename} 20 ekar relung - convert 20 ekar ke berapa relung')
        print('output: ')
        print_output('ekar', 'relung', 20)
        try:
            val, unit1, unit2 = sys.argv[1:4]
        except:
            print('salah format nih')
            exit()
        valid = True
        try:
            val = float(val)
        except ValueError:
            print('boleh bagi nombot kot noh')
            valid = False
        if unit1 not in area_conversion:
            print(f"'{unit1}' xdak dlm tu noh")
            valid = False
        if unit2 not in area_conversion:
            print(f"'{unit2}' xdak dlm tu noh")
            valid = False
        if not valid:
            exit()
        print_output(unit1, unit2, val)
        exit()

    while True:
        print('hang nak kira relung besaq mana?')
        print('unit2 yg dok ada:')
        print(', '.join(i for i in area_conversion))
        print()
        unit1 = input('unit pertama: ')
        while unit1 not in area_conversion:
            print(f"'{unit1}' xdak dlm tu noh")
            unit1 = input('boh balik unit pertama: ')
        unit2 = input('unit kedua: ')
        while unit2 not in area_conversion:
            print(f"'{unit2}' xdak dlm tu noh")
            unit2 = input('boh balik unit kedua: ')
        while not val:
            val = input(f'nak kira berapa {unit1}?')
            try:
                val = float(val)
            except ValueError:
                print('boleh bagi nombot kot')
                val = None

        if unit1 and unit2 and val:
            print_output(unit1, unit2, val)
        del unit1, unit2, val
