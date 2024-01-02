from django.shortcuts import render

# Create your views here.

def get_info(request):
    if request.method == "POST":
        context = {}
        context['f_name'] = request.POST.get('f_name')
        context['l_name'] = request.POST.get('l_name')
        context['food'] = request.POST.get('food')
        context['vacation'] = request.POST.get('vacation')
        return render(request, 'info.html', context)
    return render(request, 'form.html')
