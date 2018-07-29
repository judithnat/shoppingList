from django.db import models
from django.utils import timezone

class Shoplistclass(models.Model):
    
    
    SHOPCHOICES = (
        ('SM', 'supermarket'),
        ('BL', 'bramcotelane'),
        ('TN', 'town'),
        ('OS', 'other_shop'),
    )
    
    CATEGORYCHOICES = (
        ('FD', 'food'),
        ('CL', 'cleaning'),
        ('PH', 'pharmacy'),
        ('CT', 'clothes'),
        ('OC', 'other_category'),
    )
    
    TIMESCALECHOICES = (
        ('UG', 'urgent'),
        ('SN', 'soon'),
        ('LU', 'lessurgent'),
        ('ST', 'sometime'),
            )
    
    author = models.ForeignKey('auth.User')
    item = models.CharField(max_length=200)
    shop = models.CharField(max_length=20, choices = SHOPCHOICES, default='SM')
    category = models.CharField(max_length=20, choices = CATEGORYCHOICES, default='FD')
    quantity = models.IntegerField()
    entered_date = models.DateTimeField(auto_now_add=True)
    urgency = models.CharField(max_length=20, choices = TIMESCALECHOICES, default='SN')

    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.item #j converts object to string, when print get something useful like #John ; not <model object.; useful for debugging
