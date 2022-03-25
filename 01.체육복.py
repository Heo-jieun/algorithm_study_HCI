'''
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
'''

def solution(n, lost, reserve):
    
    # 1.체육복이 있는 사람과 없는 사람 구분
    
    ## 여벌있는데 도난 당한 사람 정리
    same = set(lost).intersection(set(reserve))
    for i in same:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)

    ## 체육복 없는 사람 : lost
    ## 여벌 있는 사람 : reserve
    
    # 학생별로 체육복이 몇개있는지 정리
    stu = [1 for i in range(n)]
    for i in lost:
        stu[i-1] = 0
    for i in reserve:
        stu[i-1] =2
    
    print(stu)
    # 2. 수업에 참여할 수 있는 최대 학생수 구하기
    for idx, value in enumerate(stu):
        if idx == 0 and value == 0 : 
            if stu[idx+1] == 2 :
                stu[idx] = 1
                stu[idx+1] = 1
                
        elif idx == len(stu) -1 and value == 0: 
            if stu[idx - 1] == 2:
                stu[idx] = 1
                stu[idx-1] = 1
        elif value == 0:
            if stu[idx-1] == 2:
                stu[idx] = 1
                stu[idx-1] = 1
            elif stu[idx+1] == 2 :
                stu[idx] = 1
                stu[idx+1] =1
    print(stu)
    num = 0
    for i in stu:
        if i != 0:
            num+=1
    print(stu) 
    return num
