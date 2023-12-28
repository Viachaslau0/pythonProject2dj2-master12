from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from userlist.forms import Sigh_inForm, Login_inForm

from .models import Category, FoodItem

from django.views import View
from django.http import HttpResponse

class OrderingMixin:
    def get_ordering(self):
        order_by = self.request.GET.get("order_by")

        if not order_by:
            return self.ordering

        if hasattr(self.model, order_by.removeprefix("-")):
            return order_by

        return self.ordering

class RestaurantView(View):
    def get(self, request):
        register_form = Login_inForm()
        login_form = Sigh_inForm()
        return render(request, 'home.html', {'register': register_form, 'login': login_form})

    def post(self, request):
        # Обработка формы регистрации
        register_form = Login_inForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('home')

        # Обработка формы входа
        login_form = Sigh_inForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

        return render(request, 'home.html', {'register': register_form, 'login': login_form})
class CategoryListView(OrderingMixin, ListView):
    model = Category
    ordering = "name"
    template_name = "category_list.html"


class CategoryDetailView(OrderingMixin, DetailView):
    model = Category
    ordering = "name"
    template_name = "category_detail.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fooditems'] = FoodItem.objects.filter(category=self.object)
        return context

class FoodItemListView(OrderingMixin, ListView):
    model = FoodItem
    ordering = "name"
    template_name = "fooditem_list.html"


class FoodItemDetailView(OrderingMixin, DetailView):
    model = FoodItem
    template_name = "fooditem_detail.html"
    ordering = "name"