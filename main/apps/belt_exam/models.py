from django.db import models
from ..belt_users.models import LogUsers

class wish_itemManager(models.Manager):
    def add_wish(self,postData, user_id):
        result  = {
            'status': False,
            'errors': []
        }
        if len(postData['item_name']) <3:
            result['errors'].append('Items must be atleast 3 characters')
        if len(result['errors'])== 0:
            result['status'] = True
            logUser_id = LogUsers.objects.get(id = user_id)
            wish = wish_items.objects.create(
                    item_name = postData['item_name'],
                    item_creator = logUser_id
                )
            wish.wisher.add(logUser_id)
            wish.save()
        return result
    def add_another_wish(self, user_id, wish_id):
        logUser_id = LogUsers.objects.get(id = user_id)
        wish = wish_items.objects.get(id = wish_id)
        wish.wisher.add(logUser_id)
        wish.save()
    def remove_from_list(self,user_id,wish_id):
        
            logUser_id = LogUsers.objects.get(id = user_id)
            wish = wish_items.objects.get(id = wish_id)
            wish.wisher.remove(logUser_id)
            wish.save()
            

        


class wish_items(models.Model):
    item_name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)
    item_creator = models.ForeignKey(LogUsers, related_name = 'created_items', on_delete = models.CASCADE)
    wisher = models.ManyToManyField(LogUsers, related_name = 'wish_adder')
    objects = wish_itemManager()

# Create your models here.
