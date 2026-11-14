from flask_restful import Resource
from ...models import Product
class ProductView(Resource):
    def get(self,id=None):
        if id is not None:
            p=Product.query.get_or_404(id)
            return {'id':p.id,'name':p.name,'price':float(p.price)}
        return [{'id':p.id,'name':p.name,'price':float(p.price)} for p in Product.query.all()]
    def post(self,id=None):return {'error':'Use the admin interface'},405
    def put(self,id=None):return {'error':'Use the admin interface'},405
    def delete(self,id=None):return {'error':'Use the admin interface'},405
