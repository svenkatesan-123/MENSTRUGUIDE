from djongo import models

class DiscussionForum(models.Model):
    Distitle=models.CharField(max_length=255)
    DisDesc=models.TextField()


