import multiprocessing


class WarehouseManager:

    def __init__(self):
        self.data = {}

    def process_request(self, request):
        if request[1] == "receipt":
            try:
                self.data[request[0]] += request[2]
            except KeyError:
                self.data[request[0]] = request[2]
        elif request[1] == "shipment":
            try:
                if self.data[request[0]] - request[2] > 0:
                    self.data[request[0]] -= request[2]
                else:
                    print('Недостаточно товара')
            except KeyError:
                print('Товар не найден')

    def run(self, request):
        for i in request:
            self.process_request(i)


# Создаем менеджера склада
manager = WarehouseManager()

# Множество запросов на изменение данных о складских запасах
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

# Запускаем обработку запросов
manager.run(requests)

# Выводим обновленные данные о складских запасах
print(manager.data)
