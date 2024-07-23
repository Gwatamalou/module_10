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
            Customer(self, count_customer).start()
            sleep(1)

    # сразу помещаем в очередь
    # выполняется это за O(1) так же как и проверка очереди через условие поэтому так
    # Возможно я не правильно понял задачу и поток нужно было запускать из serve_customer,
    # но тогда атрибут customer получается вообще не нужен
    def serve_customer(self, customer):
        self.queue.put(customer)
        current_customer = self.queue.get()
        table = next((x for x in self.tables if x.is_busy), None)

        if not table or not self.queue.empty():
            print(f'Посетитель номер {customer.customer} ожидает свободный стол')

            while not table:
                table = next((x for x in self.tables if x.is_busy), None)

        table.is_busy = False
        print(f'Посетитель номер {current_customer.customer} сел за стол {table.number}')
        sleep(5)
        table.is_busy = True
        print(f'Посетитель номер {current_customer.customer} покушал и ушёл.')


class Customer(threading.Thread):
    def __init__(self, cafe, customer):
        super().__init__()
        self.customer = customer
        self.cafe = cafe

    def run(self):
        self.cafe.serve_customer(self)


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

cafe = Cafe(tables)

customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()

