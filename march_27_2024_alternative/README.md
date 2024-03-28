# Object/Class Practice with E-Commerce Factors

This Python project provides a basic framework for managing product information in an e-commerce context. You can add new products, view the existing product list, and update product details.

## Features

- Add new products with details like name, unit cost, unit price, and category
- View a list of all registered products
- Update existing product information (functionality not fully implemented yet)

## Usage

1. Clone this repository or download the files.
2. Install any required dependencies (there are currently none).
3. Run `python main.py` to start the program.

**Note:** This program uses the `os` module to clear the console screen. This functionality might not work on all operating systems.

## How it works

The project consists of two main Python files:

- `main.py`: This script drives the program and provides a user interface for interacting with product data.
- `product_class.py`: This file defines the `Products` class, which represents a product with attributes like ID, name, cost, price, and category.

The program maintains a list of `Products` objects. Users can add new products with details and view the entire product list. Currently, updating product information has basic functionality defined but is not fully implemented.

## Contributing

We welcome contributions to improve this project! You can consider adding functionalities like:

- Removing products from the list
- Implementing full product update functionality (currently updates only if a value is provided)
- Adding calculations for profit margin based on cost and price

Feel free to fork this repository and submit a pull request with your improvements!
