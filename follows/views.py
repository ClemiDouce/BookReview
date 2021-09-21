from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView

from follows.models import UserFollows


class AbonnementView(TemplateView):
    template_name = 'follows/abonnement.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["followed_list"] = UserFollows.objects.filter(followed_user=self.request.user)
        context["following_list"] = UserFollows.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        try:
            founded_user = User.objects.get(username=request.POST['searched-user'])
            if founded_user != request.user:
                context['msg'] = f"User {founded_user.username} added to your following list"
                follow = UserFollows.objects.create(user=request.user, followed_user=founded_user)
                follow.save()
            else:
                context['msg'] = "You can't follow yourself, dumbass"
        except User.DoesNotExist:
            context['msg'] = "No user found"
        return render(request, 'follows/abonnement.html', context)

class UnfollowView(TemplateView):
    template_name = "follows/abonnement.html"