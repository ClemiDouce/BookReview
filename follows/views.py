from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView

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
            found_user = User.objects.get(username=request.POST['searched-user'])
            try:
                UserFollows.objects.get(user=request.user, followed_user=found_user)
                context['msg'] = f"Vous suivez déja {found_user.username}"
            except UserFollows.DoesNotExist:
                if found_user != request.user:
                    context['msg'] = f"Vous suivez maintenant {found_user.username}"
                    follow = UserFollows.objects.create(user=request.user, followed_user=found_user)
                    follow.save()
                else:
                    context['msg'] = "Vous ne pouvez pas vous suivre"
        except User.DoesNotExist:
            context['msg'] = "Cet utilisateur n'existe pas"
        return render(request, 'follows/abonnement.html', context)

class UnfollowView(DeleteView):
    model = UserFollows
    template_name = "follows/unfollow.html"
    success_url = reverse_lazy('follows:abonnement')