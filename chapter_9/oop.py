class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type
    
    def update_membership(self, new_membership):
        print("Calculating costs")
        # invoke api
        # update a Database
        # charge the customer
        # calculate costs
        
        
        self.membership_type = new_membership
        
customers = [Customer("Caleb", "Gold"), 
            Customer("Brad", "Bronze")]

print(customers[1].membership_type)
customers[1].membership.type = "Gold"
print(customers[1].membership_type)