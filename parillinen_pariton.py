#
# @author tekija: Verneri Lähteenoja
# @since pvm: versio pvm 18.4.2023
# @version

#

import unittest

runtest = 0

def parillisuus(number):
    for counter in range(number+1):
        if counter % 2 == 0:
            print(counter)
            onko_parillinen = 'on parillinen'
        else:
            print(counter)
            onko_parillinen = 'on pariton'
    return onko_parillinen

if runtest == 1:
    parillisuus(4)

# python -m unittest parillinen_pariton.py
class TestParillinenParitonLoop(unittest.TestCase):
    def test_parillisuus_on_pariton(self):
        testiarvo = 1
        actual = parillisuus(testiarvo)
        print(actual)
        expected = 'on pariton'
        try:
            assert actual == expected
        except:
            print(f'Virhe parittomuuden tarkistamisessa Numero = {str(testiarvo)}, {str(actual)} != {str(expected)}')

    def test_parillisuus_on_parillinen(self):
        testiarvo = 2
        actual = parillisuus(testiarvo)
        print(actual)
        expected = 'on parillinen'
        try:
            assert actual == expected
        except:
            print(f'Virhe parittomuuden tarkistamisessa. Numero = {str(testiarvo)}, {str(actual)} != {str(expected)}')