from django.forms import ModelForm

from review.models import Review


class CreateReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
