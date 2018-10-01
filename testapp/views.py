from django.shortcuts import render


# Create your views here.
from dcxt.models import Img, Dish


def upload_img(request):
    if request.method == 'POST':
        img_info = request.content_params.get('info')
        img_by = Dish.objects.get(id=request.POST.get(id))
        img = Img(img_url=request.FILES.get('img'), img_info=img_info, img_by=img_by)
        img.save()
    return render(request, 'imgupload.html')