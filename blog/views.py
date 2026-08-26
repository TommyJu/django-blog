from django.shortcuts import render

# Django templates are implicitly loaded from templates/
def post_list(request):
    return render(request, 'blog/post_list.html', {})