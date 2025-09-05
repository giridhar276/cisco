
class Marks:
    def __init__(self,marks,subject):
        print("Inside constructor ( __init__) ")
        self.marks = marks
        self.subject = subject

    def __str__(self):
        print("Inside constructor (  __str__) ")
        return 'Total marks %d obtained in %s ' %(self.marks,self.subject)
        #return 'Total marks' + str(self.marks) + 'obtained in' + self.subject

    def __add__(self,other):
        print("Inside constructor ( __add__) ")
        return Marks(self.marks + other.marks,self.subject + ',' +  other.subject)



m1 = Marks(80,"Maths")
m2 = Marks(85,"Science")
m3 = Marks(75,"English")
m4 = Marks(83,"French")
m5 = Marks(82,"Geography")

# m1 or m2 or m3 are user defined objects

print( m1 + m2 + m3 + m4 + m5 )



