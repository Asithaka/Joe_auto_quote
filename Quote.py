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
    