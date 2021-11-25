def argumenty(*argList):
    def inner_decorator(func):
        def wrapped(*args, **kwargs):
            numOfFuncArgs = len(func.__code__.co_varnames)
            numOfPassedArgs = len(args) - 1
            additionalArgs = []

            for i in range(numOfFuncArgs - numOfPassedArgs):
                if i < len(argList[0]):
                    additionalArgs.append(argList[0][i])
                else:
                    raise TypeError(func.__name__ + " () takes exactly " + str(numOfFuncArgs) + " arguments")

            func.__defaults__ = tuple(additionalArgs)

            toPassTuple = args[1:]
            response = func(*toPassTuple)
            if response is None and len(argList[0]) > numOfFuncArgs - numOfPassedArgs:
                response = argList[0][numOfFuncArgs - numOfPassedArgs]

            return response
        return wrapped

    return inner_decorator


class Operacje:
    argumentySuma=[4,5]
    argumentyRoznica=[4,5,6]

    @argumenty(argumentySuma)
    def suma(a,b,c):
        print("%d+%d+%d=%d" % (a,b,c,a+b+c))

    @argumenty(argumentyRoznica)
    def roznica(x,y):
        print("%d-%d=%d" % (x,y,x-y))

    def __setitem__(self, key, value):
        if key == "suma":
            Operacje.argumentySuma = value
            return self.argumentySuma
        elif key == "roznica":
            Operacje.argumentyRoznica = value
            return self.argumentyRoznica

    def __getitem__(self, item):  # np.  op['suma'] = [1, 2]
        if item == "suma":
            return self.argumentySuma
        elif item == "roznica":
            return self.argumentyRoznica

if __name__ == '__main__':

    op=Operacje()
    op.suma(1,2,3) #Wypisze: 1+2+3=6
    op.suma(1,2) #Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
    op.suma(1) #Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'
    try:
        op.suma() #TypeError: suma() takes exactly 3 arguments (2 given)
    except TypeError as e:
        print("Error " + str(e))

    op.roznica(2,1) #Wypisze: 2-1=1
    op.roznica(2) #Wypisze: 2-4=-2
    wynik = op.roznica() #Wypisze: 4-5=-1
    print(wynik) #Wypisze: 6

    #Zmiana zawartości listy argumentów dekoratora  dla metody 'suma'
    op['suma']=[1,2]
    #oznacza, że   argumentySuma=[1,2]

    #Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
    op['roznica']=[1,2,3]
    #oznacza, że   argumentyRoznica=[1,2,3]