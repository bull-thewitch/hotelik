import unittest
import hotel_obj

class TestBox(unittest.TestCase):
    def test_init(self):
        b = hotel_obj.Box(1)
        self.assertEqual(b.number, 1, "Numer boksu")
        self.assertIsNone(b.occupant, "Mieszkaniec")


    def test_put_dog(self):
        b = hotel_obj.Box(1)
        d = "Koma"
        b.put_dog(d)
        self.assertEqual(b.occupant, d, "Nie ma Komy")

        d2 = "Mimi"
        self.assertRaises(Exception, b.put_dog, **{"dog": d2})
        self.assertEqual(b.occupant, d)

    def test_remove_dog(self):
        d = "Koma"
        b = hotel_obj.Box(1)
        self.assertRaises(Exception, b.remove_dog)
        b.put_dog(d)
        b.remove_dog()
        self.assertIsNone(b.occupant, "Piesek")
    
    def test_is_empty(self):
        d = "Pirat"
        b = hotel_obj.Box(1)
        self.assertTrue(b.is_empty(), "Pełny")
        b.put_dog(d)
        self.assertFalse(b.is_empty(), "Pusty")
    

    def test_get_number(self):
        b = hotel_obj.Box(1)
        self.assertEqual(b.get_number(), 1)
        
    
    def test_get_occupant_str(self):
        d = "Koma"
        b = hotel_obj.Box(1)
        self.assertEqual(b.get_occupant_str(), "")
        b.put_dog(d)
        self.assertEqual(b.get_occupant_str(), d)
        

    def test_get_occupant(self):
        d = "Koma"
        b = hotel_obj.Box(1)
        b.put_dog(d)
        self.assertEqual(b.get_occupant(), d)

class TestHotel(unittest.TestCase):
    def test_init(self):
        h = hotel_obj.Hotel()
        self.assertEqual(h.boxes, [])
    
    def test_add_box(self):
        h = hotel_obj.Hotel()
        b = hotel_obj.Box(1) 
        self.assertEqual(h.boxes, [])
        h.add_box(b)
        self.assertEqual(h.boxes, [b])

    def test_check_in(self):
        h = hotel_obj.Hotel()
        #for i in range(3):
            #h.add_box hotel_obj.Box(i+1))
        p = ["Koma", "Mimi", "Majlo", "Pirat"]
        for i in range(3):
            h.add_box(hotel_obj.Box(i+1))
            h.check_in(p[i])
            self.assertEqual(h.boxes[i].get_occupant_str(), p[i])

        #h.check_in(p[0])
        #self.assertEqual(h.boxes[0].get_occupant_str(), p[0])
        #h.check_in(p[1])
        #self.assertEqual(h.boxes[1].get_occupant_str(), p[1])
        #h.check_in(p[2])
        #self.assertEqual(h.boxes[2].get_occupant_str(), p[2])

        self.assertRaises(Exception, h.check_in, **{"dog": p[3]})
        h.check_out(2)
        h.check_in(p[3])
        self.assertEqual(h.boxes[1].get_occupant_str(), p[3])


    #def test_check_out(self):
    #   h = hotel_obj.Hotel()
    #    for i in range(5):
    #       h.check_in hotel_obj.Dog(i+1))
    #       h.check_out(h.boxes[i])
    #       self.assertEqual(h.boxes[i].remove_dog(), )

    def test_check_out(self):
        h = hotel_obj.Hotel()
        for i in range(3):
            b = hotel_obj.Box(i+1)
            h.add_box(b)
        
        p = ["Koma", "Mimi", "Majlo", "Czujnik"]
        for i in range(3):
            h.check_in(p[i])

        h.check_out(1)
        self.assertTrue(h.boxes[0].is_empty(), "Box nie jest pusty")

        self.assertRaises(Exception, h.check_out, **{"number": 1})

        self.assertRaises(Exception, h.check_out, **{"number": 9}) 

    
    def test_find_box(self):
        h = hotel_obj.Hotel()
        b = hotel_obj.Box(1)
        h.add_box(b)
        self.assertEqual(h.find_box(1), b)

        self.assertIsNone(h.find_box(2))

    def test_exchange_box(self):
        h = hotel_obj.Hotel()
        h.add_box(hotel_obj.Box(1))
        h.add_box(hotel_obj.Box(2))

        h.check_in("Koma")
        h.exchange_box(1, 2)
        self.assertEqual(h.boxes[1].get_occupant(), "Koma")
        self.assertTrue(h.boxes[0].is_empty()) 

        h.exchange_box(1, 2)
        self.assertTrue(h.boxes[1].is_empty())
        self.assertEqual(h.boxes[0].get_occupant(), "Koma")

        h.check_in("Mimi")
        h.exchange_box(1, 2)
        self.assertEqual(h.boxes[0].get_occupant(), "Mimi")
        self.assertEqual(h.boxes[1].get_occupant(), "Koma")



    def test_str(self):
        h = hotel_obj.Hotel()
        b = hotel_obj.Box(1)
        h.add_box(b)
        h.check_in("Koma")
        self.assertEqual(h.__str__(), "1: Koma\n")



        
        
            




        



    
        









#if __name__ == "main":
unittest.main()
