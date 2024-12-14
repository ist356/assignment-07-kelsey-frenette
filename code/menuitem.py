from dataclasses import dataclass, asdict

@dataclass
class MenuItem:
    category: str
    name: str
    price: float
    description: str

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data):
        return MenuItem(**data)
    
if __name__=='__main__':
  
    mozz = MenuItem(name = "Mozzarella Sticks", 
                    price = 8.99, 
                    category="Apps", 
                    description="Fried cheese sticks served with marinara sauce.")
    mozz.category = "Appetizers"
    print(mozz)
    print(mozz.to_dict())

    burger = MenuItem.from_dict({"name": "Burger", 
                                 "price": 9.99, 
                                 "description": "A delicious burger.", 
                                 "category": "Entrees"})
    print(burger)

