from app import db, Userdetails

### Creates all the tables. Model --> Database Table###


kat = Userdetails('Katharina', 'hello@katharinaalf.com')
anne = Userdetails('Anne', 'anneh@gmail.com')

db.create_all()

print(kat.id)
print(anne.id)

db.session.add_all([kat, anne])
db.session.commit()

print(kat.id)
print(anne.id)

