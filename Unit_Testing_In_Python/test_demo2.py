import unittest
import demo2

#Test class skipleme: @unittest.skip("Why skipped")
class TestCalculate(unittest.TestCase):
    #setup method her bir testten önce ayrı ayrı çalışır
    def setUp(self):
        #repeated code
        #self ile tanımlayarak tüm classın kullanamasını sağlıyorum
        self.calculator = demo2.Calculate()
    
    #teardown method her bir test çalıştıktan sonra ayrı ayrı çalışlır
    #recourse to relase or connections to close
    def tearDown(self):
        print("After test ended..")

    #tek tek skipleme: @unittest.skipIf(True, "reason")   değer True olursa skip
    def add(self):
        #If we are testing method inside class we need to create object
        self.assertEqual(self.calculator.add(2,3), 5)

    def sub(self):
        self.assertEqual(self.calculator.sub(10,2), 8)

    #assertRaises check for if particular function raises a exception
    def div(self):
        self.assertEqual(self.calculator.div(10,5) ,2)
        #fonkiyonun hata fırlatıp fırlatmadığını kontrol ediyoruz. Ana kodda ValueError var ise test başarılı
        with self.assertRaises(ValueError): #sor
            self.calculator.div(10, 0)

if __name__ == "__main__":
    unittest.main()