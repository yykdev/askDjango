from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

'''
1) ./manage.py makemigrations blog
2) blog/migrations/0001_initial.py 파일 확인
3) ./manage.py sqlmigrate blog 0001_initial 명령으로 해당 migrations은 어떤 작업을 수행하는지 SQL 검토 하기
4) ./manage.py migrate blog 명령으로 DB 적용
5) SQLite Browser 를 통해서 DB TABLE 확인
'''