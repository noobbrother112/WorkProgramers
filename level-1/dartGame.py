def solution(dartResult):
    answer = 0
    temp = {}
    for i, v in enumerate(dartResult):
        if v == "S" or v == "D" or v == "T":
            if v == "S":
                temp[len(temp)] = {
                    "slice": i,
                    "bonus": 1,
                    "rewerd": 1
                }
            elif v == "D":
                temp[len(temp)] = {
                    "slice": i,
                    "bonus": 2,
                    "rewerd": 1
                }
            elif v == "T":
                temp[len(temp)] = {
                    "slice": i,
                    "bonus": 3,
                    "rewerd": 1
                }

            if i < len(dartResult) - 1:
                if dartResult[i + 1] == "*":
                    temp[len(temp)-1]["rewerd"] *= 2
                    if len(temp) >= 2:
                        temp[len(temp)-2]["rewerd"] *= 2
                elif dartResult[i + 1] == "#":
                    temp[len(temp)-1]["rewerd"] = -1

    for i in temp:
        tempJson = temp[i]
        if i == 0:
            tempNum = int(dartResult[:temp[0]["slice"]])
            value = int(dartResult[:temp[0]["slice"]])
            for i in range(1, temp[0]["bonus"]):
                tempNum *= value
            answer += (tempNum * temp[0]["rewerd"])
        else:
            if dartResult[temp[i - 1]["slice"] + 1] == "*" or dartResult[temp[i - 1 ]["slice"] + 1] == "#":
                temp[i - 1]["slice"] += 1
            tempNum = int(dartResult[temp[i-1]["slice"] + 1:tempJson["slice"]])
            value = int(dartResult[temp[i-1]["slice"] + 1:tempJson["slice"]])
            for i in range(1, tempJson["bonus"]):
                tempNum *= value
            answer += (tempNum * (tempJson["rewerd"]))

    return answer


print(solution("1S*2T*3S"))
