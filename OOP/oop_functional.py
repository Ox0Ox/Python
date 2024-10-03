class Flight():
    def __init__(self, capacity):
        self.c = capacity
        self.p = []

    def addpass(self, a):
        if len(self.p) < self.c:
            self.p.append(a)
            return True
        else:
            return False

f = Flight(3)
print(f.c)

l = ['harry', 'chicken', 'mutton', 'gluten', 'mutton1']

for i in l:
    
    if f.addpass(i):
        print('Trying to add: ',i)
    else:
        print('Maximum capacity reached, can no longer add', i)
        print('')
        break



def decorate(f):
    def wrapper():
        print("Something is happening before the function is called.")
        f()
        print('Functioning is done')

    return wrapper

@decorate
def l():
    print('LL')

l()


def f1(person):
    return person['house']


lis = [{'name':'harry', 'house':'blue', 'job':'amazing'},{'name':'larry', 'house':'yellow', 'job':'bad'},{'name':'sorry', 'house':'cyan', 'job':'lovely'}]
lis.sort(key=f1)
print(lis)




lis1 = [{'name':'harry', 'house':'blue', 'job':'amazing'},{'name':'larry', 'house':'yellow', 'job':'bad'},{'name':'sorry', 'house':'cyan', 'job':'lovely'}]
lis1.sort(key= lambda person: person['name'])
print(lis)
