if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    #set sort 2nd max
    #print(records)
    grades = sorted(set([record[1] for record in records]))
    student_names = sorted([record[0] for record in records if record[1] == grades[1]])
    for names in student_names:
        print(names)
