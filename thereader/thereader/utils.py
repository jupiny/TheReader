import os
import sys
import urllib.request


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
        with open('dist/media/voice.mp3', 'wb') as f:
            f.write(response_body)
    else:
        print("Error Code:" + rescode)
