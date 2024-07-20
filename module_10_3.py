from threading import Thread, Lock

lock = Lock()
class BankAccount(Thread):
    def __init__(self):
        super().__init__()
        self.balance = 1000

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, new balance is {self.balance}')

    def withdraw(self, amount):
        self.balance -= amount
        print(f'Withdrew {amount}, new balance is {self.balance}')


def deposit_task(account, amount):
    lock.acquire()
    for _ in range(5):
        account.deposit(amount)
    lock.release()

def withdraw_task(account, amount):
    lock.acquire()
    for _ in range(5):
        account.withdraw(amount)
    lock.release()

account = BankAccount()

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
