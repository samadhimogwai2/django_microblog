from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    
class Comment(models.Model):
    # 関連データが削除された場合、同時に削除
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)