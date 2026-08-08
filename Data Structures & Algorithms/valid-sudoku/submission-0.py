class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen_hor = set()
            seen_ver = set()

            for j in range(9):
                num_hor = board[i][j]
                num_ver = board[j][i]

                if num_hor != ".":
                    if num_hor in seen_hor:
                        return False
                    seen_hor.add(num_hor)

                if num_ver != ".":
                    if num_ver in seen_ver:
                        return False
                    seen_ver.add(num_ver)

        for st_row in range(0, 9, 3):
            for st_column in range(0, 9, 3):
                seen = set()

                for r in range(st_row, st_row + 3):
                    for c in range(st_column, st_column + 3):
                        num = board[r][c]

                        if num != ".":
                            if num in seen:
                                return False
                            seen.add(num)

        return True