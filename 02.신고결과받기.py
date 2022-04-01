def solution(id_list, report, k):
    
    # dictionary로 관리
    user_dic = {user_name : [] for user_name in id_list}
    
    for report_id in set(report) :
        report_list = report_id.split()
        user_dic[report_list[0]].append(report_list[1]) 
        
    # 신고당한 횟수 계산
    reported_count = {}
    for user_id in user_dic:
        for reported_name in user_dic[user_id]:
            if reported_name in reported_count:
                reported_count[reported_name] += 1
            else :
                reported_count[reported_name] = 1
    
    # 정지 대상자 확정
    stopper = []
    for reported_name in reported_count :
        if reported_count[reported_name] >= k:
            stopper.append(reported_name)
    
    # 정지 문자 발송
    maile_list = {user_id : 0 for user_id in user_dic}
    
    for user_id in user_dic:
        for stop_id in stopper:
            if stop_id in user_dic[user_id]:
                maile_list[user_id] += 1
                
    result = [maile_list[maile] for maile in maile_list]

    return result
