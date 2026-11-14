import sys, unittest, tempfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'shop'))
from flask_online_store import create_app
from flask_online_store.models import db, Admin

class ShopTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.app=create_app({'TESTING':True,'SQLALCHEMY_DATABASE_URI':'sqlite://','WTF_CSRF_ENABLED':False,'UPLOADS_DEFAULT_DEST':self.temp.name})
        with self.app.app_context(): db.create_all()
        self.client=self.app.test_client()
    def tearDown(self):
        with self.app.app_context(): db.session.remove();db.drop_all()
        self.temp.cleanup()
    def test_register_login_profile_logout(self):
        data={'username':'demo_user','password':'example-only-password','email':'demo@example.com','phone':'0000000000'}
        response=self.client.post('/api/users',json=data)
        self.assertEqual(response.status_code,200,response.data)
        self.assertEqual(self.client.get('/api/users/1').status_code,200)
        self.assertEqual(self.client.get('/api/users/2').status_code,403)
        self.assertEqual(self.client.get('/api/logout').status_code,200)
        response=self.client.post('/api/login',json={'username':data['username'],'password':data['password']})
        self.assertEqual(response.status_code,200,response.data)
    def test_admin_and_category(self):
        with self.app.app_context(): Admin().save({'username':'demo_admin','password':'example-only-password','email':'admin@example.com'})
        self.assertEqual(self.client.get('/admin/').status_code,302)
        response=self.client.post('/admin/login',data={'username':'demo_admin','password':'example-only-password'},follow_redirects=True)
        self.assertEqual(response.status_code,200,response.data)
        response=self.client.post('/admin/categories/new',data={'name':'Example category','description':'Example description'},follow_redirects=True)
        self.assertEqual(response.status_code,200,response.data)
        self.assertIn(b'Example category',self.client.get('/admin/categories/').data)
        response=self.client.post('/admin/products/new',data={'name':'Example product','price':'12.50','number':'3','detail':'Example detail','tips':'Example','category_id':'1'},follow_redirects=True)
        self.assertEqual(response.status_code,200,response.data)
        self.assertIn(b'Example product',response.data)
        self.assertEqual(self.client.get('/api/products').json[0]['price'],12.5)
    def test_product_list(self):
        response=self.client.get('/api/products')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json,[])
    def test_user_cannot_access_admin(self):
        self.client.post('/api/users',json={'username':'demo','password':'example-only-password','email':'demo@example.com','phone':'0000000000'})
        self.assertEqual(self.client.get('/admin/categories/').status_code,302)

if __name__=='__main__':unittest.main()
