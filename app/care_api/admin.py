from django.contrib import admin
from care_api import models

# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
admin.site.register(models.OrgDetails)
admin.site.register(models.DonationHistory)