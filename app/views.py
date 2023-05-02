from django.shortcuts import render

# Create your views here.
def Built_In_Filters(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'I Am ChANdanA','dt':dt,'c':2}
    return render(request,'Built_In_Filters.html',d)