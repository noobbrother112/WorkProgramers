def solution(survey, choices):
    score = [0, 0, 0, 0]
    for i, s in enumerate(survey):
        if s == "RT":
            score[0] += ((choices[i] - 4) *-1)
        elif s == "TR":
            score[0] += (choices[i] - 4)
        elif s == "CF":
            score[1] += ((choices[i] - 4)*-1)
        elif s == "FC":
            score[1] += (choices[i] - 4)
        elif s == "JM":
            score[2] += ((choices[i] - 4)*-1)
        elif s == "MJ":
            score[2] += (choices[i] - 4)
        elif s == "AN":
            score[3] += ((choices[i] - 4)*-1)
        elif s == "NA":
            score[3] += (choices[i] - 4)
        print(score)
    answer = ("R" if score[0] >=0 else "T")+("C" if score[1] >=0 else "F")+("J" if score[2] >=0 else "M")+("A" if score[3] >=0 else "N")

    return answer


solution(["TR", "RT", "TR"], [7, 1, 3])
