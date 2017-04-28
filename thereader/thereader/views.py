from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect

from .utils import make_mp3_file


@require_http_methods(["GET"])
def home(request):
    return render(
        request,
        'index.html',
    )


@require_http_methods(["POST"])
def make_mp3_file_view(request):
    if request.method == 'POST':
        text = request.POST['text']
        make_mp3_file(text, 'mijin', 0)
        return redirect('home')
