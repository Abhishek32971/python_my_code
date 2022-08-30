def inp_points():
    while True:
        try:
            n = int(input().strip())
            assert n > 0
            break
        except:
            print("Enter a valid positve integer")
            continue

    return [int(input()) for _ in range(n)]


def find_ways(pts: int) -> int:
    if pts == 0 or pts == 1:
        return 1
    elif pts == 2:
        return 2
    return find_ways(pts - 1) + find_ways(pts - 2) + find_ways(pts - 3)


def output(res: list[tuple[int, int]]):
    for i, j in res:
        print(f"{i} points: {j} ways")


def main():
    pts = inp_points()
    res = []
    for i in pts:
        res.append((i, find_ways(i)))

    output(res)


if __name__ == "__main__":
    main()