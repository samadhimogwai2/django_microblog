from django.contrib import admin
from .models import *

# 管理画面で使用できるようにmodelを登録する
admin.site.register(Post)
admin.site.register(Comment)
