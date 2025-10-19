from django.db.models.signals import m2m_changed

from .models import Message, Thread, User


def not_third_user_messages_in_thread(sender, **kwargs):
    """
      Signal handler to prevent adding messages from users who are not part of the thread.

    """
    instance = kwargs.pop('instance', None)
    action = kwargs.pop('action', None)
    pk_set = kwargs.pop('pk_set', None)
    print(instance, action, pk_set)

    false_pk_set = set()
    # first: Intercept messages before they are added to the thread
    if action == 'pre_add':
        # Iterate over all message primary keys in pk_set
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            # If the message's user is not part of the thread:
            if msg.user not in instance.users.all():
                print("User: ({}), is not in the thread".format(msg.user))
                # Mark the message as invalid if its user is not in the thread
                false_pk_set.add(msg_pk)

    # Remove invalid messages from the pk_set
    pk_set.difference_update(false_pk_set)


m2m_changed.connect(not_third_user_messages_in_thread,
                    sender=Thread.message.through)
