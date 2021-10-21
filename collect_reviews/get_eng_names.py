import re
import os

file_path = os.path.abspath('collect_reviews/beernames.txt')
with open(file_path, 'r') as f:
    names = f.read().split('\n')

beer_eng_names = []
err_cnt = 0
for name in names:
    p = re.compile('[A-Z][a-z]+')
    r = p.search(name)
    try:
        beer_eng_names.append(name[r.start():])
    except:
        print(f'{name} is not collected')
        err_cnt += 1
print(f'({err_cnt}) beers were not collected')
    

save_path = os.path.abspath('collect_reviews/beer_eng_names.txt')
with open(save_path, 'w') as f:
    f.write('\n'.join(beer_eng_names))

# max는 Max hite로 변경하여 검색
