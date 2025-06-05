
import pydeepl
import io
import sys

import pydeepl

from_language = sys.argv[1]
to_language = sys.argv[2]
sentence = sys.argv[3]

translation = pydeepl.translate(sentence, to_language, from_lang=from_language)
print(translation)

exit(0)
