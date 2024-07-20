from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
print(time_end-time_start)

first_thread = Thread(target=write_words, args=(10, 'example5.txt'))
second_thread = Thread(target=write_words, args=(30, 'example6.txt'))
third_thread = Thread(target=write_words, args=(200, 'example7.txt'))
fourth_thread = Thread(target=write_words, args=(100, 'example8.txt'))

time_start = datetime.now()

first_thread.start()
second_thread.start()
third_thread.start()
fourth_thread.start()

first_thread.join()
second_thread.join()
third_thread.join()
fourth_thread.join()

time_end = datetime.now()

print(time_end-time_start)

