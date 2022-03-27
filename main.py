print (format(__name__))

class new_car:
    '''initiate a new car'''
    def __init__(self,a,b,c):
        self.brand = a
        self.out_year = b
        self.manufacturer = c

a = new_car("Altis", 1992, "Toyata")

print(new_car.__doc__) #print out the comments
print(a.brand)

record=[]
record.append(a)

print(record[0].brand)

