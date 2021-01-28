from django.shortcuts import render, redirect,reverse
from .models import Lead,Agent
from .forms import LeadModelForm
from django.views import generic
   

# Create your views here.
class LandingPage(generic.TemplateView):
    template_name = "landing.html"



def landing_page(request):
    leads = Lead.objects.all()
    return  render(request, 'landing.html', {'leads':leads})
####### 
####### 
def lead_list(request):
    leads = Lead.objects.all()
    return  render(request, 'leads/lead_list.html', {'leads':leads})

class LeadListView(generic.ListView):
    template_name='leads/lead_list.html'
    queryset = Lead.objects.all()
    context_object_name = "leads"


#######
####### 

def lead_detail(request,pk):
    lead = Lead.objects.get(id=pk)
    return  render(request, 'leads/lead_detail.html', {'lead':lead})

class LeadDetail(generic.DetailView):
    template_name='leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = "lead"


#######
####### 

## CREATE NEW LEADS ##
def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads") 
    return  render(request, 'leads/lead_create.html', {'form':form})

class CreateLeadView(generic.CreateView):
    template_name='leads/lead_create.html'
    form_class = LeadModelForm
    def get_success_url(self):
        return reverse('leads:lead-list')
 
#######
####### 
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

class UpdateLeadView(generic.UpdateView):
    template_name='leads/lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()
    def get_success_url(self):
        return reverse('leads:lead-list')
#######
####### 
def lead_delete(request,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")

class DeleteLeadView(generic.DeleteView):
    template_name='leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse('leads:lead-list')

 
































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



