def solution(N, stages):
    rate = {}
    stageCount = len(stages)

    for i in range(1, N+1):
        if stageCount != 0:
            count = stages.count(i)
            rate[i] = count / stageCount
            stageCount -= count
        else:
            rate[i] = 0

    answer = []
    for k, v in sorted(rate.items(), key=lambda e: e[1], reverse=True):
        answer.append(k)

    return answer


print(solution(4, [4,4,4,4,4]))
