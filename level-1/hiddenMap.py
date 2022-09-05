def decoder(n, arr):
    for i, v in enumerate(arr):
        temp = bin(v)[2:]
        while len(temp) < n:
            temp = "0" + temp
        arr[i] = ""
        for c in temp:
            if c == "0":
                arr[i] += " "
            else:
                arr[i] += "#"
    return arr

def solution(n, arr1, arr2):
    arr1 = decoder(n, arr1)
    arr2 = decoder(n, arr2)
    answer = []
    for i, v in enumerate(arr1):
        temp = ""
        for vi, vv in enumerate(v):
            if arr2[i][vi] == "#" or arr1[i][vi] == "#":
                temp += "#"
            else:
                temp += " "
        answer.append(temp)

    return answer


solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
