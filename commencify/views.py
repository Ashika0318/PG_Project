from django.contrib import messages
from django.shortcuts import render, redirect
from commencify.models import employee
from scientist.models import requirement, registration

def commencify_RL(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        department=request.POST['department']
        password=request.POST['password']
        employee(name=name, email=email,phone=phone, department=department,password=password).save()
        messages.info(request,f"{name} Registration Successful")
        return render(request, "commencify/commencify_RL.html")
    return render(request,"commencify/commencify_RL.html")

def commencify_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            s = employee.objects.get(email=email, password=password)

            if s.grant:
                messages.info(request, "Commencify Login Successful")

                request.session['user_id'] = s.emp_id
                print( request.session['user_id'])
                return redirect("/commencify_home/")
            else:
                messages.info(request, "You need Management Approval to Access")
                return render(request, "commencify/commencify_RL.html")

        except employee.DoesNotExist:
            messages.info(request, "Invalid Email or Password")

    return render(request, "commencify/commencify_RL.html")


def commencify_logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id',None)
        messages.success(request,'Logout successful')
        return redirect('/')
    else:
        messages.success(request, 'Logout successful')
        return redirect('/')

def commencify_home(request):
    return render(request,"commencify/commencify_home.html")

def explore_req(request):
    data=requirement.objects.all()
    return render(request,"commencify/explore_req.html",{'data':data})

def process_req(request):
    data=requirement.objects.all()
    return render(request,"commencify/process_req.html",{'data':data})


import pandas as pd
def cresultprocess(request, s_id):
    data = requirement.objects.filter(s_id=s_id)
    csv_path = r'E:\Project\ML - Chemical Prints\Chemical_Prints\Origination Dataset.csv'
    df = pd.read_csv(csv_path)
    for _, row in df.iterrows():
        for i in data:
            if (i.tree_species,i.tree_origin) == (row['tree_species'],row['tree_origin']):
                i.age = row['age']
                i.wood_property = row['wood_property']
                i.density = row['density']
                i.hardness = row['hardness']
                i.grain_pattern = row['grain_pattern']
                i.durability = row['durability']
                i.eco_toxicology = row['eco_toxicology']
                i.eco_toxicity = row['eco_toxicity']
                i.eco_sustainability = row['eco_sustainability']
                i.save()
    d=registration.objects.get(s_id=s_id)
    d.cdone=True
    d.save()
    data1 = requirement.objects.get(s_id=s_id)
    data1.cdone1=True
    data1.save()

    messages.info(request, f"Requirements Processed Successfully for {s_id}")
    return render(request, 'commencify\process_req.html')


def c_result(request):
    data=requirement.objects.filter(cdone1=True)
    return render(request,"commencify/c_result.html",{'data':data})