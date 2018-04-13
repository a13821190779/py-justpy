import random
import string

chars = string.ascii_letters + string.digits


def generateFour():
    return ''.join(random.sample(chars, 4))


list = [generateFour() for x in range(1, 5)]


def generateCode(num = 4):
    index = 0
    return '-'.join([generateFour() for item in range(index, index + num)])
    
def main(count):
    return [generateCode() for item in range(count)]
    
print(main(10))