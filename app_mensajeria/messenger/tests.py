from django.test import TestCase
from django.contrib.auth.models import User

from .models import Message, Thread

# Create your tests here.


class ThreadTestCase(TestCase):
    def setUp(self) -> None:
        """
          2 test users => name + email + pass
          1 thread
        """

        self.userTest1 = User.objects.create_user(

            'userTest1',
            None,
            'test1234'
        )

        self.userTest2 = User.objects.create_user(

            'userTest2',
            None,
            'test1234'
        )

        self.userTest3 = User.objects.create_user(
            'userTest3',
            None,
            'test1234'
        )

        self.thread = Thread.objects.create()

    def test_add_users_to_thread(self) -> None:
        """
          Add users to the thread and check the count.
          The number of users in the thread should equal N, where N is the number of users added.
        """
        self.thread.users.add(self.userTest1, self.userTest2)
        self.assertEqual(len(self.thread.users.all()), 2)

    def test_filter_thread_by_users(self):
        """
          Test: Filter threads by multiple users and verify the result.

          This test adds two users to a thread and then filters threads that include both users.
          It asserts that the retrieved thread matches the one originally created.
        """

        self.thread.users.add(self.userTest1, self.userTest2)

        # queryset
        threads = Thread.objects.filter(
            users=self.userTest1
        ).filter(
            users=self.userTest2
        )

        self.assertTrue(threads.exists())
        self.assertEqual(self.thread, threads.first())

    def test_filter_non_existent_thread(self):
        """
          Test: Filter threads by users not assigned to any thread.

          This test attempts to retrieve threads that include two users who have not been added to any thread.
          It asserts that the resulting QuerySet is empty, confirming no such thread exists.
        """
        # queryset
        threads = Thread.objects.filter(
            users=self.userTest1
        ).filter(
            users=self.userTest2)

        self.assertEqual(len(threads), 0)

    def test_add_message_to_thread(self):
        """
          Test: Add messages to a thread and verify they are properly stored.

          This test creates two users and two messages, then adds the messages to a thread.
          It asserts that both messages are present in the thread and prints their content for verification.
        """
        self.thread.users.add(self.userTest1, self.userTest2)

        message1 = Message.objects.create(
            user=self.userTest1, content='userTest1 says hello to userTest2')
        message2 = Message.objects.create(
            user=self.userTest2, content='here userTest2 hello to userTest1')

        self.thread.message.add(message1, message2)

        self.assertEqual(len(self.thread.message.all()), 2)

        for message in self.thread.message.all():
            print("{}: {}".format(message.user, message.content))

    def test_add_message_from_user_not_in_thread(self):
        """
            Test: Check if a third person messages (not in the thread) can be add in the thread.
        """
        self.thread.users.add(self.userTest1, self.userTest2)

        message1 = Message.objects.create(
            user=self.userTest1, content='userTest1 says hello to userTest2')
        message2 = Message.objects.create(
            user=self.userTest2, content='here userTest2 hello to userTest1')
        message3 = Message.objects.create(
            user=self.userTest3, content='here userTest3 this message should not be in the thread')

        self.thread.message.add(message1, message2, message3)

        self.assertEqual(len(self.thread.message.all()), 2)

        # for message in self.thread.message.all():
        #     print("{}: {}".format(message.user, message.content))

    def test_find_thread_with_custom_manager(self):
        """
            Test: Use the custom manager to find a thread by two users.

            This test adds two users to a thread and uses the custom manager's 'find' method to retrieve it. It asserts that the returned thread matches the one originally created.
        """

        self.thread.users.add(self.userTest1, self.userTest2)

        thread = Thread.objects.find(  # type: ignore

            self.userTest1, self.userTest2)
        self.assertEqual(self.thread, thread)

    def test_find_or_create_thread_with_custom_manager(self):
        """
            Test: Use the custom manager to find or create a thread by two users.

            This test adds two users to a thread and uses the custom manager's 'find_ior_create' method to retrieve it. It asserts that the returned thread matches the one originally created.
        """

        self.thread.users.add(self.userTest1, self.userTest2)

        thread = Thread.objects.find_or_create(  # type: ignore
            self.userTest1, self.userTest2)

        self.assertEqual(self.thread, thread)

        thread = Thread.objects.find_or_create(  # type: ignore
            self.userTest1, self.userTest3)

        self.assertIsNotNone(self.thread, thread)
