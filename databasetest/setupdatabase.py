from userinfo import db, Userdetails

### Creates all the tables. Model --> Database Table###

db.create_all()

kat = Userdetails('Katharina', 'hello@katharinaalf.com')
fab = Userdetails('Fabby', 'fabbie@gmail.com')

print(kat.id)
print(fab.id)

db.session.add_all[(kat, fab)]
db.session.commit()

print(kat.id)
print(fab.id)

