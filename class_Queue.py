class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Добавление элемента в конец очереди"""
        self.items.append(item)

    def dequeue(self):
        """Удаление элемента из начала очереди"""
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items.pop(0)

    def is_empty(self):
        """Проверка, пуста ли очередь"""
        return len(self.items) == 0

    def peek(self):
        """Просмотр первого элемента в очереди"""
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items[0]

    def size(self):
        """Возвращает размер очереди"""
        return len(self.items)
def process_tasks(tasks):
    """
    Моделирование обработки задач в очереди.
    tasks — список кортежей (название_задачи, время_выполнения)
    """
    queue = Queue()
    current_time = 0

    # Добавляем все задачи в очередь
    for task_name, duration in tasks:
        queue.enqueue((task_name, duration))

    print("Начало обработки задач:")
    print("-!" * 40)

    # Обрабатываем задачи по очереди
    while not queue.is_empty():
        task_name, duration = queue.dequeue()
        start_time = current_time
        end_time = current_time + duration
        current_time = end_time

        print(f"Задача: {task_name}")
        print(f"  Время начала: {start_time} минут")
        print(f"  Время выполнения: {duration} минут")
        print(f"  Время завершения: {end_time} минут")
        print()

# Пример использования
tasks = [
    ("Обработка данных", 5),
    ("Отправка отчёта", 3),
    ("Резервное копирование", 8),
    ("Обновление системы", 12),
    ("Проверка безопасности", 6)
]

process_tasks(tasks)