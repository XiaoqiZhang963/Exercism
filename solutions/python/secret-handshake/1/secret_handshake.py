ACTION = ['wink',
         'double blink',
         'close your eyes',
         'jump',
         'reverse']

def commands(binary_str):
    handshake = []
    for index, num in enumerate(reversed(binary_str)):
        if num == '1':
            handshake.append(ACTION[index])
    if handshake and handshake[-1] == 'reverse':        
        handshake.pop()
        handshake.reverse()
    return handshake
