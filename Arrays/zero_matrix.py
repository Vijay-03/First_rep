def set_zero(matrix, n):
    zero_rows = [False] * n
    zero_cols = [False] * n

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_rows[i] = True
                zero_cols[j] = True

    for i in range(n):
        if zero_rows[i] is True:
            for col in range(n):
                matrix[i][col] = 0

    for i in range(n):
        if zero_cols[i] is True:
            for row in range(n):
                matrix[row][i] = 0

    return matrix


if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        # arr.append(list(map(int, input().split()))
        row = list(map(int, input().split()))
        arr.append(row)

    ans = set_zero(arr, n)

    for i in range(n):
        for j in range(n):
            print(ans[i][j], end=' ')
        print()

# inputs
# 4
# 2 3 9 0
# 4 3 8 9
# 4 6 0 6
# 3 4 6 7
