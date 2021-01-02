from django.db import models
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Plan(models.Model):
    destination =models.CharField(max_length=255)
    start_date=models.DateField()
    end_date=models.DateField()
    description=models.TextField()
    user=models.ForeignKey(User,related_name='created_by',on_delete=models.CASCADE)
    who_join=models.ManyToManyField(User,related_name="joined_user")



def insert_PlanRecord(destination,start_date,end_date,description,user):
    plan=Plan.objects.create(destination=destination,start_date=start_date,end_date=end_date,description=description,user=user)
    return plan



def insert_new_user(fname,lname,email,passwd):
    user=User.objects.create(first_name=fname,last_name=lname,email=email,password=passwd)
    return user


def is_duplicate_email(email):
    users = User.objects.filter(email=email).values()
    if len(users):
        return True
    return False
    return users[0]


def get_userByEmail(email):
    users = User.objects.filter(email=email)
    if users:
        return users[0]
    return None

def get_userById(id):
    user =User.objects.get(id=id)
    return user

def get_mytravelsById(userId):
    user=get_userById(userId)
    alltravels=Plan.objects.filter(user=user)
    return alltravels


def get_allPlan():
    plans=Plan.objects.all()
    return plans

def get_planById(id):
    plan=Plan.objects.get(id=id)
    return plan