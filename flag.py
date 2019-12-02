import sys

def flag(N):
    try:
        N = int(N)
        if N < 0 or N % 2 != 0:
            raise ValueError
        string = ""
        height = 2 * N + 2
        width = 3 * N + 2

        x = [int(0.5 * N + 1), int(0.5 * N + 1), N, N, N + 1, N + 1, int(1.5 * N), int(1.5 * N)]
        y = [int(1.5 * N), int(1.5 * N + 1), N + 1, 2 * N, N + 1, 2 * N, int(1.5 * N), int(1.5 * N + 1)]

        for i in range(height):
            for j in range(width):
                if i == 0 or i == height - 1:
                    string += "#"
                elif j == 0 or j == width - 1:
                    string += "#"
                elif i >= x[4] and i <= x[6] and i == j:
                    string += "*"
                elif i >= x[1] and i <= x[3] and i + N == j:
                    string += "*"
                elif i >= x[0] and i <= x[2] and i == height - j - 1:
                    string += "*"
                elif i >= x[5] and i <= x[7] and i == height - j - 1 + N:
                    string += "*"
                elif j > y[2] and j < y[3] and i > x[0] and i < x[6] and i < j and i + N > j and i > height - j - 1 and i < height - j - 1 + N:
                    string += "o"
                else:
                    string += " "
            string += "\n"
        return string
    except ValueError as ArgumentError:
        print("ArgumentError")
    except Exception:
        print("Error")



if __name__==  "__main__":
    N = input("N = ")
    flag(N)

