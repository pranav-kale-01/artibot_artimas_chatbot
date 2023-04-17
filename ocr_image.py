from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from io import BytesIO
import requests

@csrf_exempt
def perfrom_ocr(request, *args, **kwargs):
    img = request.FILES["user-file"].read() 
    stream = BytesIO(img)
    image = Image.open(stream).convert("RGB")
    stream.close()
    photo_path = 'test.png'
    image.save(photo_path)
    url = "http://127.0.0.1:5000/upload_image"

    payload={}
    files=[
        ('image',('Test.png',open('Test.png','rb'),'image/png'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)

    response_json = JsonResponse( {'data' : response.text } )

    return response_json