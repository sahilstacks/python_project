# Python Mini Projects Collection

A collection of interactive command-line and graphical Python projects built to practice programming fundamentals, database connectivity, GUI development, and logic building. This repository includes a Banking Software with database integration, an Area Calculator for 2D/3D shapes, a Game Store Shopping Cart, and a Tkinter-based GUI Calculator.

---

## Project Overview

This repository is split into four main modules:
1. **Banking Software (`/bank`)**: A database-driven console application that allows users to create bank accounts, search user details, deposit money, and close accounts. It connects directly to a MySQL database to store and manage information.
2. **Area Calculator (`/basic_calculator`)**: A simple program to quickly calculate the area of different shapes like Circles, Squares, Rectangles, Cubes, and Cuboids based on user input.
3. **Ryzen Game Store (`/shopping_cart`)**: An interactive shopping cart simulation of a gaming store where users can choose from a list of popular games, purchase multiple copies, and get an itemized bill showing applied discounts and GST charges.
4. **GUI Calculator (`/calculator`)**: A graphical desktop application built using Tkinter that performs basic arithmetic operations (addition, subtraction, multiplication, division) through a user-friendly interface.

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

### 4. GUI Calculator
* **User-friendly Interface**: Clean desktop window built with Python's standard `tkinter` library.
* **Core Arithmetic Operations**: Quick buttons to perform Addition, Subtraction, Multiplication, and Division.

---

## Technologies Used

* **Language**: Python 3
* **GUI Framework**: Tkinter (for GUI Calculator)
* **Database**: MySQL (for the Banking project)
* **Libraries**: `mysql-connector-python` (used to link Python and MySQL)

---

## Future Improvements

* **Input Validation**: Add robust error handling to prevent crashes when users enter letters instead of numbers.
* **Database Updates for Shopping Cart**: Save the Ryzen Store inventory and order logs in a MySQL database instead of hardcoding items in Python.
* **Withdrawal Feature**: Add a cash withdrawal option to the Banking module that updates and checks account balance before debiting.
* **Calculator Enhancement**: Add support for advanced mathematical operations (modulus, power, square root, etc.) and keyboard shortcuts to the GUI Calculator.