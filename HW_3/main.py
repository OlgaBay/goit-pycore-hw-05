from collections import defaultdict
import sys


# Розбирає рядок логу на дату, час, рівень та повідомлення.
def parse_log_line(line: str) -> dict:
    log_split = line.split(" ", 3)
    valid_levels = {"INFO", "DEBUG", "ERROR", "WARNING"}

    date = log_split[0]
    time = log_split[1]
    level = log_split[2]

    if level.upper() not in valid_levels:
        raise ValueError
    
    message = log_split[3] 

    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message
    }


# Завантажує логи з файлу, пропускаючи некоректні рядки.
def load_logs(file_path: str) -> list:
    logs = []

    with open(file_path, 'r', encoding="utf-8") as file:
        for logline in file:
            log = logline.strip()

            if not log:
                continue
            try:
                parsed_log = parse_log_line(log)
                logs.append(parsed_log)
            except (IndexError, ValueError):
                print(f"\nПомилка: неправильний формат рядка логу: {log}")
        
    return logs
    

# Фільтрує записи за рівнем логування без урахування регістру.
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"].upper() == level.upper()] 


# Підраховує кількість записів для кожного рівня логування.
def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)

    for log in logs:
        level = log["level"].upper()
        counts[level] += 1

    return dict(counts)

# Виводить статистику логів у вигляді таблиці
def display_log_counts(counts: dict):
    header_level = "Рівень логування"
    header_count = "Кількість"

    width_level = len(header_level)
    width_count = len(header_count)

    print(f"\n{header_level:<{width_level}} | {header_count:<{width_count}}")
    print("-" * width_level + "-|-" + "-" * width_count)
    
    for level, count in counts.items():
        print(f"{level:<{width_level}} | {count:<{width_count}}")


if len(sys.argv) < 2:
    print("Помилка: вкажіть шлях до файлу логів.")
    sys.exit(1)

file_path = sys.argv[1]

try:
    logs = load_logs(file_path)
except FileNotFoundError:
    print("Помилка: файл не знайдено.")
    sys.exit(1)

if not logs:
    print("Помилка: не вдалося завантажити логи.")
    sys.exit(1)

counts = count_logs_by_level(logs)
display_log_counts(counts)

# Виведення деталей логів за вказаним рівнем.
if len(sys.argv) > 2:
    level = sys.argv[2]
    filtered_logs = filter_logs_by_level(logs, level)

    if not filtered_logs:
        print(f"\nЗаписів рівня {level.upper()} не знайдено.")
    else:
        print(f"\nДеталі логів для рівня {level.upper()}:")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")