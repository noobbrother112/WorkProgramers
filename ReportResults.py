def solution(id_list, report, k):
    #신고 중복제거 후 나눠서 넣기
    filteredReport2 = []
    reportedId = []
    for value in list(set(report)):
        filteredReport2.append(value.split(" "))
        reportedId.append(value.split(" ")[1])

    #아이디 정리
    idJson = {}
    for id in id_list:
        #앞이 신고받은 횟수 뒤가 메일받은 횟수
        idJson[id] = 0

    #신고받은 횟수 k회이상 목록화
    guilty = []
    for id in idJson:
        if reportedId.count(id) >= k:
            guilty.append(id)

    # 횟수가 넘은 유저를 신고한 사람찾아 숫자넣기
    for repo in filteredReport2:
        if repo[1] in guilty:
            idJson[repo[0]] = idJson[repo[0]] +1

    answer = []
    for id in id_list:
        answer.append(idJson[id])
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
