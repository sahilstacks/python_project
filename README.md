# Python Mini Projects Collection

A collection of interactive command-line and graphical Python projects built to practice programming fundamentals, database connectivity, GUI development, machine learning, and logic building. This repository includes Banking Software with database integration, an AI Chatbot with ML prediction, an Area Calculator for 2D/3D shapes, a Game Store Shopping Cart, and a Tkinter-based GUI Calculator.

---

## Project Overview

This repository is split into five main modules:
1. **Banking Software (`/bank`)**: A database-driven console application that allows users to create bank accounts, search user details, deposit money, and close accounts. It connects directly to a MySQL database to store and manage information.
2. **AI Chatbot (`/chat_bot`)**: A Machine Learning powered command-line chatbot built using Scikit-Learn (`CountVectorizer` + `MultinomialNB`) that responds to general queries and logs conversations directly into a MySQL database.
3. **Area Calculator (`/basic_calculator`)**: A simple program to quickly calculate the area of different shapes like Circles, Squares, Rectangles, Cubes, and Cuboids based on user input.
4. **Ryzen Game Store (`/shopping_cart`)**: An interactive shopping cart simulation of a gaming store where users can choose from a list of popular games, purchase multiple copies, and get an itemized bill showing applied discounts and GST charges.
5. **GUI Calculator (`/calculator`)**: A graphical desktop application built using Tkinter that performs basic arithmetic operations (addition, subtraction, multiplication, division) through a user-friendly interface.

---

## Features

### 1. Banking Software
* **Account Creation**: Add new customer details (account number, name, age, occupation, address, mobile number, Aadhaar number, account type, and initial deposit).
* **Multi-criteria Search**: View details of a specific customer using their Account Number, Name, Mobile Number, or Aadhaar Number, or list all customers at once.
* **Deposits**: Add money to existing accounts, keeping track of the month of deposit.
* **Close Account**: Permanently delete customer records and transactions from the database.

### 2. AI Chatbot
* **Intent Prediction**: Uses Scikit-Learn (`CountVectorizer` & `MultinomialNB`) to extract text features and predict responses from a trained dataset.
* **Conversational Knowledge Base**: Answers questions about greetings, identity, programming topics (Python, AI, ML, C, Java, HTML, CSS, JavaScript), jokes, and farewells.
* **MySQL Logging**: Automatically records every conversation (`user_message` and `bot_reply`) in a `chat_history` table within a MySQL database (`chatbot_py`).

### 3. Area Calculator
* Supports calculations for both 2D and 3D shapes:
  * **Circle**
  * **Square**
  * **Rectangle**
  * **Cube** (Total Surface Area)
  * **Cuboid** (Total Surface Area)

### 4. Ryzen Game Store Shopping Cart
* **Menu**: Displays a numbered list of games with realistic prices.
* **Quantity Selection**: Users can choose how many copies of each game they want to buy.
* **Automatic Discounts**:
  * 2.5% discount for bills between ₹5,000 and ₹9,000.
  * 12% discount for bills exceeding ₹9,000.
* **Tax Calculation**: Applies an 18% GST (split into 9% SGST and 9% CGST) on the discounted price.
* **Bill**: Displays original price, discounts, taxes, and final payable amount.

### 5. GUI Calculator
* **User-friendly Interface**: Clean desktop window built with Python's standard `tkinter` library.
* **Core Arithmetic Operations**: Quick buttons to perform Addition, Subtraction, Multiplication, and Division.

---

## Technologies Used

* **Language**: Python 3
* **Machine Learning**: Scikit-Learn (`scikit-learn`)
* **GUI Framework**: Tkinter (for GUI Calculator)
* **Database**: MySQL (for Banking and AI Chatbot modules)
* **Libraries**: `mysql-connector-python`, `scikit-learn`

---

## Future Improvements

* **Input Validation**: Add robust error handling to prevent crashes when users enter invalid data types.
* **Database Updates for Shopping Cart**: Save the Ryzen Store inventory and order logs in a MySQL database instead of hardcoding items in Python.
* **Withdrawal Feature**: Add a cash withdrawal option to the Banking module that updates and checks account balance before debiting.
* **Calculator Enhancement**: Add support for advanced mathematical operations (modulus, power, square root, etc.) and keyboard shortcuts to the GUI Calculator.