import os
from PIL import Image
import time
if os.name == 'nt':
    import ctypes
    kernel32 = ctypes.windll.kernel32
    # 7 = ENABLE_PROCESSED_OUTPUT | ENABLE_WRAP_AT_EOL_OUTPUT | ENABLE_VIRTUAL_TERMINAL_PROCESSING
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

def ascii_frame(img):
    img = img.resize((100, 50))
    sym = ' .\'``^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvcz░XYUJCLQ0OZ▒mwqpdbkhao*#MW&8%B@$▓██'
    len_ = len(sym) - 1
    x, y = img.size
    for y_ in range(y):
        for x_ in range(x):
            pixel = img.getpixel((x_, y_))

            str_ = sym[int((pixel/255)*len_)]
            print(str_, end='')
        print()

names_list = os.listdir('output_frames')
FRAME_DURATION = 1.0 / 60.0

for name_ in names_list:
    print("\033[H", end="")
    start_time = time.time()  # Фиксируем время начала обработки кадра

    # Очистка экрана и вывод кадра
  #  os.system('cls' if os.name == 'nt' else 'clear')
    img = Image.open('output_frames/' + name_).convert('L')
    ascii_frame(img)

    # Вычисляем, сколько времени заняла отрисовка
    elapsed_time = time.time() - start_time

    # Спим только оставшуюся часть времени от 1/30 секунды
    sleep_time = FRAME_DURATION - elapsed_time
    if sleep_time > 0:
        time.sleep(sleep_time)
    else:
        continue

start_time = time.time()
print("\033[H", end="")
ascii_frame(Image.open('output_frames/frame_6000.jpg').convert('L'))
print("\033[H", end="")
elapsed_time = time.time() - start_time

input()
