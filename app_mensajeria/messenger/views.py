from django.db.models.base import Model as Model
from django.contrib.auth.models import User
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from .models import Message, Thread

# Create your views here.


@method_decorator(login_required, name='dispatch')
class ThreadList(TemplateView):
    template_name = 'messenger/threads_list.html'


@method_decorator(login_required, name='dispatch')
class ThreadDetail(DetailView):
    model = Thread

    def get_object(self):
        obj = super().get_object()
        if self.request.user not in obj.users.all():  # type: ignore
            raise Http404
        return obj

# view to add new message


def add_message(request, pk):
    """
        Adds a new message to an existing conversation thread if the user is authenticated.

        Parameters:
            request (HttpRequest): The incoming HTTP request, expected to contain a 'content' parameter via GET.
            pk (int): The primary key of the Thread object to which the message will be added.

        Behavior:
            - If the user is authenticated and a 'content' value is provided, a new Message is created and linked to the specified Thread.
            - If the Thread does not exist, a 404 error is raised.
            - If the user is not authenticated, a 404 error is raised.
            - If no content is provided, no message is created and the response remains unchanged.

        Returns:
            JsonResponse: A JSON object with a 'created' key indicating whether the message was successfully created.
    """
    json_response = {

        'created': False
    }

    if request.user.is_authenticated:
        content = request.GET.get('content', None)
        if content:
            thread = get_object_or_404(Thread, pk=pk)
            message = Message.objects.create(
                user=request.user,
                content=content
            )

            thread.message.add(message)

            json_response['created'] = True
    else:
        raise Http404("User is not authenticated")

    return JsonResponse(json_response)


@login_required
def newThread(request, username):
    user = get_object_or_404(User, username=username)
    thread = Thread.objects.find_or_create(user, request.user)  # type: ignore

    return redirect(reverse_lazy('messenger:thread_detail', args=[thread.pk]))
