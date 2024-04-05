from django.contrib import messages
from django.core.files.base import ContentFile
from django.shortcuts import render,redirect
import random
from commencify.models import employee
from scientist.models import registration, requirement


def admin_login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        if username=="admin" and password=="admin":
            messages.info(request,"Admin Login Successful")
            return redirect("/admin_home/")
        elif username !="admin" and password=="admin":
            messages.error(request, "Incorrect Username!")
            return render(request, 'administrator/admin_login.html')
        elif username =="admin" and password!="admin":
            messages.error(request, "Incorrect Password!")
            return render(request, 'administrator/admin_login.html')
        elif username !="admin" and password!="admin":
            messages.error(request, "Incorrect Username and Password!")
            return render(request, 'administrator/admin_login.html')
        else:
            return render(request, 'administrator/admin_login.html')
    return render(request, 'administrator/admin_login.html')

def admin_home(request):
    return render(request,'administrator/admin_home.html')

def admins_logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id',None)
        messages.success(request,'Logout successful')
        return redirect('/')
    else:
        messages.success(request, 'Logout successful')
        return redirect('/')




def scientist_reg(request):
    data=registration.objects.all()
    return render(request,"administrator/scientist_reg.html",{'data':data})

def approve(request, id):
    datas =registration.objects.get(id=id)
    p = random.randint(10000, 50000)
    datas.s_id = f"S-{p}"
    print(p)
    datas.approve = True
    datas.reject = False
    datas.save()
    messages.info(request, f"Scientist [{datas.s_id}] Approval Successful")
    return redirect('/admin_home/')

def reject(request, id):
    datas =registration.objects.get(id=id)
    datas.reject = True
    datas.approve = False
    datas.save()
    messages.info(request, "Scientist Registration Rejected")
    return redirect('/admin_home/')

def commencify_reg(request):
    data=employee.objects.filter(department="Commencify")
    return render(request,'administrator/commencify_reg.html',{'data':data})

def grant(request, id):
    datas =employee.objects.get(id=id)
    p = random.randint(10000, 50000)
    datas.emp_id = f"C-{p}"
    print(p)
    datas.grant = True
    datas.revoke = False
    datas.save()
    messages.info(request, "Commencify Approval Successful")
    return redirect('/admin_home/')

def revoke(request, id):
    datas =employee.objects.get(id=id)
    datas.revoke = True
    datas.grant = False
    datas.save()
    messages.info(request, "Commencify Registration Rejected")
    return redirect('/admin_home/')

def fibroanalysis_reg(request):
    data=employee.objects.filter(department="Fibroanalysis")
    return render(request,'administrator/fibroanalysis_reg.html',{'data':data})

def accept(request, id):
    datas =employee.objects.get(id=id)
    p = random.randint(10000, 50000)
    datas.emp_id = f"F-{p}"
    print(p)
    datas.accept = True
    datas.decline = False
    datas.save()
    messages.info(request, "Fibroanalysis Approval Successful")
    return redirect('/admin_home/')

def decline(request, id):
    datas =employee.objects.get(id=id)
    datas.decline = True
    datas.accept = False
    datas.save()
    messages.info(request, "Fibroanalysis Registration Rejected")
    return redirect('/admin_home/')

def ecotoxify_reg(request):
    data=employee.objects.filter(department="Ecotoxify")
    return render(request,'administrator/ecotoxify_reg.html',{'data':data})

def admit(request, id):
    datas =employee.objects.get(id=id)
    p = random.randint(10000, 50000)
    datas.emp_id = f"E-{p}"
    print(p)
    datas.admit = True
    datas.deny = False
    datas.save()
    messages.info(request, "Ecotoxify Approval Successful")
    return redirect('/admin_home/')

def deny(request, id):
    datas =employee.objects.get(id=id)
    datas.deny = True
    datas.admit = False
    datas.save()
    messages.info(request, "AmplifyCraft Registration Rejected")
    return redirect('/admins_home/')


def commencify_result(request):
    data=requirement.objects.filter(cdone1=True)
    return render(request,"administrator/commencify_result.html",{'data':data})

def capprove(request, s_id):
    datas = requirement.objects.get(s_id=s_id)
    datas.capprove = True
    datas.creject = False
    datas.save()
    messages.info(request, f"{datas.s_id} Commencify Report Approved Successful")
    return redirect('/admin_home/')

def fibroanalysis_result(request):
    data=requirement.objects.filter(sdone4 = True)
    return render(request,"administrator/fibroanalysis_result.html",{'data':data})

def fibroanalysis_result_report(request, s_id):
    data = requirement.objects.get(s_id=s_id)
    title = "FIBROANALYSIS REPORTS"
    list_data = [
        f"S.ID: {data.s_id}",
        "----------------------------------------------------",
        "Fire Resistence\n"
        "----------------------------------------------------",

        f"Thickness: {data.thickness_inches}",
        f"Charring Rate: {data.charring_rate_inches_hour}",
        f"Critical Section Depth: {data.critical_section_depth_inches}",
        f"Fire Resistence: {data.fire_resistance_h}",
        f"Fire Resistence Level: {data.fire_resistance_level}",

        "----------------------------------------------------",
        "Thermal Insulation\n"
        "----------------------------------------------------",

        f"T1: {data.T1}",
        f"T2: {data.T2}",
        f"Thermal Conductivity Rate Difference: {data.rate_of_difference_in_thermal_conductivity}",
        f"Average Thermal Conductivity: {data.avg_thermal_conductivity}",
        f"Thermal Conductivity Level: {data.thermal_conductivity_level}",
        f"Thermal Insulation Level: {data.thermal_insulation_level}",

        "----------------------------------------------------",
        "Sound Absorption\n"
        "----------------------------------------------------",
        f"Reflection: {data.coefficient_of_reflection}",
        f"Transmission: {data.coefficient_of_transmission}",
        f"Sound Absorption: {data.sound_absorption}",
        f"Sound Absorption Level: {data.sound_absorption_level}",
    ]
    content = f"{title}\n\n" + '\n'.join(list_data)

    file_content = ContentFile(content.encode('utf-8'))
    data.f_report.save(f"{title}_{data.s_id}.txt", file_content)
    data.fview=True
    data.save()
    return redirect('/fibroanalysis_result/')

def fapprove(request, s_id):
    datas = requirement.objects.get(s_id=s_id)
    datas.fapprove = True
    datas.freject = False
    datas.save()
    messages.info(request, f"{datas.s_id} Fibroanalysis Report Approved Successful")
    return redirect('/admin_home/')

def ecotoxify_result(request):
    data=requirement.objects.filter(edone5 = True)
    return render(request,"administrator/ecotoxify_result.html",{'data':data})

def eapprove(request, s_id):
    datas = requirement.objects.get(s_id=s_id)
    datas.eapprove = True
    datas.ereject = False
    datas.save()
    messages.info(request, f"{datas.s_id} Fibroanalysis Report Approved Successful")
    return redirect('/admin_home/')


def valid_report(request):
    data=requirement.objects.filter(eapprove = True)
    return render(request,"administrator/valid_report.html",{'data':data})


def view_final_report(request, s_id):
    data = requirement.objects.get(s_id=s_id)

    title = "CHEMICAL PRINTS REPORTS"
    list_data = [
        f"S.ID: {data.s_id}",
        "----------------------------------------------------",
        "Origination(Commencify)\n"
        "----------------------------------------------------",
        f"Tree Species: {data.tree_species}",
        f"Tree Origin: {data.tree_origin}",
        f"Tree Age : {data.age}",
        f"Tree Wood Property: {data.wood_property}",
        f"Tree Density: {data.density}",
        f"Tree Hardness: {data.hardness}",
        f"Tree Grain Pattern: {data.grain_pattern}",
        f"Tree Durability: {data.durability}",
        f"Tree Eco-Toxicology: {data.eco_toxicology}",
        f"Tree Eco-Toxicity: {data.eco_toxicity}",
        f"Tree Eco-Sustainability: {data.eco_sustainability}",

        "----------------------------------------------------",
        "Fire Resistence\n"
        "----------------------------------------------------",

        f"Thickness: {data.thickness_inches}",
        f"Charring Rate: {data.charring_rate_inches_hour}",
        f"Critical Section Depth: {data.critical_section_depth_inches}",
        f"Fire Resistence: {data.fire_resistance_h}",
        f"Fire Resistence Level: {data.fire_resistance_level}",

        "----------------------------------------------------",
        "Thermal Insulation\n"
        "----------------------------------------------------",

        f"T1: {data.T1}",
        f"T2: {data.T2}",
        f"Thermal Conductivity Rate Difference: {data.rate_of_difference_in_thermal_conductivity}",
        f"Average Thermal Conductivity: {data.avg_thermal_conductivity}",
        f"Thermal Conductivity Level: {data.thermal_conductivity_level}",
        f"Thermal Insulation Level: {data.thermal_insulation_level}",

        "----------------------------------------------------",
        "Sound Absorption\n"
        "----------------------------------------------------",
        f"Reflection: {data.coefficient_of_reflection}",
        f"Transmission: {data.coefficient_of_transmission}",
        f"Sound Absorption: {data.sound_absorption}",
        f"Sound Absorption Level: {data.sound_absorption_level}",

        "----------------------------------------------------",
        "Eco Toxicity\n"
        "----------------------------------------------------",
        f"Reflection: {data.ecotoxicity}",
        f"Acute Toxicity[Humans]: {data.acute_toxicity_humans}",
        f"Acute Toxicity[Wildlife]: {data.acute_toxicity_wildlife}",
        f"Chronic Toxicity[Humans] : {data.chronic_toxicity_humans}",
        f"Chronic Toxicity[Wildlife]: {data.chronic_toxicity_wildlife}",

    ]
    content = f"{title}\n\n" + '\n'.join(list_data)

    file_content = ContentFile(content.encode('utf-8'))
    data.cp_final_report.save(f"{title}_{data.s_id}.txt", file_content)
    data.finalreportview = True
    data.save()
    messages.info(request,"Report Generated Successfully")
    return redirect('/valid_report/')



def finalreportapprove(request, s_id):
    datas = requirement.objects.get(s_id=s_id)
    data=registration.objects.get(s_id=s_id)
    data.final=True
    datas.finalreportapprove = True
    datas.finalreportreject = False
    data.save()
    datas.save()
    messages.info(request, f"{datas.s_id} Chemical Print Report Approved Successful")
    return redirect('/admin_home/')