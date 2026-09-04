CODE = {'black': 0,
'brown': 1,
'red': 2,
'orange': 3,
'yellow': 4,
'green': 5,
'blue': 6,
'violet': 7,
'grey': 8,
'white': 9}

def label(colors):
    digit = CODE[colors[0]]*10 + CODE[colors[1]]
    multiplier = 10**CODE[colors[2]]
    value = digit * multiplier
    if value == 0:
        return '0 ohms'
    if value%10**9 == 0:
        return str(value//10**9) + ' gigaohms'
    if value%10**6 == 0:
        return str(value//10**6) + ' megaohms'
    if value%1000 == 0:
        return str(value//1000) + ' kiloohms'
    else:
        return str(value) + ' ohms'
