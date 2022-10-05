class Dog:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.breed = ""

class Box:
    def __init__(self, number):
        self.number = number 
        self.occupant = None 

    def put_dog(self, dog):
        if self.occupant == None:
            self.occupant = dog 
        else:
            raise Exception("Boks zajęty!")

    def remove_dog(self):
        if self.occupant != None:
            self.occupant = None
        else:
            raise Exception("Box jest pusty")
    
    def is_empty(self):
        return self.occupant == None
    
    def get_number(self):
        return self.number

    def get_occupant_str(self):
        if self.occupant:
            return str(self.occupant)
        else:
            return ""

    def get_occupant(self):
        return self.occupant


class Hotel:
    def __init__(self):
        self.boxes = []
        
    def add_box(self, box):
        self.boxes.append(box)
        
    def check_in(self, dog):
        for x in self.boxes:
            if x.is_empty():
                x.put_dog(dog)
                return True
        raise Exception("Brak wolnych boxów")
    
    def check_out(self, number):
        y = self.find_box(number)
        if y:
            y.remove_dog()
            return True
        raise Exception("Nie ma takiego numeru boxa")

    def find_box(self, number):
        for x in self.boxes:
            if x.get_number() == number:
                return x
        return None

    # def change_box(self):
    #     box1 = self.find_box(number1)
    #     box2 = self.find_box(number2)

    #     a = box1.get_occupant()
    #     box1.remove_dog()
    #     box2.put_dog(a)


    def exchange_box(self, number1, number2):

        box1 = self.find_box(number1)
        box2 = self.find_box(number2)
            
        if not box1.is_empty() and not box2.is_empty():
            a = box1.get_occupant()
            b = box2.get_occupant()

            box1.remove_dog()
            box2.remove_dog()

            box1.put_dog(b)
            box2.put_dog(a)
            
        elif not box1.is_empty() and box2.is_empty():
            a = box1.get_occupant()
            box1.remove_dog()
            box2.put_dog(a)

        elif not box2.is_empty() and box1.is_empty():
            a = box2.get_occupant()
            box2.remove_dog()
            box1.put_dog(a)
            

        # a = None
        # if not box1.is_empty():
        #     a = box1.get_occupant()
        #     box1.remove_dog()

        # b = None
        # if not box2.is_empty():
        #     b = box2.get_occupant()
        #     box2.remove_dog()

        # if not a is None:
        #     box2.put_dog(a)
        # if not b is None:
        #     box1.put_dog(b)


    def __str__(self):
        res = ""
        for x in self.boxes:
            res = res + "{}: {}\n".format(x.get_number(), x.get_occupant_str())
        return res
            




