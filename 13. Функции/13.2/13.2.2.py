def draw_triangle(fill, base):
    for i in range(1, base+1):
        if i <= (base // 2 + 1):
            print(fill * i)
        elif i > (base // 2 + 1):
            print(fill * (base + 1 - i))


fill = input()
base = int(input())

draw_triangle(fill, base)
