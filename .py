import uuid

# Base User class
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def __str__(self):
        return f"{self.role}: {self.username}"

# Customer class
class Customer(User):
    def __init__(self, username):
        super().__init__(username, "Customer")

# Business Owner class
class BusinessOwner(User):
    def __init__(self, username):
        super().__init__(username, "BusinessOwner")
        self.products = []

    def add_product(self, product):
        self.products.append(product)

# Delivery Agent class
class DeliveryAgent(User):
    def __init__(self, username):
        super().__init__(username, "DeliveryAgent")
        self.assigned_orders = []

# Admin class
class Admin(User):
    def __init__(self, username):
        super().__init__(username, "Admin")

# Product class
class Product:
    def __init__(self, name, price):
        self.id = str(uuid.uuid4())[:8]
        self.name = name
        self.price = price

# Order class
class Order:
    def __init__(self, customer, product):
        self.id = str(uuid.uuid4())[:8]
        self.customer = customer
        self.product = product
        self.status = "Pending"
        self.delivery_agent = None

    def assign_agent(self, agent):
        self.delivery_agent = agent
        agent.assigned_orders.append(self)
        self.status = "Out for Delivery"

    def update_status(self, status):
        self.status = status

    def __str__(self):
        return f"OrderID: {self.id}, Product: {self.product.name}, Customer: {self.customer.username}, Status: {self.status}"

# System Controller
class DeliverySystem:
    def __init__(self):
        self.customers = []
        self.business_owners = []
        self.delivery_agents = []
        self.admins = []
        self.orders = []

    def register_user(self, username, role):
        if role == "Customer":
            user = Customer(username)
            self.customers.append(user)
        elif role == "BusinessOwner":
            user = BusinessOwner(username)
            self.business_owners.append(user)
        elif role == "DeliveryAgent":
            user = DeliveryAgent(username)
            self.delivery_agents.append(user)
        elif role == "Admin":
            user = Admin(username)
            self.admins.append(user)
        else:
            raise ValueError("Invalid role")
        return user

    def place_order(self, customer, product):
        order = Order(customer, product)
        self.orders.append(order)
        return order

    def assign_delivery(self, order, agent):
        order.assign_agent(agent)

    def show_orders(self):
        for order in self.orders:
            print(order)

# Example usage
if __name__ == "__main__":
    system = DeliverySystem()

    # Register users
    cust = system.register_user("erin_customer", "Customer")
    owner = system.register_user("eshita_owner", "BusinessOwner")
    agent = system.register_user("agent1", "DeliveryAgent")
    admin = system.register_user("admin1", "Admin")

    # Business owner adds product
    product1 = Product("Necklace", 1500)
    owner.add_product(product1)

    # Customer places order
    order1 = system.place_order(cust, product1)

    # Admin assigns delivery agent
    system.assign_delivery(order1, agent)

    # Delivery agent delivers
    order1.update_status("Delivered")

    # Show all orders
    system.show_orders()
