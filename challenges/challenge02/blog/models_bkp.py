from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='addresses')
    street = models.CharField(max_length=200)
    suite = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return f'Street: {self.street},' \
               f'Suite: {self.suite},' \
               f'City: {self.city},' \
               f'Zipcode: {self.zipcode} '

    class Meta:
        ordering = ('street',)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='posts', db_column='userId')
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f'Title: {self.title},' \
               f'Body: {self.body},'

    class Meta:
        ordering = ('title',)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments',
                             db_column='postId')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return f'Name: {self.name},' \
               f'E-mail: {self.email},' \
               f'Body: {self.body}'
