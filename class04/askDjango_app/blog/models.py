from django.db import models


# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 객체만 출력시 어떤 포맷으로 보여줄 것인가를 결정함
    # 객체 조회와 상관 없음
    def __str__(self):
        return self.title

'''
1) ./manage.py makemigrations blog
2) blog/migrations/0001_initial.py 파일 확인
3) ./manage.py sqlmigrate blog 0001_initial 명령으로 해당 migrations은 어떤 작업을 수행하는지 SQL 검토 하기
4) ./manage.py migrate blog 명령으로 DB 적용
5) SQLite Browser 를 통해서 DB TABLE 확인
'''

'''

# 필수 필드를 model에 추가시 기본 값 셋팅 처리

➜  askDjango_app git:(master) ./manage.py makemigrations 
You are trying to add a non-nullable field 'author' to post without a default; we can't do that (the database needs something to populate existing rows).
# 'author' 필드는 필수 필드인데 불구하고 null 도 허용하지 않고 default 값도 없는데, 어떤 값을 저장해야 하는가?
# 문제가 되는 필드(컬럼)이 어느 것인지 꼭 확인 !!!

Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
# 값 입력 진행

 2) Quit, and let me add a default in models.py
# 나중에 makemigratins을 하겠음. 그냥 종료.
 
Select an option: 1

Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
# timezone.now 값을 입력하라는 의미가 아님 !!! timezone.now 은 이미 import 되었으니 다시 import 할 필요는 없다.

Type 'exit' to exit this prompt
>>> '값입력'
# 위 값입력은 ''를 통해 문자열을 입력해 줘야 하며, default 값을 설정 하게 된다. 유효성 검사를 하지 않기 때문에 값 입력을 조심 해야 한다.
# 값 입력 후에는 필히 migrate를 하기 전에 migrations 파일을 점검 해야 한다. default 값이 제대로 들어갔는지 확인 해야 한다.


'''