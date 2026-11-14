"""Local database commands. No account has a default password."""
import argparse,getpass
from flask_online_store import create_app
from flask_online_store.models import db,Admin
def main():
    p=argparse.ArgumentParser();p.add_argument('command',choices=['init','admin','routes']);args=p.parse_args()
    app=create_app()
    with app.app_context():
        if args.command=='init':db.create_all();print('Database initialized.')
        elif args.command=='routes':print(app.url_map)
        else:
            name=input('Admin username: ').strip();password=getpass.getpass('Password: ')
            if not name or len(password)<12:raise SystemExit('Use a name and at least 12 password characters.')
            Admin().save({'username':name,'password':password,'email':'admin@example.com'})
            print('Admin created.')
if __name__=='__main__':main()
