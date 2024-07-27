import multiprocessing as mp


class WarehouseManager:

    def __init__(self):
        self.data = {}

    def process_request(self, request, data, lock):
        with lock:
            if request[1] == 'receipt':
                try:
                    data[request[0]] += request[2]
                except KeyError:
                    data[request[0]] = request[2]
            elif request[1] == "shipment":
                try:
                    if data[request[0]] - request[2] > 0:
                        data[request[0]] -= request[2]
                except KeyError:
                    print('Товар не найден')

    def run(self, requests):
        process = []
        with mp.Manager() as manager:
            requestDict = manager.dict()
            for request in requests:
                p = mp.Process(target=self.process_request, args=(request, requestDict, lock,))
                p.start()
                p.join()
            self.data.update(requestDict)


if __name__ == '__main__':
    lock = mp.Lock()

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
