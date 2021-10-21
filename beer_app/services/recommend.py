# use cosine simmilarity
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import re
beers = pd.read_pickle('recommendation/beers_data/Beers_TFIDF_ended.pkl')
matrix = beers.set_index('name').drop(['look', 'smell', 'taste', 'feel'], axis=1)
cosine_sim = cosine_similarity(matrix, matrix)
indices = pd.Series(data=beers.index, index=beers['name'])

def get_recommendation(beer_name):
    # 영어로된 이름만 가져오기
    s = re.search('[A-Za-z]', beer_name).start()
    name = beer_name[s:].strip()
    
    # 선택한 맥주와의 유사도 가져오기
    try:
        idx = indices[name]
    except:
        return '해당 맥주가 추천시스템에 존재하지 않습니다. 죄송합니다.'

    # 해당 맥주와의 유사도 구하기
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 유사도에 따라 맥주 정렬
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # 가장 유사한 맥주 3개 가져오기
    sim_scores = sim_scores[1:4]

    # 가장 유사한 맥주 3개의 인덱스 가져오기
    beer_indices = [i[0] for i in sim_scores]

    return indices.iloc[beer_indices].index.tolist()

if __name__ == '__main__':
    print(get_recommendation('Hoegaarden Original White Ale'))



    # def recommend_beer(body, fruit=0, bitter=0, hoppy=0, sweet=0, high_alcohol=0, malty=0):
#     result = ''
#     if body == 1:
#         if fruit == 1:
#             result = ['바이젠', '화이트 비어']
#         else:
#             result = ['라거', '필스너']
#     elif body == 2:
#         if bitter == 1:
#             if hoppy == 1:
#                 result = 'IPA'
#             else:
#                 result = '브라운 에일'
#         else:
#             if sweet == 1:
#                 result = '골든 에일'
#             else:
#                 result = '브라운 에일'
#     elif body == 3:
#         if high_alcohol == 1:
#             result = ['트라피스트', '쿼드러플']
#         else:
#             if malty == 1:
#                 result = ['스타우트', '포터']
#             else:
#                 result = '페일 에일'
#     return result