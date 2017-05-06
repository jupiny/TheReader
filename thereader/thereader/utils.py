import os
import sys
import urllib.request
import datetime

from django.conf import settings


def make_mp3_file(text, speaker, speed):
    enc_text = urllib.parse.quote(text)
    data = "speaker={speaker}&speed={speed}&text={text}".format(
                speaker=speaker,
                speed=speed,
                text=enc_text,
            )
    url = "https://openapi.naver.com/v1/voice/tts.bin"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", os.environ.get('CLIENT_ID'))
    request.add_header("X-Naver-Client-Secret", os.environ.get('CLIENT_SECRET'))
    response = urllib.request.urlopen(request, data=data.encode('utf-8'))
    rescode = response.getcode()
    if(rescode == 200):
        print("TTS mp3 저장")
        response_body = response.read()
        print('Response 데이터 읽음')
        media_dir = settings.MEDIA_ROOT
        print('media_dir : ' +  media_dir)
        if not os.path.exists(media_dir):
            os.makedirs(media_dir)
            print('media 폴더 생성')
        remove_startwith_file(media_dir, 'voice')
        print('voice.mp3 파일 제거')
        filename = set_filename_format('voice.mp3')
        newfile= os.path.join(media_dir, filename)
        print('newfile : ' +  newfile)
        with open(newfile, 'wb') as f:
            f.write(response_body)
            print('mp3 파일 저장')
        return filename
    else:
        print("Error Code:" + rescode)


def set_filename_format(filename):
    now = datetime.datetime.now()
    return "{filename}_{year}{month}{day}{microsecond}{extension}".format(
        filename=os.path.splitext(filename)[0],
        year =now.year,
        month =now.month,
        day =now.day,
        microsecond=now.microsecond,
        extension=os.path.splitext(filename)[1],
    )


def remove_startwith_file(directory, startwith_name):
    for fname in os.listdir(directory):
        if fname.startswith(startwith_name):
            os.remove(os.path.join(directory, fname))
