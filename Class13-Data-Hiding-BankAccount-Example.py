# Author McInventor29
class BankAccount:
    def __init__(self, money):
        self.__money = money  # The amount of money you have is PRIVATE.

    def deposit(self, money):  # This adds money to your account.
        self.__money += money

    def withdrawl(self, money):  # This takes away money from your account.
        self.__money -= money

    def get_money(self):
        print("Alert: Amount of money is being shown.")  # Alerts when the amount of money is being shown.
        return self.__money


acc = BankAccount(10000)  # Puts $10,000 in a bank account.
print(
    acc.get_money())  # This is how you're supposed to get money from your account. You would know that money is being shown.
print()

acc.deposit(500)
print(acc.get_money())
print()

acc.withdrawl(250)
try:
    print(
        acc.__money)  # A bad hacker could try to get the info like this to avoid raising the alarm, but it wouldn't work.
except AttributeError as a:
    print('You cannot get the amount of money with __money.')
    print(a)
print()

print(
    acc._BankAccount__money)  # A good hacker could try to get the money with this more complicated syntax and succeed.
# Notice that the private attribute __money was accessed without using the get_money() method.
