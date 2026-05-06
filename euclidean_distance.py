import math


def euclidean_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """计算二维平面上两点 (x1, y1) 与 (x2, y2) 的欧氏距离。"""
    return math.hypot(x2 - x1, y2 - y1)


def main() -> None:
    print("请输入第一个坐标 x1 y1：")
    x1, y1 = map(float, input().split())

    print("请输入第二个坐标 x2 y2：")
    x2, y2 = map(float, input().split())

    distance = euclidean_distance(x1, y1, x2, y2)
    print(f"两点之间的欧氏距离为: {distance:.6f}")


if __name__ == "__main__":
    main()
