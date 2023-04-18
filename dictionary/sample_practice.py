if __name__=='__main__':
    n = int(input())
    students_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        students_marks[name]=scores
    query_name = input()
marks = students_marks.get(query_name)
av= sum(marks)/len(marks)
print("{0:.2f}".format(av))   #cant use round() method