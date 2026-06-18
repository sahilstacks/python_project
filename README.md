# Python Mini Projects Collection

A collection of three interactive command-line Python projects built to practice programming fundamentals, database connectivity, and logic building. This repository includes a Banking Software with database integration, an Area Calculator for 2D/3D shapes, and a Game Store Shopping Cart with automatic tax and discount calculation.

---

## Project Overview

This repository is split into three main modules:
1. **Banking Software (`/bank`)**: A database-driven console application that allows users to create bank accounts, search user details, deposit money, and close accounts. It connects directly to a MySQL database to store and manage information.
2. **Area Calculator (`/basic_calculator`)**: A simple program to quickly calculate the area of different shapes like Circles, Squares, Rectangles, Cubes, and Cuboids based on user input.
3. **Ryzen Game Store (`/shopping_cart`)**: An interactive shopping cart simulation of a gaming store where users can choose from a list of popular games, purchase multiple copies, and get an itemized bill showing applied discounts and GST charges.

---

## Features

### 1. Banking Software
* **Account Creation**: Add new customer details (account number, name, age, occupation, address, mobile number, Aadhaar number, account type, and initial deposit).
* **Multi-criteria Search**: View details of a specific customer using their Account Number, Name, Mobile Number, or Aadhaar Number, or list all customers at once.
* **Deposits**: Add money to existing accounts, keeping track of the month of deposit.
* **Close Account**: Permanently delete customer records and transactions from the database.

### 2. Area Calculator
* Supports calculations for both 2D and 3D shapes:
  * **Circle**
  * **Square**
  * **Rectangle**
  * **Cube** (Total Surface Area)
  * **Cuboid** (Total Surface Area)

### 3. Ryzen Game Store Shopping Cart
* **Menu**: Displays a numbered list of games with realistic prices.
* **Quantity Selection**: Users can choose how many copies of each game they want to buy.
* **Automatic Discounts**:
  * 2.5% discount for bills between ₹5,000 and ₹9,000.
  * 12% discount for bills exceeding ₹9,000.
* **Tax Calculation**: Applies an 18% GST (split into 9% SGST and 9% CGST) on the discounted price.
* **Bill**: Displays original price, discounts, taxes, and final payable amount.

---

## Technologies Used

* **Language**: Python 3
* **Database**: MySQL (for the Banking project)
* **Libraries**: `mysql-connector-python` (used to link Python and MySQL)

---

## How to Setup and Run

### Prerequisites
Make sure you have Python installed. If you want to run the Banking project, ensure you have a MySQL server running (e.g., via XAMPP or MySQL Installer) and install the MySQL connector for Python:
```bash
pip install mysql-connector-python
```

### Steps to Run
1. **Clone the repository**:
   ```bash
   git clone https://github.com/sahilstacks/python_project.git
   cd python_project
   ```

2. **Setup the Database (for Banking Software)**:
   * Open your MySQL client (like phpMyAdmin or MySQL CLI).
   * Create a database named `bank_py`.
   * Create the `account` and `amt` tables using the database schema detailed above.

3. **Running the Programs**:
   * To run the Banking System:
     ```bash
     python bank/bank_.py
     ```
   * To run the Area Calculator:
     ```bash
     python basic_calculator/basic_area_calculator.py
     ```
   * To run the Shopping Cart:
     ```bash
     python shopping_cart/shopping_cart.py
     ```

---

## Future Improvements

* **Input Validation**: Add robust error handling to prevent crashes when users enter letters instead of numbers.
* **Database Updates for Shopping Cart**: Save the Ryzen Store inventory and order logs in a MySQL database instead of hardcoding items in Python.
* **Withdrawal Feature**: Add a cash withdrawal option to the Banking module that updates and checks account balance before debiting.