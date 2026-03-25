from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def category(request):
    return render(request, 'category.html')

def blog_details(request):
    return render(request, 'blog_details.html')

def author_page(request):
    return render(request, 'author_page.html')

def contact(request):
    return render(request, 'contacts.html')

def search_result(request):
    return render(request, 'search_result.html')

def not_found(request):
    return render(request, '404.html')