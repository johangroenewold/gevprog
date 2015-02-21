#!/usr/bin/env python

import sys

class Country():
    def __init__(self, country):
        self.country = country
    
    def changeCountry(self, country):
        self.country = country
    
    def __str__(self):
        retString = "Hello from "
        retString += self.country
        return retString


if __name__ == '__main__':
    country = Country("Netherlands")
    print(country)

