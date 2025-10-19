from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    """
      User Messages 1:N
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class ThreadManager(models.Manager):

    def find(self, user1, user2):
        """
          Returns the first thread that includes both user1 and user2.
          If no such thread exists, returns None.
        """
        queryset = self.filter(users=user1).filter(users=user2)

        if len(queryset) > 0:
            return queryset.first()
        return None

    def find_or_create(self, user1, user2):
        """
          Retrieves an existing thread between two users, or creates a new one if none exists.

          Parameters:
              user1 (User): First participant.
              user2 (User): Second participant.

          Returns:
              Thread: A thread instance that includes both users.
        """

        thread = self.find(user1, user2)

        if thread is None:
            thread = Thread.objects.create()
            thread.users.add(user1, user2)
        return thread


class Thread(models.Model):
    """
      Represents a conversation thread where users exchange messages.
      Each thread includes participants and their respective messages.

    """
    users = models.ManyToManyField(User, related_name='threads')
    message = models.ManyToManyField(Message)

    objects = ThreadManager()
