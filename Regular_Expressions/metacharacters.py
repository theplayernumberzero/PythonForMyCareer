import re

string = ""
pattern1 = r"ab*c" #star metacharacter: b karakteri c karakterinden önce 0 veya daha fazla kez bulunabilir
pattern2 = r"ab+c" #plus metacharacter: b karakteri c karakterinden önce en az 1 kez bulunmalı
pattern3 = r"ab{2}c"   #curly braces metacharacter: {x} ile b karakteri c den önce x defa olmalı, {x,} ile b karakteri c den önce en az x defa olmalı
pattern4 = r"ab.c"  #wildcard metacharacter: b ve c arasına herhangi bir tek karakter gelebilir
pattern5 = r"ab?c"  #optional metacharacter: b karakteri optional. abc ve ac match found olur
pattern6 = r"^90"   #caret metacharacter: ^ ardından hangi karakterler varsa onunla eşleşir (ülke kodunda kullanabilirsin)

if re.match(pattern=pattern1, string= string):
    print("Match found")
else:
    print("Match not found")