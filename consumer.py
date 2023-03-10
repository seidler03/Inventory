from main import r, Products
import time

key = 'order_completed'
group = 'inventory-group'

try:
    r.xgroup_create(key, group)
except:
    print('Group alredy exists')

while True:
    try:
        results = r.xreadgroup(group, key, {key: '>'}, None)
        if results != []:
            for result in results:
                print(result)
                order_info = result[1][0][1]
                product = Products.get(order_info['product_id'])
                product.quantity = product.quantity - int(order_info['quantity'])

                product.save()

    except Exception as e:
        print(str(e))
    time.sleep(1)
