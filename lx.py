#!/usr/bin/env python
import requests
import string
import time

response            = requests.get("https://gist.githubusercontent.com/Jekiwijaya/0b85de3b9ff551a879896dd78256e9b8/raw/e9d58da5d4df913ad62e6e8dd83c936090ee6ef4/gistfile1.txt")
lex                 = list(str(response.text))

result = []
for char in lex:
    if char not in result:
        result.append(char)
lex = list("".join(result))

print("Removed duplicate", "".join(lex))

u = True
i = 0
asc = 97


for e in range(1,len(lex)-1):
    if chr(asc) == lex[0]:
        asc +=1
    hold = chr(asc)
    lex[lex.index(hold)] = lex[e]
    lex[e] = hold
    print("Possible lexicograph",i, "".join(lex))        
    i += 1
    asc += 1
