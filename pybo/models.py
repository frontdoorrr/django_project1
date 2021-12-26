from django.db import models

# Create your models here.
class Question(models.Model):
	subject = models.CharField(max_length=200)  # 글자 수가 제한된 필드의 경우 CharField 사용
	content = models.TextField()                # 글자 수를 제한할 수 없을 땐 TextField 사용
	create_date = models.DateTimeField()

	def __str__(self):
		return self.subject

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE) #CASCADE는 이 답변과 연결된 질문이 삭제될 경우 함께 삭제된다는 의미(종속된다는 의미)
	content = models.TextField()
	create_date = models.DateTimeField()
