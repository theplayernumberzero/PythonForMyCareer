#Bu sınıflar, bir grup karakteri temsil eder ve bunlara genellikle köşeli parantezler [] içinde yer verilir.

import re

#match python or Python
string = ""
pattern1 = r"[Pp]ython" #olabilecek ihtimalleri [] içine yaz
pattern2 = r"[a-z]" #a dan z ye karakterler kullanan hepsi için geçerli

if re.match(pattern=pattern1, string= string):
    print("Match found")
else:
    print("Match not found")