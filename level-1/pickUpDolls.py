def solution(board, moves):
    answer = 0
    dollList = []
    for move in moves:
        move -= 1
        for line in board:
            if line[move] != 0:
                if len(dollList) > 0:
                    if dollList[len(dollList)-1] == line[move]:
                        answer+=2
                        dollList = dollList[:len(dollList)-1]
                        line[move] = 0
                    else:
                        dollList.append(line[move])
                        line[move] = 0
                    break
                else:
                    dollList.append(line[move])
                    line[move] = 0
                    break
    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
         [1, 5, 3, 5, 1, 2, 1, 4]))
