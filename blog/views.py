from django.shortcuts import render

def post_list(request):
    return render(request, 'blod/post_list.html', {})
