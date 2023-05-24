
# Create your views here.
from django.shortcuts import render
import openai
# Create your views here.

openai.api_key = "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"
#API 키를 설정하면 openai.ChatCompletion.create()과 같은 함수를 호출할 때 인증이 자동으로 수행

#chatGPT에게 채팅 요청 API
def chatGPT(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    print(completion)
    result = completion.choices[0].message.content
    return result

#chatGPT에게 그림 요청 API
def imageGPT(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256"
    )
    result =response['data'][0]['url']
    return result

def index(request):
    return render(request, 'selfchatgpt/index.html')

def chat(request):
    #post로 받은 question
    prompt = request.POST.get('question')


    #type가 text면 chatGPT에게 채팅 요청 , type가 image면 imageGPT에게 채팅 요청
    result = chatGPT(prompt)

    context = {
        'question': prompt,
        'result': result
    }

    return render(request, 'selfchatgpt/result.html', context) 