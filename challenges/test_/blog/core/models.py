from django.db import models


class Address(models.Model):
    user = models.ForeignKey('User', models.CASCADE, related_name="addresses")
    street = models.CharField(max_length=255)
    suite = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'addresses'


class Comment(models.Model):
    post = models.ForeignKey('Post', models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.name


    class Meta:
        managed = True
        db_table = 'comments'


class Post(models.Model):
    user = models.ForeignKey('User', models.CASCADE,
                             related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.title

    @property
    def total_comments(self):
        return self.comments.count()

    class Meta:
        managed = True
        db_table = 'posts'


class User(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()

    def total_posts(self):
        return self.posts.count()

    def total_comments(self):
        total = 0
        for p in self.posts.all():
            total += p.total_comments()
        return total


    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'users'
