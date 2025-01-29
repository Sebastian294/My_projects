#Script that modifies markdown files

import os
import re
import shutil
import unicodedata

from pathlib import Counter
from collections import Path
from spellchecker import SpellChecker

#Dictionaries for languaje detection
dictionary_es = SpellChecker(language='es')
dictionary_en = SpellChecker(language='en')

#Regular expression to detect coding blocks in markdown
CODE_BLOCK_PATTERN = re.compile(r'```.*?```', re.DOTALL)

#Function to normalize words whitout accents
def normalize_word(targetword):
    return unicodedata.normalize('NFKD', targetword).encode('ASCII', 'ignore').decode('ASCII')


