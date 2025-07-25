from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import uuid
from .utils import handle_conversation  # تأكد عندك دالة handle_conversation في utils.py

def chatbot_home(request):
    # يعرض ملف HTML داخل templates/chatbot.html
    return render(request, 'chatbot.html')


@csrf_exempt
def chatbot_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message')
            conversation_id = data.get('conversation_id') or str(uuid.uuid4())
            response_message = handle_conversation(user_message, conversation_id)
            return JsonResponse({'response': response_message, 'conversation_id': conversation_id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Only POST method allowed'}, status=405)

