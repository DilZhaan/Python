if __name__ == '__main__':
    records = []
    scores = []
    scnd_Name = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        scores.append(score)
    min_value = min(scores)
    scores.remove(min_value)
    scndMValue = min(scores)
    for i in range (len(records)):
        if records[i][1] == scndMValue :
            scnd_Name.append(records[i][0])
            
    scnd_Name = sorted(scnd_Name)
    for i in range(len(scnd_Name)):
        print(scnd_Name[i])
        