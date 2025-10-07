from django.shortcuts import render

def index(request):
    return render(request, 'website/index.html')

def login_page(request):
    return render(request, 'website/loginpage.html')

def join(request):
    return render(request, 'website/join.html')

def help_center(request):
    return render(request, 'website/helpcenter.html')

def premium(request):
    return render(request, 'website/premiummembershipsdetails.html')

def terms(request):
    return render(request, 'website/terms.html')

def privacy(request):
    return render(request, 'website/privacy.html')

def safety(request):
    return render(request, 'website/safetyguidelines.html')

def trust(request):
    return render(request, 'website/trustsafety.html')

def success_stories(request):
    return render(request, 'website/sucessstories.html')

def about(request):
    return render(request, 'website/aboutus.html')

def contact(request):
    return render(request, 'website/contact us.html')

def discover(request):
    return render(request, 'website/discoverelitemembers.html')

def events(request):
    return render(request, 'website/exclusiveevents.html')

def faq(request):
    return render(request, 'website/faq.html')
