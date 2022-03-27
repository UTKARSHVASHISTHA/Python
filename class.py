class Car:
    def __init__(self,car_company_name,car_name,car_color,car_price):
        self.car_company_name = car_company_name
        self.car_name = car_name
        self.car_color = car_color
        self.car_price = car_price

Thar = Car("Mahindra","Thar","Black","15")  #object creation
Verna=Car("Hyundai","Verna","Blsck","9")

print("Car Company Name: ",Thar.car_company_name)
print("Car Color: ",Thar.car_color)





