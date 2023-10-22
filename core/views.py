# core/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.exceptions import PermissionDenied
from django.utils.crypto import get_random_string
from .tools import send_markdown_email
from .models import WebhookToken

def generate_token():
    # 使用Django的内置函数生成一个随机的16字符令牌
    return get_random_string(length=16)

def generate_webhook(request):
    if request.method == 'POST':
        token = generate_token()
        data = request.POST.dict()
        webhook_token = WebhookToken.objects.create(token=token, data=data)
        return JsonResponse({'webhook_url': f'/webhook/{token}'})
    else:
        raise PermissionDenied

@csrf_exempt
@require_POST
def webhook(request, token):
    try:
        webhook_token = WebhookToken.objects.get(token=token)
    except WebhookToken.DoesNotExist:
        raise PermissionDenied

    data = webhook_token.data
    received_data = request.POST.dict()
    receiver_email = data["receiver_email"]
    markdown_text = data["markdown_text"]
    subject = data["subject"]

    if receiver_email:
        send_markdown_email(receiver_email, markdown_text, choice=1, subject=subject)
        return JsonResponse({'message': f'已发送 {markdown_text} 到邮箱 {receiver_email}'})
    else:
        return JsonResponse({'error': '接收邮箱为空'}, status=403)
