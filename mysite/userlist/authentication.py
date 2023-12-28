from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from django.shortcuts import render, redirect


class EmailAuth(BaseBackend):
    user_form = get_user_model()

    def authenticate(self, request, user_email = None, password = None, **kwargs):

        try:
            user = self.user_form.objects.get(email=user_email)
            if user.check_password(password):
                return user
            return None

        except self.user_form.DoesNotExist:
            return None

    def get_user(self, user_id):

        try:
            return self.user_form.objects.get(pk=user_id)
        except self.user_form.DoesNotExist:
            return None

