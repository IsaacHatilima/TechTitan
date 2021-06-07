from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    if request.method == 'GET':
        return render(request, 'website_files/index.html', {'home' : True})


def about_us(request):
    if request.method == 'GET':
        return render(request, 'website_files/about_us.html', {'about' : True})

def why_us(request):
    if request.method == 'GET':
        return render(request, 'website_files/why_us.html', {'why_us' : True})
    
def out_team(request):
    if request.method == 'GET':
        return render(request, 'website_files/leadership-team.html')
    
def it_solutions(request):
    if request.method == 'GET':
        return render(request, 'website_files/it-solutions.html',{'it_things' : True})
    
def it_management_services(request):
    if request.method == 'GET':
        return render(request, 'website_files/it-management-services.html',{'it_things' : True})
    
def cyber_security_services(request):
    if request.method == 'GET':
        return render(request, 'website_files/cyber-security.html',{'it_things' : True})
    
def software_dev_services(request):
    if request.method == 'GET':
        return render(request, 'website_files/software-development.html',{'it_things' : True})
    
def networking_services(request):
    if request.method == 'GET':
        return render(request, 'website_files/cloud-computing.html',{'it_things' : True})    
      
def consulting_services(request):
    if request.method == 'GET':
        return render(request, 'website_files/consultations.html',{'it_things' : True})       
    
def backup_services(request):
    if request.method == 'GET':
        return render(request, 'website_files/data-backup.html',{'it_things' : True})        
    
def email_hosting(request):
    if request.method == 'GET':
        return render(request, 'website_files/email-hosting.html',{'it_things' : True})        

def web_hosting(request):
    if request.method == 'GET':
        return render(request, 'website_files/web-hosting.html',{'it_things' : True})  
    
def blogging(request):
    if request.method == 'GET':
        return render(request, 'website_files/blog.html') 
    
def contact(request):
    if request.method == 'GET':
        return render(request, 'website_files/contact-us.html', {'contact' : True}) 
    
def find_out(request):
    if request.method == 'POST':
        pass
    
def get_quote(request):
    if request.method == 'GET':
        return render(request, 'website_files/request-quote.html') 