counter = 0

data = [
    0, 254, 9, 9, 9, 254, 255, 137, 137, 137, 118, 126, 129, 129, 129, 129,
    255, 129, 129, 129, 126, 255, 137, 137, 137, 137, 255, 9, 9, 9, 1,
    126, 129, 129, 145, 243, 255, 8, 8, 8, 255, 129, 129, 255, 129, 129,
    96, 128, 129, 127, 1, 255, 8, 20, 34, 193, 255, 128, 128, 128, 128,
    255, 2, 12, 2, 255, 255, 2, 60, 64, 255, 126, 129, 129, 129, 126,
    255, 9, 9, 9, 6, 126, 129, 161, 65, 190,
    255, 25, 41, 73, 134, 134, 137, 137, 137, 113, 1, 1, 255, 1, 1,
    127, 128, 128, 128, 127, 63, 96, 192, 96, 63, 127, 128, 112, 128, 127,
    195, 36, 24, 36, 195, 3, 4, 248, 4, 3, 193, 161, 145, 137, 135,
    0, 0, 0, 0, 0, 126, 161, 137, 133, 126, 132, 130, 255, 128, 128, 194, 161, 145,
    137, 134, 66, 137, 137, 137, 118, 12, 10, 137, 255, 136, 199, 137, 137, 137,
    248, 126, 137, 137, 137, 114, 1, 1, 249, 5, 2, 118, 137, 137, 137, 118,
    70, 137, 137, 137, 126]

def restore_data():
    global counter
    counter = 0


def read_data():
    global counter
    counter += 1
    return data[counter - 1]


def tab(k):
    for i in range(k):
        write(" ", "")

def space():
    for i in range(30):
        a = 0
        print_row(a)


def is_web():
    return "__BRYTHON__" in globals()

def init_console():
    if is_web():
        from browser import document
        console = document.getElementById('output')
        console.appendChild(document.createElement('p'))


def write(message="", end='\n'):
    if is_web():
        from browser import document
        console = document.getElementById('output')

        console.lastChild.textContent += message
        if end == "\n":
            console.appendChild(document.createElement('p'))
        console.scrollTop = console.scrollHeight
    else:
        print(message, end=end)


async def read():
    if is_web():
        from browser import document, aio
        inp = document.getElementById('input')
        while True:
            event = await aio.event(inp, 'keydown')
            if event.key == 'Enter':
                tmp = event.target.value
                event.target.value = ''
                write(tmp)
                return tmp
    else:
        return input()


def run(function):
    if is_web():
        from browser import aio
        aio.run(function())
    else:
        import asyncio
        asyncio.run(function())

def print_row(A):
    for i in range(8):
        if A < 128:
            write(" ", "")
        else:
            write("*", "")
            A = A - 128
        A = A * 2
    write()

async def ticket():
    init_console()
    tab(24)
    write("TICKERTAPE")
    tab(20)
    write("CREATIVE COMPUTING")
    tab(18)
    write("MORRISTOWN, NEW JERSEY")

    write()
    write()
    write()

    write("? ", "")
    a_inp = str(await read())
    space()

    for n in range(len(a_inp)):
        b = ord(a_inp[n])
        if b > 90:
            b = 27
        elif b < 65:
            if b > 57 or b < 48:
                b = 27
            else:
                b = b - 20
        else:
            b = b - 64

        for s in range((b - 1) * 5 + 1):
            a = read_data()

        for s in range(5):
            a = read_data()
            print_row(a)

        a = 0
        print_row(a)
        restore_data()

    space()


run(ticket)