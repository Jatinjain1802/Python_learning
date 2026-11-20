# from django.shortcuts import render
# from .mock_data import book

# def home_view(request):
#     return render(request, 'home.html', {'books': book})


from django.shortcuts import render
from .mock_data import BOOKS

def display_view(request):
    context = {
        'books' : BOOKS,
    }
    return render(request, 'display.html', context)

def display_table_view(request):
    context = {
        'books' : BOOKS,
    }
    return render(request, 'display_table.html', context)



def home_view(request):
    context = {
        'books' : BOOKS,
    }
    return render(request,'home.html',context)

def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    return render(request,'contact.html')
