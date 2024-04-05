from django.contrib import messages
from django.shortcuts import redirect
def scientist_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            s = registration.objects.get(email=email, password=password)
            if s.approve:
                messages.info(request, f"Scientist Login Successful")
                request.session['user_id'] = s.s_id
                print( request.session['user_id'])
                s.login = True
                s.logout = False
                s.save()
                return redirect("/scientist_home/")
            else:
                messages.info(request, "You need Management approval to Access")
                return render(request, "scientist/scientist_RL.html")
        except registration.DoesNotExist:
            messages.info(request, "Invalid Email or Password")
    return render(request, "scientist/scientist_RL.html")

def index(request):
    return render(request,"home/index.html")
def scientist_home(request):
    return render(request,"scientist/scientist_home.html")

def scientist_logout(request):
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        try:
            s = registration.objects.get(s_id=user_id)
            s.logout = True
            s.login = False
            s.save()
            del request.session['user_id']
            messages.success(request, 'Logout successful')
            return redirect('/')
        except registration.DoesNotExist:
            messages.error(request, 'User not found')
        request.session.pop('user_id', None)
    else:
        messages.info(request, 'Logout successful')
    return redirect('/')
def scientist_RL(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        registration(name=name, email=email,phone=phone, password=password).save()
        messages.info(request,f"{name} Registration Successful")
        return render(request, "scientist/scientist_RL.html")
    return render(request,"scientist/scientist_RL.html")

def scientist_requirement(request):
    try:
        data = registration.objects.get(login=True)
        s_id = data.s_id
        crp_data = requirement.objects.get(s_id=s_id)
        messages.info(request, "Requirements already uploaded")
        return redirect("/scientist_home/")
    except:
        data = registration.objects.get(login=True)
        s_id = data.s_id
        if request.method=="POST":
            s_id = data.s_id
            tree_species=request.POST['tree_species']
            tree_origin=request.POST['tree_origin']
            wood_color=request.POST['wood_color']
            wood_grain_pattern=request.POST['wood_grain_pattern']
            requirement(s_id=s_id,tree_species=tree_species,tree_origin=tree_origin,wood_color=wood_color,
                     wood_grain_pattern=wood_grain_pattern).save()
            data = registration.objects.get(login=True)
            data.upload = True
            data.save()
            messages.info(request,"Requirement Uploaded Successfully")
            return redirect("/scientist_home/")
    return render(request,"scientist/scientist_requirement.html",{'s_id': s_id})

# def checkpoints(request):
#     data=registration.objects.get(login=True)
#     s = data.s_id
#     h = data.final
#     data1=requirement.objects.filter(s_id=s)
#     return render(request,'scientist/checkpoints.html', {'data':data,'h':h,'data1':data1})


from django.shortcuts import render, get_object_or_404
from .models import registration, requirement

def checkpoints(request):
    data = get_object_or_404(registration, login=True)
    s_id = data.s_id
    h = data.final
    data1 = requirement.objects.filter(s_id=s_id)

    return render(request, 'scientist/checkpoints.html', {'data': data, 'h': h, 'data1': data1})


