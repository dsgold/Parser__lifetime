import json
import requests


def getData():
    responce = requests.get(url='https://www.lifetime.plus/api/analysis2')
    categories = responce.json().get('categories')
    full_info = []
    for c in categories:
        c_name = c.get('name').strip()
        c_items = c.get('items')
        category_items = []
        for item in c_items:
            item_info = {
                "item_name": item.get('name'),
                "item_type": item.get('type'),
                "item_days": item.get('days'),
                "item_price": item.get('price'),
                "item_old_price": item.get('oldPrice'),
                "item_cur_price": item.get('price'),
                "item_guide": item.get('preparationGuide'),
                "item_biomaterial": item.get('biomaterial'),
                "item_description": item.get('description'),
                "item_synonyms": item.get('synonyms')
            }
            category_items.append(item_info)
        categories = {
            "name": c_name,
            "items": category_items
        }
        full_info.append(categories)
    with open('./' + 'lifetime price-list.json', 'w') as outfile:
        json.dump(full_info, outfile, ensure_ascii=False)


def main():
    getData()


if __name__ == '__main__':
    main()
