import textwrap

def wrap(string, max_width):
    result = ''
    warpper = textwrap.TextWrapper(width= max_width)
    wrapped_txt = warpper.wrap(string)
    for i in wrapped_txt:
        result += i +'\n'
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)