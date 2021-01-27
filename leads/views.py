from django.shortcuts import render, redirect
from .models import Lead,Agent
from .forms import LeadModelForm
# Create your views here.
def lead_list(request):
    leads = Lead.objects.all()
    return  render(request, 'leads/lead_list.html', {'leads':leads})

def lead_detail(request,pk):
    lead = Lead.objects.get(id=pk)
    return  render(request, 'leads/lead_detail.html', {'lead':lead})

## CREATE NEW LEADS ##
def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
 
        
    return  render(request, 'leads/lead_create.html', {'form':form})

## UPDATE LEADS ##
def lead_update(request,pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
 
        
    return  render(request, 'leads/lead_update.html', {'form':form,'lead':lead,})






## CREATE NEW LEADS test1 ##
# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name  = form.cleaned_data['last_name']
#             age        = form.cleaned_data['age']
#             agent      = Agent.objects.first()
#             Lead.objects.create(
#                 first_name=first_name,last_name=last_name,age=age,agent=agent
#             )
#             return redirect("/leads")

        
#     return  render(request, 'leads/lead_create.html', {'form':form})

## UPDATE LEADS test1 ##
# def lead_update(request,pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name  = form.cleaned_data['last_name']
#             age        = form.cleaned_data['age']
#             agent      = Agent.objects.first()
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.agent = agent
#             lead.save()
#             return redirect("/leads")
 
        
#     return  render(request, 'leads/lead_update.html', {'form':form,'lead':lead,})



