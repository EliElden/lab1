import time
import os

RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
CLEAR_CMD = 'cls' if os.name == 'nt' else 'clear'

def swiss_flag():
    print("--- Задание 1: Флаг Швейцарии ---")
    height = 15
    width = 30
    
    for y in range(height):
        line = ''
        for x in range(width):
            in_vertical = (12 <= x <= 17) and (3 <= y <= 11)
            in_horizontal = (6 <= x <= 23) and (6 <= y <= 8)
            
            if in_vertical or in_horizontal:
                line += f'{WHITE} {END}'
            else:
                line += f'{RED} {END}'
        print(line)
    print()

def draw_double_ring_pattern(repeat_x=3, repeat_y=2):
    print("--- Задание 2: Узор (j) ---")
    pattern = [
        "   ████      ████   ",
        " ██    ██  ██    ██ ",
        "██      ████      ██",
        "██      ████      ██",
        " ██    ██  ██    ██ ",
        "   ████      ████   "
    ]
    
    for _ in range(repeat_y):
        for line in pattern:
            # Множим строку шаблона на количество повторений по горизонтали + отступ
            print((line + "  ") * repeat_x)
        print()

def draw_graph_y_eq_x_over_3():
    print("--- Задание 3: График y = x / 3 ---")
    height = 10
    width = 30
    
    grid = [[' ' for _ in range(width + 1)] for _ in range(height + 1)]
    
    for y in range(height + 1):
        grid[y][0] = '|'
    for x in range(width + 1):
        grid[height][x] = '-'
    grid[height][0] = '+'
    
    for y in range(height):
        x = 3 * y
        if 0 <= x <= width:
            row_idx = height - y 
            grid[row_idx][x] = '*'

    for row in grid:
        print(''.join(row))
    print("  0" + " " * 27 + "X\n")

def read_sequence_and_draw_pie(path='sequence.txt', bar_width=40):
    print("--- Задание 4: Диаграмма последовательности ---")
    counts = {'in_range': 0, 'out_range': 0}
    total = 0

    try:
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                s = line.strip()
                if not s:
                    continue
                try:
                    val = float(s.split()[-1])
                    total += 1
                    if -3.0 <= val <= 3.0:
                        counts['in_range'] += 1
                    else:
                        counts['out_range'] += 1
                except ValueError:
                    continue
                    
        if total == 0:
            print("Файл не содержит подходящих чисел.")
            return

        pct_in = counts['in_range'] / total * 100
        pct_out = counts['out_range'] / total * 100

        print(f"Всего чисел: {total}")
        print(f"В диапазоне [-3, 3]: {counts['in_range']} ({pct_in:.1f}%)")
        print(f"Остальные: {counts['out_range']} ({pct_out:.1f}%)")

        in_blocks = int(round(pct_in / 100 * bar_width))
        out_blocks = bar_width - in_blocks

        bar = "#" * in_blocks + "-" * out_blocks
        print(f"\nДиаграмма:\n[{bar}]\n")
        
    except FileNotFoundError:
        print(f"Ошибка: Файл '{path}' не найден.\n")

def simple_animation_demo():
    print("--- Допзадание: Анимация ---")
    print("Запуск анимации через 2 секунды...")
    time.sleep(2)
    
    frames = [
        "   ( •_•)   \n   ( > )>○  \n    / \\     ",
        "   ( •_•)   \n   ( > )> ○ \n    / \\     ",
        "   ( •_•)   \n   ( > )>  ○\n    / \\     ",
        "   ( •_•)   \n   ( > )> ○ \n    / \\     "
    ]
    
    try:
        for _ in range(4):
            for frame in frames:
                os.system(CLEAR_CMD)
                print(frame)
                time.sleep(0.3)
    except KeyboardInterrupt:
        pass
    finally:
        os.system(CLEAR_CMD)
        print("Анимация завершена!")

if __name__ == '__main__':
    swiss_flag()
    draw_double_ring_pattern()
    draw_graph_y_eq_x_over_3()
    read_sequence_and_draw_pie()
    # Раскомментировать строку ниже, чтобы запустить анимацию
    #simple_animation_demo()