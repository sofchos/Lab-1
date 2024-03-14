import sys
ROW1_L = 8
ROW2_L = 10
ROW3_L = 12
STEP_BW_ROWS = 1
RED = 41
GREEN = 42

def line_in_circle(row, scaleup=True):
    sys.stdout.write('\u001b[1A') 
    if scaleup:
        sys.stdout.write(f'\u001b[{str(row - STEP_BW_ROWS)}D')
    else:
        sys.stdout.write(f'\u001b[{str(row + STEP_BW_ROWS)}D')
    sys.stdout.write(f"\u001b[{RED}m{' '*row}")

def flag(WIDTH, LENGTH):
    #сам флаг
    for i in range(WIDTH):
        print(f"\u001b[{GREEN}m{' '*LENGTH}\u001b[0m")
    #создание первого ряда в круге (нижний)
    sys.stdout.write(f'\u001b[{str(WIDTH//2 - 1)}A')
    sys.stdout.write(f'\u001b[{str(LENGTH//2 - (ROW1_L//2 + 4))}C')
    sys.stdout.write(f"\u001b[{RED}m{' '*ROW1_L}")
    #второй ряд в круге
    line_in_circle(ROW2_L)
    #третий ряд в круге
    line_in_circle(ROW3_L)
    #четвертый ряд в круге
    line_in_circle(ROW2_L, scaleup=False)
    #пятый ряд в круге
    line_in_circle(ROW1_L, scaleup=False)
    #возвращение к обычным настройкам терминала
    sys.stdout.write(f'\u001b[{str(WIDTH)}B')
    sys.stdout.write('\u001b[0m')

flag(9,30)
print()

def function_graph(WIDTH, LENGTH):
    plain = [[' ' for i in range(WIDTH)] for i in range(LENGTH)] #создает массив - пустое поле графика
    for i in range(WIDTH):
        for j in range(LENGTH):
            if j == 0:
                plain[i][j] = f'{str(i)}  ' #вертикальная линия цифр
            if i == 0:
                plain[i][j] = f'{str(j)}  ' #горизонтальная линия цифр
            if i == (2 * j)+3:
                plain[i][j] = '//'

    for i in range(WIDTH):
        print(' '.join(plain[WIDTH - 1 - i])) #вывод содержимого массива (в обратном порядке)
        print(' ')

function_graph(10,10)

def count_percent(x):
    return round((x/100)*10,3)

def create_diagram(percent1, percent2, color1, color2):
    x = f"\u001b[{color1}m \u001b[0m"
    y = f"\u001b[{color2}m \u001b[0m"
    print('↑ percent, %')
    for i in range(100, 0, -1):
        if percent1 >= i and percent2 >= i:
            print('|' + x + y)
        elif percent1 >= i:
            print('|' + x)
        elif percent2 >= i:
            print('|' + ' ' + y)
        else:
            print('|')
    print('|' + '-' * 3 + '→')
    print('0')

print('Диаграмма процентного соотношения чисел:')
with open('sequence.txt') as f:
    sum1 = 0
    sum2 = 0
    cnt = 0
    for line in f:
        s = float(line)
        cnt += 1
        if 1 <= cnt <= 125:
            if s >=0:
                sum1 += s
            else:
                sum1 = sum1 - s
        else:
            if s >=0:
                sum2 += s
            else:
                sum2 = sum1 - s
                
percent1 = count_percent(sum1)
percent2 = count_percent(sum2)
create_diagram(percent1, percent2, GREEN, RED)
print (percent1)
print (percent2)

def pattern(WIDTH, LENGTH):
    for i in range(WIDTH):
        print('\u001b[40;1m ' * LENGTH, '\u001b[0m')#задает поле для рисунка
    
    for j in range (2):
        sys.stdout.write(f'\u001b[{str(WIDTH+j)}A')
        for i in range (5):
            sys.stdout.write(f'\u001b[{str(j)}B')
            sys.stdout.write(f"\u001b[{RED}m{' '*1}")
            sys.stdout.write(f'\u001b[{str(j)}D')

        sys.stdout.write(f'\u001b[{str(LENGTH+j)}A')
        sys.stdout.write(f"\u001b[{RED}m{' '*1}")

        for i in range (4):
            sys.stdout.write(f'\u001b[{str(j)}D')
            sys.stdout.write(f"\u001b[{RED}m{' '*2}")
            sys.stdout.write(f'\u001b[{str(j)}C')
        
        for i in range(2):
            sys.stdout.write(f'\u001b[{str(j)}B') 
        for i in range (3):
            sys.stdout.write(f'\u001b[{str(j)}D')
            sys.stdout.write(f"\u001b[{RED}m{' '*1}")
            sys.stdout.write(f'\u001b[{str(j)}A')
        
        for i in range(3):
            sys.stdout.write(f'\u001b[{str(j)}B')  
        for i in range (3):
            for i in range(3):
             sys.stdout.write(f'\u001b[{str(j)}D') 
            sys.stdout.write(f"\u001b[{RED}m{' '*1}")
            for i in range(3):
             sys.stdout.write(f'\u001b[{str(j)}C')   

        for i in range(2):
            sys.stdout.write(f'\u001b[{str(j)}B')  
        for i in range(5):
            sys.stdout.write(f'\u001b[{str(j)}D') 
        for i in range (2):
            sys.stdout.write(f'\u001b[{str(j)}D')
            sys.stdout.write(f"\u001b[{RED}m{' '*1}")
            sys.stdout.write(f'\u001b[{str(j)}A')   

        for i in range(2):
             sys.stdout.write(f'\u001b[{str(j)}B')
        sys.stdout.write(f'\u001b[{str(j)}D') 
        for i in range (7):
            sys.stdout.write(f'\u001b[{str(j)}C')
            sys.stdout.write(f"\u001b[{RED}m{' '*1}")
            sys.stdout.write(f'\u001b[{str(j)}D') 
        
    sys.stdout.write(f'\u001b[{str(WIDTH)}B')
    sys.stdout.write('\u001b[0m')


for i in range(4):
    pattern(11,24)

