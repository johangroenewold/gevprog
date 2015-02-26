#!usr/bin/python3

import sys
import json
from collections import namedtuple

def main():
    # Open JSON file, create empty list for matches and define namedtuples
    jsonFile = json.load(open("blood-die.json"))
    matchList = []
    Match = namedtuple('Matches', 'language, classifications')
    
    for language in jsonFile:
        langName = language[0]
        langClass = language[1]
        langBlood = language[2]
        langDie = language[3]
        
        bloodList = langBlood.strip().split(", ")
        dieList = langDie.strip().split(", ")
		
        # Find matches and break out of loops to prevent adding languages twice
        for bloodWord in bloodList:
            for dieWord in dieList:
                if(bloodWord == dieWord):
                    matchList.append(Match(langName, langClass))
                    break
            break
                    
    # Formatted printing using list comprehensions
    [print("{:25} {}".format(lang, lClass)) for lang, lClass in matchList]
if __name__ == "__main__":
	main()
