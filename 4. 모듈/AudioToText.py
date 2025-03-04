# 1-1 audio2text--------------------
# OpenAI API 불러온 후, 음성 인식한 텍스트를 요약해서 리턴하는 함수
def AudioToText(audio_path, filename, Client):
    c = Client
    audio_file = open(audio_path + filename, "rb")
    transcript = c.audio.transcriptions.create(
        file=audio_file,
        model="whisper-1",
        language="ko",
        response_format="text",
        temperature=0.0
    )
    return transcript
