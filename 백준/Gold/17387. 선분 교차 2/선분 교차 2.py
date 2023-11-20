import sys

input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

points = []
points.append([x1, y1])
points.append([x2, y2])
points.append([x3, y3])
points.append([x4, y4])


def ccw(p1, p2, p3):
    cross_p = (p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]) - (
        p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1]
    )
    if cross_p > 0:
        return 1
    elif cross_p == 0:
        return 0
    else:
        return -1


def cross(p1, p2, p3, p4):
    flag = False
    abc = ccw(p1, p2, p3)
    abd = ccw(p1, p2, p4)
    cda = ccw(p3, p4, p1)
    cdb = ccw(p3, p4, p2)

    if abc * abd == 0 and cda * cdb == 0:
        flag = True
        if (
            min(p1[0], p2[0]) <= max(p3[0], p4[0])
            and min(p3[0], p4[0]) <= max(p1[0], p2[0])
            and min(p1[1], p2[1]) <= max(p3[1], p4[1])
            and min(p3[1], p4[1]) <= max(p1[1], p2[1])
        ):
            return 1

    if abc * abd <= 0 and cda * cdb <= 0 and not flag:
        return 1

    return 0


print(cross(points[0], points[1], points[2], points[3]))
