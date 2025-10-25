from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    return render(request, 'website/index.html')

def login_page(request):
    if request.method == 'POST':
        messages.success(request, 'Welcome back!')
        return redirect('dashboard')
    return render(request, 'website/loginpage.html')

def join(request):
    if request.method == 'POST':
        messages.success(request, 'Welcome to AgreedDating! Your account has been created successfully.')
        return redirect('create_profile_step1')
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

def dashboard(request):
    return render(request, 'website/dashboard.html')

def profile_detail(request, username):
    context = {'username': username}
    return render(request, 'website/profile_detail.html', context)

def create_profile(request):
    return redirect('create_profile_step1')

def create_profile_step1(request):
    if request.method == 'POST':
        messages.success(request, 'Profile information saved! Continue to step 2.')
        return redirect('create_profile_step2')
    return render(request, 'website/create_profile_step1.html')

def create_profile_step2(request):
    if request.method == 'POST':
        messages.success(request, 'Personality details saved! Continue to step 3.')
        return redirect('create_profile_step3')
    return render(request, 'website/create_profile_step2.html')

def create_profile_step3(request):
    if request.method == 'POST':
        messages.success(request, 'Preferences saved! Final step.')
        return redirect('create_profile_step4')
    return render(request, 'website/create_profile_step3.html')

def create_profile_step4(request):
    if request.method == 'POST':
        messages.success(request, 'Congratulations! Your profile is now complete and active.')
        return redirect('dashboard')
    return render(request, 'website/create_profile_step4.html')
