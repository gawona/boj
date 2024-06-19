def solution(brown, yellow):
    answer = []
    temp = (brown - 4) // 2
    
    for a in range(1, temp + 1):
        b = temp - a
        
        if a * b == yellow:
            # 2씩 더하기, b > a
            answer.append(b + 2)
            answer.append(a + 2)
            break
            
    return answer