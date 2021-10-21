from beer_app import create_app
from beer_app.models.beer_model import Beer
import re
import os
app = create_app()
names = []
with app.app_context():
    for beer in Beer.query.all():
        names.append(beer.name)

# print(names)
beer_eng_names = []
err_cnt = 0
for name in names:
    p = re.compile('[A-Z][a-z]+')
    r = p.search(name)
    print(r)
    break
    try:
        beer_eng_names.append(name[r.start():])
    except:
        print(f'{name} is not collected')
        err_cnt += 1
print(f'({err_cnt}) beers were not collected')
    

# with open('beernames.txt', 'w') as f:
#     f.write('\n'.join(names))

with open('beer_eng_names.txt', 'w') as f:
    f.write('\n'.join(beer_eng_names))
        