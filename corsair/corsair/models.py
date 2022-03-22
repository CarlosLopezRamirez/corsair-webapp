from django.db import models

###################################################################
#                         Corsair User                            #
###################################################################

class Corsair_User(models.Model):
    class Employment():
        employer_name = models.CharField(max_length=20)
        title = models.CharField()
        location = models.CharField()
        description = models.TextField()
        start_year = models.DateField()
        end_year = models.DateField()

    CORSAIR_SECTORS = (
        ('C', 'Management Consulting'),
        ('B', 'Investment Banking'),
        ('T', 'Technology')
    )
    user_id = models.IntegerField()
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    linked_in = models.URLField()
    class_of = models.IntegerField()
    sector = models.CharField(max_length=1, choices=CORSAIR_SECTORS)
    profile_picture = models.FileField()
    password = models.CharField(max_length=200)
    verification_link_header = models.CharField(max_length=200)
    verified = models.IntegerField()
    bio = models.TextField()
    interests = models.JSONField()
    current_employer = Employment()
    past_employers = models.JSONField()