def bar(p):
    full = int(p // 5)
    return '█' * full + '░' * (20 - full)

def terminal_link(text, url):
    return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"