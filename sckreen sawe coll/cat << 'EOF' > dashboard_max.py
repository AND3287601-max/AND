cat << 'EOF' > dashboard_max.py
import os
import sys
import time
import random
import math

GASTER_CHARS = ['☠', '⚡', '✈', '✖', '☤', '☥', '☦', '☧', '☨', '☩', '☪', '☫', '☬', '☭', '☮', '☯', '☰', '☱', '☲', '☳', '☴', '☵', '☶', '☷', '☸', '☹', '☺', '☻', '☼', '☽', '☾', '♠', '♡', '♢', '♣', '♤', '♥', '♦', '♧', '♨', '♩', '♪', '♫', '♬']

BAR_VALS = [50, 70, 30]
BAR_TARGETS = [50, 70, 30]
BAR_TIMERS = [0, 0, 0]

# УВЕЛИЧЕННЫЕ РАЗМЕРЫ ГРАФИКА
GRAPH_HEIGHT = 12
GRAPH_WIDTH = 50
graph_matrix = [[" " for _ in range(GRAPH_WIDTH)] for _ in range(GRAPH_HEIGHT)]

def get_gradient_color(factor, text):
    r = int(128 + 127 * math.sin(factor * math.pi))
    g = int(50 + 200 * math.cos(factor * math.pi))
    b = int(200 + 55 * math.sin(factor * math.pi + math.pi/2))
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

def generate_new_chart():
    global graph_matrix
    graph_matrix = [[" " for _ in range(GRAPH_WIDTH)] for _ in range(GRAPH_HEIGHT)]
    last_v = GRAPH_HEIGHT // 2
    for w in range(GRAPH_WIDTH):
        # Делаем шаги более размашистыми для выразительности курса
        move = random.choice([-2, -1, 0, 1, 2])
        new_v = last_v + move
        if new_v < 0: new_v = 0
        if new_v >= GRAPH_HEIGHT: new_v = GRAPH_HEIGHT - 1

        if new_v > last_v:
            graph_matrix[last_v][w] = "/"
        elif new_v < last_v:
            graph_matrix[last_v][w] = "\\"
        else:
            graph_matrix[last_v][w] = "_"
        last_v = new_v

generate_new_chart()
current_draw_col = 0
last_graph_update = time.time()
start_time = time.time()

# Скрыть курсор и очистить экран
sys.stdout.write("\033[?25l\033[2J")
sys.stdout.flush()

try:
    while True:
        current_time = time.time()
        elapsed_graph = current_time - last_graph_update

        # 1. Логика полосок
        for i in range(3):
            if BAR_TIMERS[i] <= 0:
                BAR_TARGETS[i] = random.randint(1, 100)
                BAR_TIMERS[i] = random.choice([15, 30])
            else:
                BAR_TIMERS[i] -= 1

            diff = BAR_TARGETS[i] - BAR_VALS[i]
            if diff != 0:
                step = int(diff / 3)
                if step == 0 and diff > 0: step = 1
                if step == 0 and diff < 0: step = -1
                BAR_VALS[i] += step

        # 2. Перерисовка графика раз в 30 сек
        if elapsed_graph >= 30:
            last_graph_update = current_time
            generate_new_chart()
            current_draw_col = 0

        # Увеличили скорость прорисовки, так как график стал шире
        if current_draw_col < GRAPH_WIDTH:
            current_draw_col += 2
            if current_draw_col > GRAPH_WIDTH:
                current_draw_col = GRAPH_WIDTH

        # Бегущая строка Гастера
        gaster_line = " ".join(random.choice(GASTER_CHARS) for _ in range(32))

        # Очистка и вывод в начало
        out = "\033[H"
        out += get_gradient_color(0.1, "=========================================================================================\n")
        out += get_gradient_color(0.2, f"    METRICS SYSTEM v10.0 // BIG LIVE CRYPTO PLOTTER // HEIGHT: {GRAPH_HEIGHT} ROWS              \n")
        out += get_gradient_color(0.3, "=========================================================================================\n\n")

        # Вывод интерфейса (высота подстроена под увеличенный график)
        TOTAL_ROWS = max(14, GRAPH_HEIGHT + 2)
        for h in range(TOTAL_ROWS, 0, -1):
            # Отрисовка баров (они масштабируются под общую высоту)
            line_str = ""
            for b in range(3):
                val_level = int((BAR_VALS[b] / 100) * (TOTAL_ROWS - 2))
                line_str += "  ███████  " if (h - 1) <= val_level else "  ░░░░░░░  "

            graph_row = ""
            # Отрисовка самого графика внутри его диапазона высоты
            if h <= GRAPH_HEIGHT:
                r_idx = h - 1
                for w in range(GRAPH_WIDTH):
                    if w < current_draw_col:
                        graph_row += graph_matrix[r_idx][w] + " "
                    else:
                        graph_row += "  "

            # Текстовые плашки сбоку
            if h == TOTAL_ROWS: graph_row = "   [ CRYPTO MARKET BIG LIVE CHART (Resets every 30s) ]"
            if h == TOTAL_ROWS - 1: graph_row = f"   📉 Next chart re-draw in: {int(30 - elapsed_graph)}s"
            if h == 1: graph_row = f"   SYS_UPTIME: {int(current_time - start_time)}s // STATUS: LIVE // GRID: {GRAPH_WIDTH}x{GRAPH_HEIGHT}"

            out += f"{get_gradient_color(0.1 + h*0.05, line_str):<40} {get_gradient_color(0.6, graph_row)}\n"

        out += f"   {BAR_VALS[0]:>3}%      {BAR_VALS[1]:>3}%      {BAR_VALS[2]:>3}%    \n"
        out += "  (BAR 1)    (BAR 2)    (BAR 3)   \n\n"
        out += get_gradient_color(0.8, "--- GASTER STREAM LINE ------------------------------------------------------------------\n")
        out += get_gradient_color(0.95, f" {gaster_line}\n")
        out += get_gradient_color(0.8, "-----------------------------------------------------------------------------------------\n")

        hex_err = f"{random.randint(0, 0xFFFFFFFF):08X}"
        out += get_gradient_color(0.4, f" >> NET_STREAM_LOG: [0x{hex_err}] TRANSACTION VALIDATED .. PACKETS FORWARDED ..\n")

        sys.stdout.write(out)
        sys.stdout.flush()
        time.sleep(0.08)

except KeyboardInterrupt:
    sys.stdout.write("\033[?25h\n")
    sys.stdout.flush()
EOF
python3 dashboard_max.py
