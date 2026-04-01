# *3. Banking Application *
# 📌 Question:
# Design a banking application: Implement a BankAccount class where account details (e.g., balance, account number) are private, and only public methods can be used to access or modify them, ensuring secure data handling.

# 📖 Explanation:
# Encapsulation using private variables.

class BankAccount:
    def __init__(self, acc_no, balance):
        self.__acc_no = acc_no
        self.__balance = balance

    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        self.__balance -= amt

    def show(self):
        print("Account:", self.__acc_no)
        print("Balance:", self.__balance)

b = BankAccount(101, 1000)
b.deposit(500)
b.withdraw(200)
b.show()
