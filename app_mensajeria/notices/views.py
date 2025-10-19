from django.shortcuts import redirect, render
from .models import Notice
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import NoticeForm
# decorador para control de acceso
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
# fin decorador control de acceso


# Create your views here.


class StaffRequiredMixin(object):
    """
        Mixin (clase que modifica el comportamiento de otra clase) requerir que el usuario sea del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class NoticeDetailView(DetailView):
    model = Notice


class NoticeListView(ListView):
    model = Notice


@method_decorator(staff_member_required, name='dispatch')
class NoticeCreate(CreateView):
    model = Notice
    form_class = NoticeForm
    success_url = reverse_lazy('notices:notices')


@method_decorator(staff_member_required, name='dispatch')
class NoticeUpdate(UpdateView):
    model = Notice
    form_class = NoticeForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('notices:update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')
class NoticeDelete(DeleteView):
    model = Notice
    success_url = reverse_lazy('notices:notices')
