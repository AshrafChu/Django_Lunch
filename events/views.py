from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from django.utils.decorators import classonlymethod
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from .forms import EventForm, OrderForm
from .models import Event, Order
from braces.views import LoginRequiredMixin

# Create your views here.

class EventCreateView(LoginRequiredMixin,CreateView):
    form_class = EventForm
    http_method_names = ('post',)
    model = Event

class EventDetailView(LoginRequiredMixin,DetailView):
    model = Event

    def get_order(self, user):
        try:
            order = Order.objects.get(user=user, event=self.get_object())
        except Order.DoesNotExist:
            order = None
        return order


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        order = self.get_order(user=self.request.user)
        order_form = OrderForm(instance=order)
        order_form.fields['item'].queryset = self.object.store.menu_items.all()
        data['order_form'] = order_form
        return data 
    
    def post(self, request, *args, **kwargs):
        order = self.get_order(user=request.user)
        form = OrderForm(request.POST, instance=order)
        if not form.is_valid():
            return HttpResponseBadRequest()
        order = form.save(commit=False)
        order.user = request.user
        order.event = self.get_object()
        order.save()
        return redirect(order.event.get_absolute_url())


 






