def solution(fees, records):
    data = {}
    for r in records:
        rData = r.split(" ")
        if rData[2] == "IN":
            try:
                buf = data[rData[1]]
            except KeyError:
                data[rData[1]] = []
            data[rData[1]].append(
                {
                    "IN": rData[0],
                    "OUT": "23:59"
                }
            )
        else:
            data[rData[1]][len(data[rData[1]])-1]["OUT"] = rData[0]
    data2 = {}
    for car in data:
        try:
            buf = data2[car]
        except KeyError:
            data2[car] = 0

        for t in data[car]:
            t["IN"] = t["IN"].split(":")
            t["OUT"] = t["OUT"].split(":")
            data2[car] += (int(t["OUT"][0])*60+int(t["OUT"][1]))-(int(t["IN"][0])*60+int(t["IN"][1]))
    for car in data2:
        if data2[car] <= fees[0]:
            data2[car] = fees[1]
        else:
            a = (data2[car]-fees[0])%fees[2]
            if a != 0:
                a = 1
            data2[car] = fees[1]+int((data2[car]-fees[0])/fees[2]+a)*fees[3]

    answer = []
    for k, v in sorted(data2.items(), key=lambda e: e[0], reverse=False):
        answer.append(data2[k])
    return answer


solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
