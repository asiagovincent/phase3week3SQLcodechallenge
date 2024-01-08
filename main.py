
from models import Restaurant, Customer, Review, session

# Create sample data
restaurant1 = Restaurant(name='Restaurant A', price=3)
restaurant2 = Restaurant(name='Restaurant B', price=4)

customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Doe')

review1 = Review(restaurant=restaurant1, customer=customer1, star_rating=5)
review2 = Review(restaurant=restaurant2, customer=customer1, star_rating=4)
review3 = Review(restaurant=restaurant1, customer=customer2, star_rating=3)

session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2, review3])
session.commit()

# Test methods
print("All Reviews for Restaurant A:")
print(restaurant1.all_reviews())

print("\nFanciest Restaurant:")
print(Restaurant.fanciest().name)

print("\nFull Name of Customer 1:")
print(customer1.full_name())

print("\nFavorite Restaurant of Customer 1:")
print(customer1.favorite_restaurant().name)
