# art.py

import sys
import random

chars = '\|/'

def draw(rows, columns):
    # rows는 정수이기 때문에 순회할 수 없다. 대신 range(rows)를 사용해 행의 수만큼 반복해야 한다.
    for r in range(rows):
        print(''.join(random.choice(chars) for _ in range(columns)))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit("usage: art.py rows columns")
    draw(int(sys.argv[1]), int(sys.argv[2]))
