disDoc = {
    2:{
        1: 1,
        2: 0,
        3: 1,
        4: 2,
        5: 1,
        6: 2,
        7: 3,
        8: 2,
        9: 3,
        0: 3,
        "*": 4,
        "#": 4
    },
    5:{
        1: 2,
        2: 1,
        3: 2,
        4: 1,
        5: 0,
        6: 1,
        7: 2,
        8: 1,
        9: 2,
        0: 2,
        "*": 3,
        "#": 3
    },
    8:{
        1: 3,
        2: 2,
        3: 3,
        4: 2,
        5: 1,
        6: 2,
        7: 1,
        8: 0,
        9: 1,
        0: 1,
        "*": 2,
        "#": 2
    },
    0:{
        1: 4,
        2: 3,
        3: 4,
        4: 3,
        5: 2,
        6: 3,
        7: 2,
        8: 1,
        9: 2,
        0: 0,
        "*": 1,
        "#": 1
    },
    "left": [1, 4, 7],
    "right": [3, 6, 9]
}


def checkDis(nowNumber, targetNumber):
    distance = disDoc[targetNumber][nowNumber]
    return distance


def solution(numbers, hand):
    answer = ''
    leftPosition = "*"
    rightPosition = "#"
    mainHand = hand
    for number in numbers:
        if number in disDoc["left"]:
            answer += "L"
            leftPosition = number
        elif number in disDoc["right"]:
            answer += "R"
            rightPosition = number
        else:
            leftDis = disDoc[number][leftPosition]
            rightDis = disDoc[number][rightPosition]
            if leftDis < rightDis:
                answer += "L"
                leftPosition = number
            elif leftDis > rightDis:
                answer += "R"
                rightPosition = number
            elif mainHand == "left":
                answer += "L"
                leftPosition = number
            elif mainHand == "right":
                answer += "R"
                rightPosition = number
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
