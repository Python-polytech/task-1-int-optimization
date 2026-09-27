# Диапазон оптимизации выделения памяти под объекты int

Программа находит диапозон чисел, которые в CPython хранятся в закешированном виде.

### 1. Клонирование репозитория
```bash
git clone https://github.com/Python-polytech/task-1-int-optimization.git
cd task-1-int-optimization
```

### 2. Создание и запуск виртуального окружения
#### Для Windows:
```bash
# Создание окружения
python -m venv venv
# Активация окружения
.\venv\Scripts\activate
```

#### Для macOS и Linux:
```bash
# Создание окружения
python3 -m venv venv
# Активация окружения
source venv/bin/activate
```

## Запуск
В директории **task-1-int-optimization/** выполнить команду
```bash
python main.py
```

После запуска программы в консоль будет выведен отрезок кешируемых чисел. 
