import string
def print_rangoli(size):
    # your code goes here
    width = (size-1)*2 + (size*2)-1
    design = ''
    letters = list(string.ascii_letters)[:size]

    count = 1
    for i in range (0 , size):
        index = -1 
        if i < size:
            for j in range (0,count):
                if j == 0:
                    design = letters[index]
                elif j > 0 and j < (count)/2:
                    index = size-(j+1)
                    design += '-' + letters[index]
            for k in range(index+1,size):
                if index != -1:
                    design += '-' + letters[k]

            count += 2
            print(design.center(width,'-'))
    design = ''
    count -= 4
    for i in range(count,0,-2):
        for j in range ( 0 , i ):
            if j == 0:
                index = -1
                design = letters[index]
            if j < (count / 2)-1:
                index = size-(j+2)
                design += '-' + letters[index]
        
        for k in range(index+1,size):
                if index != -1:
                    design += '-' + letters[k]
        count -= 2
        print(design.center(width,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)