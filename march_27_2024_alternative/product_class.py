class Products:
    def __init__(self, product_id, product_name, unit_cost, unit_price, category):
        self.product_id = product_id
        self.product_name = product_name
        self.unit_cost = unit_cost
        self.unit_price = unit_price
        self.category = category
    # add
    # remove
        
    # Update
    
    def update(self, product_id=None, product_name=None, unit_cost=None, unit_price=None, category=None):
        # Checks if there is value. If there is None doesn't update.
        if product_id:
            self.product_id = product_id
        if product_name:
            self.product_name = product_name
        if unit_cost:
            self.unit_cost = unit_cost
        if unit_price:
            self.unit_price = unit_price
        if category:
            self.category = category
        
    # Display
    def __str__(self):
        return f"Product ID: {self.product_id}, Product Name: {self.product_name}, Unit Cost: {self.unit_cost}, Unit Price: {self.unit_price}, Category: {self.category}\n"

