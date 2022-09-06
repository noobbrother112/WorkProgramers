def solution(s):
    counter = {}
    strList = {}
    maxlength = len(s)
    if maxlength == 1:
        return maxlength
    # 1부터 총 길이의 반 까지 나누기 테스트
    for i in range(1, int((maxlength / 2)) + 1):
        slicedStr = []
        counter[i] = {}
        # 문자열 총 길이를 나눔 만큼
        for ii in range(1, int(maxlength / i) + 1):
            slicedStr.append(s[len(slicedStr) * i:(len(slicedStr) + 1) * i])
            if ii == int(maxlength / i):
                if s[(len(slicedStr)) * i:] != "":
                    slicedStr.append(s[(len(slicedStr)) * i:])

        for ii2 in range(len(slicedStr)):
            if len(counter[i]) == 0:
                counter[i][0] = [slicedStr[ii2], 1]
            elif counter[i][len(counter[i]) - 1][0] == slicedStr[ii2]:
                counter[i][len(counter[i]) - 1][1] += 1
            else:
                counter[i][len(counter[i])] = [slicedStr[ii2], 1]

        temp = ""

        for ii3 in range(len(counter[i])):
            if counter[i][ii3][1] > 1:
                temp += str(counter[i][ii3][1])
            temp += counter[i][ii3][0]

        strList[temp] = len(temp)
    result = sorted(strList.items(), key=lambda e: e[1], reverse=False)
    answer = result[0][1]
    return answer

print(solution("a"))