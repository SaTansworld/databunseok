import math

h = int(input('정수 10에서 20사이의 수 를 입력하시오 : '))


while True:
    if 10 <= h and h <= 20:
        print(f'입력된 값:{h}')
        for r in range(5, 16):
            v = (1/3) *  3.14 *r * r * h
            print(f'결과 값:{v}')
            
    else:
        print('숫자를 다시 입력해주세요')
    break
