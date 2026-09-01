if __name__ == '__main__':
    n = int(input())
    sums=0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks[query_name]:
        sums=i+sums
    print(f"{sums / len(student_marks[query_name]):.2f}")



