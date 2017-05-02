from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect

from .utils import make_mp3_file

    
@require_http_methods(["GET"])
def home(request):
    text = request.session.pop('text', '')
    filename = request.session.pop('filename', '')
    speaker = request.session.pop('speaker', '')
    speed = request.session.pop('speed', '')
    return render(
        request,
        'index.html',
        context={
            'text': text,
            'filename': filename,
            'speaker': speaker,
            'speed': speed,
        },
    )


@require_http_methods(["POST"])
def make_mp3_file_view(request):
    if request.method == 'POST':
        text = request.POST['text']
        speaker = request.POST['speaker']
        speed = request.POST['speed']

        filename = make_mp3_file(text, speaker, speed)

        request.session['text'] = text
        request.session['filename'] = filename
        request.session['speaker'] = speaker
        request.session['speed'] = speed
        return redirect('home')
