from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    return render(request, 'website/index.html')

def login_page(request):
    if request.method == 'POST':
        # Process login form
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # For now, just redirect to dashboard
        # In a real app, you would authenticate the user here
        messages.success(request, 'Successfully signed in!')
        return redirect('dashboard')
    
    return render(request, 'website/loginpage.html')

def join(request):
    if request.method == 'POST':
        # Process registration form
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        location = request.POST.get('location')
        
        # For now, just redirect to create profile
        # In a real app, you would create a user account here
        messages.success(request, 'Account created successfully! Please complete your profile.')
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
    return render(request, 'website/successstories.html')  # Fixed typo

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

# Add these missing views that are referenced in your templates
def dashboard(request):
    return render(request, 'website/dashboard.html')

def create_profile_step1(request):
    if request.method == 'POST':
        # Process step 1 data and move to step 2
        messages.success(request, 'Basic info saved! Now tell us more about yourself.')
        return redirect('create_profile_step2')
    
    # GET request - show the form
    messages.success(request, 'Profile creation started! Complete your profile to get matches.')
    return render(request, 'website/create_profile_step1.html')  # FIXED NAME

def create_profile_step2(request):
    if request.method == 'POST':
        # Process step 2 data and move to step 3
        messages.success(request, 'Personal details saved! Almost done.')
        return redirect('create_profile_step3')
    
    # GET request - show the form
    return render(request, 'website/create_profile_step2.html')  # FIXED NAME

def create_profile_step3(request):
    if request.method == 'POST':
        # Process step 3 data and move to step 4
        messages.success(request, 'Preferences saved! Final step.')
        return redirect('create_profile_step4')
    
    # GET request - show the form
    return render(request, 'website/create_profile_step3.html')  # FIXED NAME

def create_profile_step4(request):
    if request.method == 'POST':
        # Process step 4 data and redirect to success page
        messages.success(request, 'Profile completed successfully! Welcome to AgreedDating.')
        return redirect('join_success')
    
    # GET request - show the form
    return render(request, 'website/create_profile_step4.html')  # FIXED NAME

def create_profile(request):
    # Main profile creation entry point
    return redirect('create_profile_step1')

def join_success(request):
    # Show success page after profile completion
    messages.success(request, 'Welcome to AgreedDating! Your profile is now complete and active.')
    return render(request, 'website/join_success.html')

def profile_detail(request, username):
    # Profile detail view - for now just show a basic page
    context = {'username': username}
    return render(request, 'website/profile_detail.html', context)
