from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)  # on-delete 옵션 :계정이 삭제되면 이 계정이 작성한 질문을 모두 삭제
	subject = models.CharField(max_length=200)  # 글자 수가 제한된 필드의 경우 CharField 사용
	content = models.TextField()                # 글자 수를 제한할 수 없을 땐 TextField 사용
	create_date = models.DateTimeField()

	def __str__(self):
		return self.subject

class Answer(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE) #CASCADE는 이 답변과 연결된 질문이 삭제될 경우 함께 삭제된다는 의미(종속된다는 의미)
	content = models.TextField()
	create_date = models.DateTimeField()


'''
********** 모델을 변경한 후에는 makemigrations와 migrate를 실행해 데이터베이스를 반드시 변경해주어야 한다. **********

1. console 창에 python3 manage.py makemigrations 입력
2. console 창에 python3 manage.py migrate 입력
'''
