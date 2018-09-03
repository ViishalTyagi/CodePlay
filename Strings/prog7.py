strg = 'X-DSPAM-Confidence: 0.8475 '
print(strg)
var = strg.find(':')
print('Postion of colon is:', var)
getstr = strg[ var+1 : ]
print(getstr)
value = float(getstr)
print(value)
        