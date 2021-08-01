def recommend_beer(body, fruit=0, bitter=0, hoppy=0, sweet=0, high_alcohol=0, malty=0):
    result = ''
    if body == 1:
        if fruit == 1:
            result = ['바이젠', '화이트 비어']
        else:
            result = ['라거', '필스너']
    elif body == 2:
        if bitter == 1:
            if hoppy == 1:
                result = 'IPA'
            else:
                result = '브라운 에일'
        else:
            if sweet == 1:
                result = '골든 에일'
            else:
                result = '브라운 에일'
    elif body == 3:
        if high_alcohol == 1:
            result = ['트라피스트', '쿼드러플']
        else:
            if malty == 1:
                result = ['스타우트', '포터']
            else:
                result = '페일 에일'
    return result