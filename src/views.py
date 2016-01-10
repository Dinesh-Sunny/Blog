from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from src.models import Post

class PostManager(View):

    def get(self, request):
        posts = Post.objects.all()

        return render(request,
                      'src/templates/index.html',
                      {'posts':posts}
                      )
