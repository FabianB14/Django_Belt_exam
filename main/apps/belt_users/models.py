from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from datetime import datetime


class LogUsersManager(models.Manager):
    def basic_registration(self, postData):
        now = datetime.now()
        result = {
            'status': False,
            'errors':[]
        }
        print(now)
        if len(postData['date_hired'])==0:
            result['errors'].append('please fillin date hired field')
        if str(now) < postData['date_hired']:
            result['errors'].append('date hired cannot be in the furture')
        if len(postData['name'])<2 :
            result['errors'].append('Name needs to be greater than 2 charaters.')
            print('yup errors')
        if len (postData['username']) == LogUsers.objects.filter(user_name = postData['username']):
            result['errors'].append('Username exist already.')
        if postData['password'] != postData['confirmation_password']:
            result['errors'].append('Passwords do not match')
        if len(postData['password']) <7:
            result['errors'].append('Password has to be more than 7 charaters.')
        if len(postData['username'])<3:
            result['errors'].append('Username is too short, has to be atleast 3 characters.')
        
        # if not EMAIL_REGEX.match(postData['email']):
        #     result['errors'].append('Invalid Email')
        if len(result['errors'])<1:
            result['status'] = True
            result['user_id']= LogUsers.objects.create(
                    name=postData['name'],
                    # last_name= postData['last'],
                    user_name=postData['username'],
                    password=bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode('utf-8'),
                    date_hired =postData['date_hired']
                    ).id
        return result

    def basic_login(self,postData):
        result  = {
            'status': False,
            'errors': []
        }

        existing_users = LogUsers.objects.filter(user_name= postData['username'])
        # if not EMAIL_REGEX.match(postData['email']):
        #     result['errors'].append('Invalid email or password did not matach.')
        if  len(existing_users) == 0:
            result['errors'].append('Invalid Username or password did not matach.')
        else:
            if  bcrypt.hashpw(postData['password'].encode(),existing_users[0].password.encode()):
                result['status'] = True
                result ['user_id'] = existing_users[0].id
        print(result)
        return result
        
        
class LogUsers(models.Model):
    # full_name = models.CharField(max_length = 30)
    name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length= 30)
    email_address = models.CharField(max_length=30)
    password = models.CharField(max_length= 30)
    age = models.AutoField
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    date_hired = models.DateField()
    objects = LogUsersManager()
    def __repr__(self):
        return "<users object:{} {} {}  >".format(self.name,  self.email_address, self.user_name)




# Create your models here.
