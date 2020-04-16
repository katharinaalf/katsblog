from userinfo import db, Userdetails

#### CREATE ####

new_signup = Userdetails('Katharina', 'hello@katharinaalf.com')
db.session.add(new_signup)
db.session.commit()

#### READ ####

all_signups = Userdetails.query.all()  ## this will return a list of all sign ups in the table ###
print(all_signups)

#### SELECT BY ID ####

signup_one = Userdetails.query.get(1)
print(signup_one.name)

#### FILTERS #### 
signup_kat = Userdetails.query.filter_by(name = 'kat')
print(signup_kat.all())

### UPDATE ###

first_signup = Userdetails.query.get(1)
first_signup.email = 'hello@katharinaalf.com'
db.session.add(first_signup)
db.session.commit()

### DELETE ####

second_signup = Userdetails.query.get(2)
db.session.delete(second_signup)
db.session.commit()

#

all_signups = Userdetails.query.all()
print(all_signups)

