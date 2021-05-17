from django.contrib import admin

from task_manager.tasks import models
# Register your models here.


admin.site.register(models.Status)
admin.site.register(models.Task)
