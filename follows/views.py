from django.shortcuts import render
from django.views.generic import TemplateView

from follows.models import UserFollows


class AbonnementView(TemplateView):
    template_name = 'follows/abonnement.html'

    def post(self, request, *args, **kwargs):
        context = super().get_context_data()
        context["followed_list"] = UserFollows.objects.filter(followed_user=request.user)
        context["following_list"] = UserFollows.objects.filter(user=request.user)
        return render(request, 'follows/abonnement.html', context)

class UnfollowView(TemplateView):
    template_name = "follows/abonnement.html"