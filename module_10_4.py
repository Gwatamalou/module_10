import queue
import threading
from time import sleep


class Table:
    def __init__(self, number=int):
        self.number = number
        self.is_busy = True


class Cafe:
    def __init__(self, tables: list):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        count_customer = 0
        while count_customer < 20:
            count_customer += 1
            self.serve_customer(count_customer)
            print(f'Посетитель номер {count_customer} прибыл')
            sleep(1)

    def serve_customer(self, customer):
        while self.queue:
            for table in self.tables:
                if table.is_busy:
                    Customer(self.queue.get(), table).start()
                    break



class Customer(threading.Thread):
    def __init__(self, customer, table):
        self.customer = customer
        self.table = table
        super().__init__()

    def run(self):
        self.table.is_busy = False
        print(f'Посетитель номер {self.customer} сел за стол {self.table.number}')
        sleep(5)
        self.table.is_busy = True
        print(f'Посетитель номер {self.customer} покушал и ушёл.')


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
serve_arrival_thread = threading.Thread(target=cafe.serve_customer)
customer_arrival_thread.start()
serve_arrival_thread.start()
customer_arrival_thread.join()
serve_arrival_thread.join()
