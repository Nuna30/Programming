from desk_class import Desk

desk=[
    (11, '서울'),
    (23, '경기'),
    (37, '강원'),
    (41, '충청'),
    (56, '전라'),
    (62, '경상'),
    (73, '제주'),
    (88, '독도')
]

def crack(e, n, desk):
    # To-do
    desk=Desk(desk)
    check_list=[1,n//2,n] # 1,4,8
    k=1
    for _ in range(10): # 10번만 시도.
        check,location=desk.open(check_list[k]) # 여러번 여는 걸 방지하기 위해 한 번 열고 정보를 전부 저장
        
        if check==e :
            return location
        elif check>e : 
            check_list.append((check_list[k-1]+check_list[k])//2)
            check_list.sort()
        else :
            check_list.append((check_list[k]+check_list[k+1])//2)
            check_list.sort()
            k+=1

print(crack(41,8,desk))

