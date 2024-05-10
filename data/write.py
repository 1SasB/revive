import docx2txt
import json
text = docx2txt.process('west-african-herbal-pharmacopoeiaok-neat.docx')

with open("textt.txt", "w", encoding="utf-8") as f:
    f.write(text)