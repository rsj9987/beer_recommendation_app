import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import os

def beer_review_crawling(beer_name_list, save_path):
    '''
    Crawling from 'https://www.beeradvocate.com'
    Parameter : beer_name_list : list of beer names, save_path : save path to collected review
    '''
    
    err_cnt = 0
    err_bnames = []
    scores_list = []
    url = 'https://www.beeradvocate.com'
    for bname in beer_name_list:
        search_name = bname.replace(' ', '+')
        res = requests.get(url + f'/search/?q={search_name}')
        html = res.content
        bs = BeautifulSoup(html, 'html.parser')
        try:
            beer_url = bs.select_one('div#ba-content > div > div > a')['href']
            beer_res = requests.get(url + beer_url)
            beer_bs = BeautifulSoup(beer_res.content, 'html.parser')
            reviews = beer_bs.find_all('div', {'id' : 'rating_fullview_content_2'})
        except:
            reviews = bs.find_all('div', {'id' : 'rating_fullview_content_2'})
        
        if reviews:
            review_cnt = 0
            for review in reviews:
                try:
                    rev = review.text
                    s = re.search('%', rev).end()
                    e = re.search('overall:', rev).start() - 2
                    scores = rev[s:e]
                    scores = scores.split('|')
                    beer_reviews = {'name' : bname}

                    for sc in scores:
                        sc = sc.strip()
                        sc = sc.split(':')
                        sense = sc[0].strip() 
                        score = float(sc[1].strip())
                        
                        beer_reviews[sense] = score
                    # collect review
                    r_s = re.search('overall: [0-9][.]?[0-9]?[0-9]?', rev).end()
                    beer_reviews['review'] = rev[r_s:]

                    scores_list.append(beer_reviews)
                    review_cnt += 1
                except:
                    pass
            print(f"{review_cnt} of {bname} review are collected.") 
        else:
            err_cnt += 1
            err_bnames.append(bname)
            print(f"{bname} is not collected")
    print(err_bnames, 'are not collected')
    print(f'not collected total : {err_cnt}')
    with open(save_path + '/err_collected_beers.txt', 'w') as f:
        f.write('\n'.join(err_bnames))
    df = pd.DataFrame(scores_list)
    df.to_csv(save_path + '/beer_scores.csv', index=False)





if __name__ == '__main__':

    # beer_recommandation_app 경로에서 실행
    file_path = os.path.abspath('collect_reviews/beer_eng_names.txt')

    with open(file_path, 'r') as f:
        beer_names = f.read().split('\n')
    save_path = os.path.abspath('collect_reviews/')
    beer_review_crawling(beer_names, save_path)

