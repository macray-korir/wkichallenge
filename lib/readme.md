# Pizza Restaurant API
This is a Flask-based API for a Pizza Restaurant. The API allows you to manage restaurants, pizzas, and the association between them, along with various CRUD operations.

# Getting Started
To get started with this API, follow the instructions below.

# Prerequisites
Python 3.x
Flask
Flask-SQLAlchemy
Flask-Migrate
Installation
Clone the repository:

# API Endpoints
Get All Restaurants
URL: /restaurants

# Method: GET
Description: Get a list of all restaurants.
Response: JSON data containing restaurant details.

# Get Restaurant by ID
URL: /restaurants/<int:id>
Method: GET
Description: Get details of a specific restaurant by its ID.
Response: JSON data containing restaurant details, including associated pizzas.

# Delete Restaurant by ID
URL: /restaurants/<int:id>
Method: DELETE
Description: Delete a restaurant by its ID. Also deletes associated RestaurantPizzas.
Response: Empty response on success.

# bGet All Pizzas
URL: /pizzas
Method: GET
Description: Get a list of all pizzas.
Response: JSON data containing pizza details.
Create Restaurant Pizza
URL: /restaurant_pizzas

# Method: POST
Description: Create a new RestaurantPizza association between an existing pizza and restaurant.
Request Body: JSON data containing price, pizza_id, and restaurant_id.
Response: JSON data containing pizza details on success.

# Validations
The price of a RestaurantPizza must be between 1 and 30.
Restaurant names must be unique and less than 50 characters in length.
Required fields for creating RestaurantPizza: price, pizza_id, and restaurant_id.
Example Requests
Here are some example requests you can make to the API using tools like Postman or cURL:

# Get All Restaurants:
http
Copy code
GET http://localhost:5000/restaurants
Get Restaurant by ID (Replace <id> with an actual ID):

http
Copy code
GET http://localhost:5000/restaurants/<id>
Delete Restaurant by ID (Replace <id> with an actual ID):

http
Copy code
DELETE http://localhost:5000/restaurants/<id>
Get All Pizzas:

http
Copy code
GET http://localhost:5000/pizzas
Create Restaurant Pizza:

http
Copy code
POST http://localhost:5000/restaurant_pizzas
Request Body:


# Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make your changes and commit them.
Push your changes to your fork.
Submit a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
This API was built using Flask, Flask-SQLAlchemy, and Flask-Migrate.
Thanks to the Flask community for creating and maintaining these wonderful tools.
