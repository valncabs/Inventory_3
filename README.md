# Inventory Management System

## Description

This project is a simple inventory system made in Python.
It allows the user to manage products using basic operations like add, show, search, update, and delete.

The program also works with CSV files to save and load data.

---

## Features

* Add a product
* Show all products
* Search a product
* Update a product
* Delete a product
* Show statistics
* Save data to CSV
* Load data from CSV
* Merge or overwrite inventory

---

## Project Structure


* main.py → main program with menu
* services.py → functions for inventory (CRUD and statistics)
* file_manager.py → functions for CSV files

---

## Data Structure

Each product is stored like this:

{
"name": string,
"price": float,
"quantity": int
}

---

## How to Run

1. Open the project folder
2. Run the program:

python main.py

---

## CSV Format

The CSV file must have this format:

name,price,quantity
Laptop,2500,2
Mouse,50,5

---

## Validations

* Price must be a number ≥ 0
* Quantity must be an integer ≥ 0
* Invalid rows are ignored
* The program does not stop on errors

---

## Notes

* When loading a file, the user can:

  * Overwrite the inventory
  * Merge with current data

---


