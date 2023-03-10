import redis
from fastapi import FastAPI
from redis_om import HashModel

app = FastAPI()

r = redis.Redis(
    host='redis-18050.c232.us-east-1-2.ec2.cloud.redislabs.com',
    port=18050,
    password='pUbl4R754XDkohqVgwuiY8UWoINSYu9m'
)


class Products(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = r


@app.get('/products')
def all_products():
    return [format(pk) for pk in Products.all_pks()]


@app.get('/products/{pk}')
def get_by_id(pk: str):
    return Products.get(pk)


@app.post('/products')
def create_products(product: Products):
    return product.save()


@app.delete('/products/{pk}')
def get_by_id(pk: str):
    return Products.delete(pk)


def format_data(pk: str):
    product = Products.get(pk)
    return {
        'id': product.pk,
        'name': product.name,
        'price': product.price,
        'quantity': product.price
    }
