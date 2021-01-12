
class func():
    name = 'addZero'

    def __init__(self):
        self.zero = 0
    
    def getZero(self):
        return self.zero

if __name__ == '__main__':
    a = func().getZero()
    print(a)