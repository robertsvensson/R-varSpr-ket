# -*- coding: UTF-8 -*-

class Rovare(object):
    def __init__(self):
        self.rovarTecken = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']

    def draEnRovare(self, s):
        result = ''

        for letter in s:
            if letter in self.rovarTecken:
                result = result + letter + 'o' +letter
            else:
                result = result + letter

        return result
