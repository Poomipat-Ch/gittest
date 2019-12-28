import bisect 

def determine_grade(scores, breakpoints=[50, 60, 70, 80, 90], grades='FEDCBA'):
    i = bisect.bisect(breakpoints, scores)
    return grades[i]


print(determine_grade(90))
