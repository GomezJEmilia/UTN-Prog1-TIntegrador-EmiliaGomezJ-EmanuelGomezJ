blue_s = chr(27)+"[0;34m"
green_s = chr(27)+"[1;32m"
red_s = chr(27)+"[;31m"

def res(en):
    print(chr(27)+"[0m"+'', end = en)

def blue(message, e = '\n'):
    print(blue_s+f'{message}', end= e )
    res(e)

def green(message, e = '\n'):
    print(green_s+f'{message}', end = e)
    res(e)

def red(message, e = '\n'):
    print(red_s+f'{message}', end= e)
    res(e)
    