from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxLengthValidator


User = get_user_model()


class Blog(models.Model):
    user = models.OneToOneField(User,
                                null=False,
                                blank=False,
                                related_name='blog',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField(validators=[MaxLengthValidator(140), ])
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name="Дата публикации")
    blog = models.ForeignKey(Blog,
                             blank=False,
                             related_name='post',
                             null=False,
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Follow(models.Model):
    user = models.ForeignKey(User,
                             blank=False,
                             related_name='following',
                             on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,
                             blank=False,
                             related_name='following',
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"


class Read(models.Model):
    user = models.ForeignKey(User,
                             blank=False,
                             related_name='read',
                             on_delete=models.CASCADE)
    post = models.ForeignKey(Post,
                             blank=False,
                             related_name='read',
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Прочитан"
        verbose_name_plural = "Прочитанные"
