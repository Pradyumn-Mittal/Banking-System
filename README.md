# 🏦 Banking System - Console Application in Python

A fully functional **Banking System** implemented using Python's Object-Oriented Programming (OOP) principles. This console-based application allows users to create and manage bank accounts with basic operations like deposits, withdrawals, and balance inquiries. The system uses **JSON** for persistent data storage.

## 🚀 Features

- ✅ Create new accounts with unique account numbers  
- 💵 Deposit and withdraw funds with validation  
- 🧾 Check account balance  
- 🔐 Secure file-based JSON storage for persistent data  
- 🧱 Modular design using:
  - Inheritance
  - Polymorphism
  - Encapsulation
  - Abstraction

## 📁 Project Structure

```
Banking-System/
│
├── main.py                # Entry point for the application
├── bank.py                # Core banking logic and classes
├── database.json          # Persistent storage for account data
├── utils.py               # Utility functions (e.g., input validation)
└── README.md              # Project documentation
```

## 🧠 Object-Oriented Design

This project demonstrates effective use of OOP in Python:

- `Bank` class: Handles account creation, deposits, withdrawals, and data persistence.
- `Account` class: Represents a user's bank account with private attributes and getter/setter methods.
- Interfaces and polymorphism to ensure extensibility.
- Data is securely stored in a structured `JSON` file.

## 🖥️ How to Run

### Prerequisites

- Python 3.8 or higher

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Pradyumn-Mittal/Banking-System.git
   cd Banking-System
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/b8067f99-7d4b-4b11-9598-eee7673a89c7)


## 🧪 Sample Use Case

```
1. Open a new account
2. Deposit money
3. Withdraw money
4. Check balance
5. Exit
```

## 📦 JSON Data Format (Example)

```json
{
  "10001": {
    "name": "Alice",
    "balance": 5000,
    "email": "alice@example.com"
  },
  "10002": {
    "name": "Bob",
    "balance": 2500,
    "email": "bob@example.com"
  }
}
```

## 🛠️ Future Improvements

- GUI using Tkinter or PyQt  
- Login/Authentication system  
- Transaction history log  
- Multi-user support  
- Unit testing for each module  

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## 📜 License

This project is licensed under the [MIT License](LICENSE).

## 👨‍💻 Author

**Pradyumn Mittal**  
[GitHub](https://github.com/Pradyumn-Mittal)

---

⭐ If you found this project helpful or learned something from it, give it a star!
