from webbrowser import get
from django.shortcuts import get_object_or_404, redirect, render
from matplotlib.style import context
from .models import Port
from.forms import PortForm
# Create your views here.
def home(request):
    portfolio=Port.objects.all()
    context={
        "portfolio":portfolio
    }
    return render(request,"home.html",context)
    #CRUD(CREATE,READ,UPDATE,DELETE)

    #CREATE
def Create(request):
    form=PortForm()
    if request.method=='POST':
        form=PortForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("portfolio:home")
            #  HttpResponseRedirect(reverse("portfolio:home"))

    context={"form":form}
    return render(request,"forms.html",context)
# def Detail(request, pk):
#     portfolio = Port.objects.get(id=pk)

#     context = {
#         'portfolio':portfolio
#     }
#     return render(request, 'detail.html', context)

    #upadete(CRUD)
# def Update(request,pk):
#   form=PortForm(instance=portfolio)
#   portfolio=get_object_or_404(Port,id=pk)
#   if request.method=="POST":
#       form=PortForm(data=request.POSt,instance=portfolio)
#       if form.is_valid():
#           form.save()
#           return redirect("Portfolio:datail",kwargs={"pk":portfolio.id})
#   context={
#       "form":form
#   }
#   return render (request,"forms.html",context)

def Delete(request,pk):
    portfolio=get_object_or_404(PortForm ,id=pk)
    if request.method=="POST":
        portfolio.delete()
        return redirect("portfolio:home")
    context={
        "portfolio":portfolio}
    return render(request,"delete.html",context)




         