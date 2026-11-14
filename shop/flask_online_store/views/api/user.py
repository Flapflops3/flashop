from flask import request
from flask_restful import Resource
from flask_login import current_user,login_user,login_required
from ...models import User
class UserView(Resource):
    def post(self,id=None):
        args=request.get_json(silent=True) or request.form
        if not all(args.get(k) for k in ['username','password','email','phone']):return {'error':'Missing required field'},400
        if User.query.filter_by(username=args['username']).first():return {'error':'Username exists'},409
        user=User();user.save(args);login_user(user)
        return {'id':user.id},200
    @login_required
    def get(self,id=None):
        if id!=current_user.id:return {'error':'Forbidden'},403
        return current_user.serialize(current_user.id)
    def put(self,id=None):return {'error':'Not implemented in this exercise'},501
    def delete(self,id=None):return {'error':'Not implemented in this exercise'},501
