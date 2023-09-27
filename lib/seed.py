from faker import Faker
import random
from app import app, db, Pizza, Restaurant, RestaurantPizza

fake = Faker()

with app.app_context():
    db.create_all()
    db.session.query(RestaurantPizza).delete()
    db.session.query(Pizza).delete()
    db.session.query(Restaurant).delete()
    pizzas = []
    for i in range(10):
        pizza = Pizza(name=fake.word(), ingredients=fake.sentence())
        pizzas.append(pizza)
    db.session.add_all(pizzas)
    
    restaurants = []
    for i in range(5):
        restaurant = Restaurant(name=fake.company(), address=fake.address())
        restaurant.pizzas.extend(random.sample(pizzas, random.randint(1, 5)))
        restaurants.append(restaurant)
    db.session.add_all(restaurants)
    

    restaurant_pizzas = []
    for restaurant in restaurants:
        for pizza in restaurant.pizzas:
            restaurant_pizza = RestaurantPizza(price=random.uniform(1, 30), pizza_id=pizza.id, restaurant_id=restaurant.id)
            restaurant_pizzas.append(restaurant_pizza)
    db.session.add_all(restaurant_pizzas)
    
    db.session.commit()
    print("Seeding completed.")
