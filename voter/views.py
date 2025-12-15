from django.shortcuts import render,redirect,get_object_or_404
from voter.models import Voter
from voter.forms import voter_form
from datetime import date
import string,random

# Create your views here.
def home(request):
    
    return render(request,'home.html')

def generate_voter_id():
    characters=string.ascii_uppercase+string.digits
    return ''.join(random.choice(characters) for i in range(10))

def post_voter(request):
    if request.method=="POST":
        form=voter_form(request.POST,request.FILES)
        if form.is_valid(): 
            voter=form.save(commit=False)
            voter.voter_id=generate_voter_id()
            voter.save()
            return redirect('get_voter',id=voter.id)
    
    else:
        form=voter_form()
    return render(request,'voter_form.html',{'form':form})

def get_voter(request,id):
    data=get_object_or_404(Voter,id=id)
    return render(request,'voter_card.html',{'data':data})
            
def get_table(request):
    table=Voter.objects.all()
    return render(request,'voter_list.html',{'table':table})