from io import BytesIO
from django.contrib import messages
from django.core.files.base import ContentFile
from django.shortcuts import render,redirect
from commencify.models import employee
from scientist.models import requirement, registration


def fibroanalysis_RL(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        department=request.POST['department']
        password=request.POST['password']
        employee(name=name, email=email,phone=phone, department=department,password=password).save()
        messages.info(request,f"{name} Registration Successful")
        return render(request, "fibroanalysis/fibroanalysis_RL.html")
    return render(request,"fibroanalysis/fibroanalysis_RL.html")

def fibroanalysis_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            s = employee.objects.get(email=email, password=password)

            if s.accept:
                messages.info(request, "Fibroanalysis Login Successful")

                request.session['user_id'] = s.emp_id
                print( request.session['user_id'])
                return redirect("/fibroanalysis_home/")
            else:
                messages.info(request, "You need Management Approval to Access")
                return render(request, "fibroanalysis/fibroanalysis_RL.html")

        except employee.DoesNotExist:
            messages.info(request, "Invalid Email or Password")

    return render(request, "fibroanalysis/fibroanalysis_RL.html")

def fibroanalysis_logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id',None)
        messages.success(request,'Logout successful')
        return redirect('/')
    else:
        messages.success(request, 'Logout successful')
        return redirect('/')

def fibroanalysis_home(request):
    return render(request,"fibroanalysis/fibroanalysis_home.html")

def c_report(request):
    data=requirement.objects.filter(capprove=True)
    return render(request,"fibroanalysis/c_report.html",{'data':data})

#Fire Analysis
def fire_res_analysis(request):
    data=requirement.objects.filter(capprove=True)
    return render(request,"fibroanalysis/fire_res_analysis.html",{'data':data})


def f_fireresistence(request, s_id):
    data = requirement.objects.filter(s_id=s_id)
    csv_path = r'E:\Project\ML - Chemical Prints\Chemical_Prints\Fire Resistence.csv'
    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        for i in data:
            if (i.tree_species, i.tree_origin) == (row['tree_species'], row['tree_origin']):
                i.thickness_inches = row['thickness_inches']
                i.charring_rate_inches_hour = row['charring_rate_inches_hour']

                k = i.thickness_inches / (i.thickness_inches * i.charring_rate_inches_hour)
                i.critical_section_depth_inches = k

                l = i.thickness_inches / i.charring_rate_inches_hour
                i.fire_resistance_h = l

                if 1 <= i.thickness_inches <= 1.5:
                    i.fire_resistance_level = "High"
                else:
                    i.fire_resistance_level = "Low"

                i.save()

                # Plotting
                plt.plot(['Thickness', 'Charring_Rate', 'Critical_Section', 'Fire_Resistence'],
                         [i.thickness_inches, i.charring_rate_inches_hour, i.critical_section_depth_inches,
                          i.fire_resistance_h],
                         marker='o', linestyle='--', color='g')

                plt.title('Fire Resistence Analysis')
                plt.xlabel('Parameters')
                plt.ylabel('Values')

                for j, txt in enumerate([i.thickness_inches, i.charring_rate_inches_hour,
                                          i.critical_section_depth_inches, i.fire_resistance_h]):
                    plt.annotate(f'{txt:.2f}', (j, txt), textcoords="offset points", xytext=(0, 10), ha='center')

                # Saving the plot
                buffer = BytesIO()
                plt.savefig(buffer, format='png')
                i.fire_resistance_plot.save('fire_resistance_plot.png', ContentFile(buffer.getvalue()))
                i.save()


    d=registration.objects.get(s_id=s_id)
    d.fdone=True
    d.save()
    data1 = requirement.objects.get(s_id=s_id)
    data1.fdone2=True
    data1.save()

    messages.info(request, f"{s_id} Fire Resistence Analysis Processed Successfully!")
    return render(request, 'fibroanalysis/fire_res_analysis.html')


def fire_res_analysis_report(request):
    data=requirement.objects.filter(fdone2=True)
    return render(request,"fibroanalysis/fire_res_analysis_report.html",{'data':data})




#Thermal Insulation
def thermal_insulation_res_analysis(request):
    data=requirement.objects.filter(capprove=True)
    return render(request,"fibroanalysis/thermal_insulation_res_analysis.html",{'data':data})


import pandas as pd
from django.core.files.base import ContentFile
from django.shortcuts import render
from django.contrib import messages

def f_thermalinsulation(request, s_id):
    data = requirement.objects.filter(s_id=s_id)
    csv_path = r'E:\Project\ML - Chemical Prints\Chemical_Prints\Thermal Insulation.csv'
    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        for i in data:
            if (i.tree_species, i.tree_origin) == (row['tree_species'], row['tree_origin']):
                i.T1 = row['T1']
                i.T2 = row['T2']
                i.rate_of_difference_in_thermal_conductivity = row['rate_of_difference_in_thermal_conductivity']
                i.avg_thermal_conductivity = row['avg_thermal_conductivity']

                k = i.avg_thermal_conductivity - i.rate_of_difference_in_thermal_conductivity * (i.T1 + i.T2) / 2
                l = abs(k)
                i.thermal_conductivity = l

                if 0.01 <= i.thermal_conductivity <= 0.05:
                    i.thermal_conductivity_level = "Low"
                elif 0.06 <= i.thermal_conductivity <= 0.15:
                    i.thermal_conductivity_level = "Medium"
                else:
                    i.thermal_conductivity_level = "High"
                i.save()

                if i.thermal_conductivity_level == "Low":
                    i.thermal_insulation_level = "High"
                elif i.thermal_conductivity_level == "Medium":
                    i.thermal_insulation_level = "Medium"
                elif i.thermal_conductivity_level == "High":
                    i.thermal_insulation_level = "Low"
                i.save()


                plt.plot(['T1', 'T2', 'Rate_of_Difference', 'Average_TC', 'Thermal Conductivity'],
                         [i.T1, i.T2, i.rate_of_difference_in_thermal_conductivity,
                          i.avg_thermal_conductivity, i.thermal_conductivity],
                         marker='o', linestyle='--', color='b')

                plt.title('Thermal Insulation Analysis')
                plt.xlabel('Parameters')
                plt.ylabel('Values')

                for j, txt in enumerate([i.T1, i.T2, i.rate_of_difference_in_thermal_conductivity,
                                         i.avg_thermal_conductivity, i.thermal_conductivity]):
                    plt.annotate(f'{txt:.2f}', (j, txt), textcoords="offset points", xytext=(0, 10), ha='center')

                buffer = BytesIO()
                plt.savefig(buffer, format='png')
                i.thermal_insulation_plot.save('thermal_insulation_plot.png', ContentFile(buffer.getvalue()))
                i.save()

    d = registration.objects.get(s_id=s_id)
    d.tdone = True
    d.save()
    data1 = requirement.objects.get(s_id=s_id)
    data1.tdone3 = True
    data1.save()
    messages.info(request, f"{s_id}Thermal Insulation Analysis Processed Successfully!")
    return render(request, 'fibroanalysis/thermal_insulation_res_analysis.html')


def thermal_insulation_analysis_report(request):
    data=requirement.objects.filter(tdone3 = True)
    return render(request,"fibroanalysis/thermal_insulation_analysis_report.html",{'data':data})



#Sound Absorption
def sound_absorption_res_analysis(request):
    data=requirement.objects.filter(capprove=True)
    return render(request,"fibroanalysis/sound_absorption_res_analysis.html",{'data':data})


from io import BytesIO
import matplotlib.pyplot as plt

def f_soundabsorption(request, s_id):
    data = requirement.objects.filter(s_id=s_id)
    csv_path = r'E:\Project\ML - Chemical Prints\Chemical_Prints\Sound Absorption.csv'
    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        for i in data:
            if (i.tree_species, i.tree_origin) == (row['tree_species'], row['tree_origin']):
                i.coefficient_of_reflection = row['coefficient_of_reflection']
                i.coefficient_of_transmission = row['coefficient_of_transmission']

                k = 1 - i.coefficient_of_reflection - i.coefficient_of_transmission
                l = abs(k)
                i.sound_absorption = l

                if i.sound_absorption < 0.5:
                    i.sound_absorption_level = "Less Effective"
                elif i.sound_absorption >= 0.5:
                    i.sound_absorption_level = "Effective"
                i.save()

                plt.plot(['Coefficient of Reflection', 'Coefficient of Transmission', 'Sound Absorption'],
                         [i.coefficient_of_reflection, i.coefficient_of_transmission, i.sound_absorption],
                         marker='o', linestyle='--', color='r')
                plt.title('Sound Absorption Analysis')
                plt.xlabel('Parameters')
                plt.ylabel('Values')

                for j, txt in enumerate([i.coefficient_of_reflection, i.coefficient_of_transmission, i.sound_absorption]):
                    plt.annotate(f'{txt:.2f}', (j, txt), textcoords="offset points", xytext=(0, 10), ha='center')

                buffer = BytesIO()
                plt.savefig(buffer, format='png')


                i.sound_absorption_plot.save('sound_absorption_plot.png', ContentFile(buffer.getvalue()))
                i.save()

    d = registration.objects.get(s_id=s_id)
    d.sdone = True
    d.save()
    data1 = requirement.objects.get(s_id=s_id)
    data1.sdone4 = True
    data1.save()
    messages.info(request, f"{s_id} Sound Absorption Analysis Processed Successfully!")
    return render(request, 'fibroanalysis/sound_absorption_res_analysis.html')


def sound_absorption_analysis_report(request):
    data=requirement.objects.filter(sdone4 = True)
    return render(request,"fibroanalysis/sound_absorption_analysis_report.html",{'data':data})

