from django.db import models

###################################################################
#                         Corsair User                            #
###################################################################

class Corsair_User(models.Model):
    CORSAIR_SECTORS = (
        ('C', 'Management Consulting'),
        ('B', 'Investment Banking'),
        ('T', 'Technology')
    )
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    email = models.EmailField()
    linked_in = models.URLField()
    class_of = models.IntegerField()
    sector = models.CharField(max_length=1, choices=CORSAIR_SECTORS)
    profile_picture = models.FileField()
    password = models.CharField()
    verification_link_header = models.CharField(max_length=200)
    verified = models.BooleanField(False)
    bio = models.TextField()


