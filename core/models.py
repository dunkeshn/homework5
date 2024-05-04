from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=50, blank=True)
    nickname = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.nickname

class UserChats(models.Model):
    nickname = models.ForeignKey(User, on_delete=models.CASCADE)
    chat_nickname = models.CharField(max_length=20)
    message_value = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

    def __str__(self):
        return self.chat_nickname
