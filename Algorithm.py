def q1000():
    A, B = input().split()
    print(int(A) + int(B))


def q1001():
    A, B = input().split()
    print(int(A) - int(B))


def q10998():
    A, B = input().split()
    print(int(A) * int(B))


def q1002():
    import math

    T = int(input())

    for t in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())

        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # 규현과 승환 사이의 거리

        if distance == 0 and r1 == r2:  # 두 원의 중심이 같고 r1과 r2가 같을 때
            print(-1)
        elif distance == (r1 + r2) or distance == abs(r1 - r2):  # 외접원 or 내접원 일 때
            print(1)
        elif abs(r1 - r2) < distance < (r1 + r2):  # 원 두개가 만나서 점 2개일 때
            print(2)
        else:
            print(0)


def q10869():
    # 문제 : 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
    # 입력 : 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
    # 출력 : 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

    A, B = input().split()

    A = int(A)
    B = int(B)

    print(A + B, A - B, A * B, A // B, A % B, sep='\n')

def q10718():
    for i in range(2):
        print('강한친구 대한육군')


def q1008():
    A, B = input().split()
    A, B = int(A), int(B)

    print(A / B)


def q9468():
    score = int(input('score :'))

    if 90 <= score <= 100:
        print('A')
    elif 80 <= score <= 89:
        print('B')
    elif 70 <= score <= 79:
        print('C')
    elif 60 <= score <= 69:
        print('D')
    else:
        print('F')


def q18108():
    print(int(input()) - 543)


def q10430():
    A, B, C = input().split()
    A, B, C = int(A), int(B), int(C)

    print((A + B) % C, ((A % C) + (B % C)) % C, (A * B) % C, ((A % C) * (B % C)) % C, sep='\n')


def q2588():
    A, B = input().split()

    A = int(A)
    B = int(B)

    print(A * (B % 10))
    print(A * (B % 100 // 10))
    print(A * (B // 100))
    print(A * B)

def q11382():
    A, B, C = map(int, input().split())

    print(A + B + C)


def q10171():
    print("\    /\\")
    print(" )  ( ')")
    print("(  /  )")
    print(" \(__)|")


def q10172():
    print("|\_/|")
    print("|q p|   /}")
    print("( 0 )\"\"\"\\")
    print("|\"^\"`    |")
    print("||_/=\\\\__|")


def q1330():
    A, B = map(int, input().split())

    if A > B:
        print(">")
    elif A < B:
        print("<")
    else:
        print("==")


def q2753():
    year = int(input())

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("1")
    else:
        print("0")


def q14681():
    x = int(input())

    y = int(input())

    if x > 0:
        if y > 0:
            print("1")
        else:
            print("4")
    else:
        if y > 0:
            print("2")
        else:
            print("3")

def q2884():
    H, M = map(int, input().split())

    if H > 0:
        if 0 <= M < 45:
            H -= 1
            M += 15

        else:
            M -= 45

    elif H == 0:
        if 0 <= M < 45:
            H += 23
            M += 15
        else:
            M -= 45

    print(f"{H} {M}")


def q2525():
    A, B = map(int, input().split())
    C = int(input())

    if (A + ((B + C) // 60)) >= 24:
        A = (A + ((B + C) // 60)) - 24

    else:
        A += (B + C) // 60

    B = (B + C) % 60

    print(f"{A} {B}")


def q2480():
    A, B, C = map(int, input().split())

    if A == B == C:
        print(10000 + A * 1000)
    elif A == B != C:
        print(1000 + A * 100)
    elif B == C != A:
        print(1000 + B * 100)
    elif C == A != B:
        print(1000 + C * 100)
    else:
        print(max(A, B, C) * 100)