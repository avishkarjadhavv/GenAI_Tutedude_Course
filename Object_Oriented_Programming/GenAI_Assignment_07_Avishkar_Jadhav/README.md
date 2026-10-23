# Assignment 7: Object-Oriented Programming (OOP)

## Objective
To learn and implement the fundamental concepts of Object-Oriented Programming in Python.

## Assignment Tasks

### Task 1: Basic Class and Object Creation
Create a `Product` class with name, price, and category attributes. Implement `get_info()` and create two product objects.

### Task 2: Constructor and Encapsulation
Use a private `__price` attribute with getter and setter methods. Update the price only when the new price is greater than zero.

### Task 3: Inheritance
Create an `ElectronicProduct` subclass of `Product`, add a `warranty_years` attribute, and override `get_info()` to include warranty information.

### Task 4: Polymorphism
Create `Laptop` and `Mobile` classes that inherit from `Product`. Override `get_info()` in both classes and demonstrate polymorphism using a loop.

### Task 5: Abstraction
Create an abstract `Payment` class with an abstract `process_payment(amount)` method. Implement `CreditCardPayment` and `UPIPayment` subclasses.

### Task 6: Magic Methods and Operator Overloading
Implement `__str__()` to display product details and `__add__()` to return the combined price of two product objects.

### Task 7: Mini Inventory System
Create `Inventory` and `Store` classes to manage products, remove products, calculate total inventory value, display product information, and show the store summary.

## Project Structure

```text
GenAI_Assignment_07_Avishkar_Jadhav/
├── README.md
├── task1.ipynb
├── task2.ipynb
├── task3.ipynb
├── task4.ipynb
├── task5.ipynb
├── task6.ipynb
└── task7.ipynb
```

## Technologies Used
- Python 3
- Jupyter Notebook
- Object-Oriented Programming

## How to Run
1. Open the project folder in VS Code.
2. Open the notebook for the desired task.
3. Select a Python kernel.
4. Run the cells in order.

## Learning Outcomes
- Understand classes, objects, constructors, and attributes.
- Apply encapsulation and getter/setter methods.
- Implement inheritance and method overriding.
- Demonstrate polymorphism.
- Understand abstraction using abstract base classes.
- Use magic methods and operator overloading.
- Build a simple inventory management system using OOP concepts.