from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='addresses')
    street = models.CharField(max_length=200)
    suite = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=10)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='posts')
    title = models.CharField(max_length=200)
    body = models.TextField()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
