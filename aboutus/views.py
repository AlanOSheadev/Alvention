from django.shortcuts import render


# Create your views here.
def aboutus(request):
    """ A view that displays the about us page """
    return render(request, "aboutus.html")
