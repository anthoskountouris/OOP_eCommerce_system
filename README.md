# OOP_eCommerce_system

The program allows the user to:
- add products
- remove products
- show a summary of their shopping session
- export the content of the shopping cart in JSON format

## Parent Class - Product
- name: a String value
- price: a Float value
- quantity: an Integer value
- unique identifier: a String value that is a 13 digit sequence. Allowed digits in the sequence go from 0 to 9. The identifier must be unique for each product
- brand: a String value

## to json() method
The class Product offers a to json() method that returns the JSON-formatted representation of the product. 

## Subclasses
### Clothing
- size
- material

### Food
- expiry date
- gluten free
- suitable for vegans

### Laptop
- processor
- operating_system
- Storage Capacity

## The shopping system
### ShoppingCart Class - container of products in a shopping session

- addProduct(p) - to add a product p to the cart
- removeProduct(p) - to remove the product p from the cart
- getContents() - to obtain the contents of the cart, which should be returned in alphabetical order of product name
- changeProductQuantity(p, q) - to change the quantity of product p to the quantity q

## Doing some shopping
The script supports the following commands:
- A - allows the user to add a product to the cart.
- R - allows the user to remove an existing product from the shopping chart. This lets the user specify exactly what product to remove, without any ambiguity whatsoever. If no such product is present, no removal should take place.
- S - prints out a formatted text summary of the cart, with an easy-to-read list with product names, quantities, partial sums per product type and total sum. The list is ordered alphabetically by product name. Note that this command does not generate JSON, for that we have command E below.
- Q - the user can directly change the quantity of a product already present in the cart. This, like the R option, lets the user specify a product without ambiguity and, if no product is found, no changes should take place.
- E - generates a summary of the cart as a JSON-formatted data dump, printed to the console. This output is an array of JSON representations of each product.
- T - the script terminates.
- H - a request for help from the user. The commands that the program recognises are printed
out to the console.
