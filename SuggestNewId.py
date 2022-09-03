import re

# -_.~!@#$%^&*()=+[{]}:?,<>/

def solution(new_id):
    answer = re.sub("([^a-z0-9-_\.])", "", new_id.lower())
    while len(answer) > 0 and re.search("\.\.", answer) != None:
        answer = re.sub("\.\.", ".", answer)
    while len(answer) > 0:
            if answer[len(answer)-1] == ".":
                answer = answer[:-1]
            elif answer[0] == ".":
                answer = answer[1:]
            else:
                break
    if len(answer) <= 0:
        answer = "a"
    if len(answer) >= 16:
        answer = answer[:15]
        print(answer)
        if answer[len(answer)-1] == ".":
            answer = answer[:-1]
    if len(answer) <= 3:
        while len(answer) < 3:
            answer = answer +answer[len(answer)-1]
    return answer


print(solution("-......._~!\@AAASSS#$%^&*()=+[{]}:?,<>/"))
