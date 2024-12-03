class customer_data:

    def __init__(self,name,address,phone):

        self.name = name
        self.address = address
        self.phone = phone

    def set_name(self):

        return self.name 
    
    def set_address(self):

        return self.address
    
    def set_phone (self):

        return self.phone 
    
    def get_name(self):

        return self.name 
    
    def get_address(self):

        return self.address
    
    def get_phone (self):

        return self.phone 
    
class Auto_data:

    def __init__(self,make,model,year):

        self.make = make
        self.model = model
        self.year = year

    def set_name(self):

        return self.make 
    
    def set_name(self):

        return self.model
    
    def set_name(self):

        return self.year 
    
    def get_name(self):

        return self.make 
    
    def get_name(self):

        return self.model
    
    def get_name(self):

        return self.year 
    

class Customer_Quote:

    def __init__(self,parts_charges,labor_charges):

        self.parts_charges = parts_charges
        self.labor_charges = labor_charges
      
    def set_parts (self ):

        return self.parts_charges 
    
    def set_labor (self):

        return self.labor_charges 
    
    def get_parts(self):

        return self.parts_charges 
    
    def get_labor(self):

        return self.labor_charges
    
    def get_sales_tax(self,cost,tax):

        self.cost = self.labor_charges + self.parts_charges
        self.tax  = self.cost * (0.088)
        return self.tax
    
    def get_total_charges(self,total_cost):

        self.cost = self.labor_charges + self.parts_charges
        tax = self.get_sales_tax()
        self.total_cost = self.cost + tax

        return self.total_cost
    

    
    
    
    
    


        

