from django.contrib import messages
from django.shortcuts import render,redirect
from commencify.models import employee
from scientist.models import requirement, registration


def ecotoxify_RL(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        department=request.POST['department']
        password=request.POST['password']
        employee(name=name, email=email,phone=phone, department=department,password=password).save()
        messages.info(request,f"{name} Registration Successful")
        return render(request, "ecotoxify/ecotoxify_RL.html")
    return render(request,"ecotoxify/ecotoxify_RL.html")

def ecotoxify_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            s = employee.objects.get(email=email, password=password)
            if s.admit:
                messages.info(request, "Ecotoxify Login Successful")
                request.session['user_id'] = s.emp_id
                print( request.session['user_id'])
                return redirect("/ecotoxify_home/")
            else:
                messages.info(request, "You need Management Approval to Access")
                return render(request, "ecotoxify/ecotoxify_RL.html")

        except employee.DoesNotExist:
            messages.info(request, "Invalid Email or Password")
    return render(request, "ecotoxify/ecotoxify_RL.html")

def ecotoxify_logout(request):
    if 'user_id' in request.session:
        request.session.pop('user_id',None)
        messages.success(request,'Logout successful')
        return redirect('/')
    else:
        messages.success(request, 'Logout successful')
        return redirect('/')

def ecotoxify_home(request):
    return render(request,"ecotoxify/ecotoxify_home.html")

def f_report(request):
    data=requirement.objects.filter(fapprove = True)
    return render(request,"ecotoxify/f_report.html",{'data':data})

def process_ecotoxify(request):
    data=requirement.objects.filter(fapprove = True)
    return render(request,"ecotoxify/process_ecotoxify.html",{'data':data})



import pandas as pd
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

def analysis_ecotoxify(request, s_id):
    con = requirement.objects.get(s_id=s_id)
    fire_resistance_h = con.fire_resistance_h
    thermal_conductivity = con.thermal_conductivity
    sound_absorption = con.sound_absorption

    dataset = pd.read_csv('E:\Project\ML - Chemical Prints\Chemical_Prints\Ecotoxify.csv')

    X = dataset[['fire_resistance_h', 'thermal_conductivity', 'sound_absorption']]
    y = dataset['ecotoxicity']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    base_regressor = DecisionTreeRegressor()
    bagging_regressor = BaggingRegressor(base_regressor, n_estimators=100, random_state=42)
    bagging_regressor.fit(X_train, y_train)

    input_data = pd.DataFrame([[fire_resistance_h, thermal_conductivity, sound_absorption]],
                              columns=['fire_resistance_h', 'thermal_conductivity', 'sound_absorption'])

    predictions = bagging_regressor.predict(input_data)

    print(predictions)



    data = requirement.objects.get(s_id=s_id)
    csv_path = r'E:\Project\ML - Chemical Prints\Chemical_Prints\Ecotoxify Acute and Chronic Dataset.csv'
    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        if (data.tree_species, data.tree_origin) == (row['tree_species'], row['tree_origin']):
            data.acute_toxicity_humans = row['acute_toxicity_humans']
            data.acute_toxicity_wildlife = row['acute_toxicity_wildlife']
            data.chronic_toxicity_humans = row['chronic_toxicity_humans']
            data.chronic_toxicity_wildlife = row['chronic_toxicity_wildlife']
            data.save()

    data.ecotoxicity = predictions
    data.save()

    d = registration.objects.get(s_id=s_id)
    d.edone = True
    d.status = "Waiting"
    d.save()
    data1 = requirement.objects.get(s_id=s_id)
    data1.edone5 = True
    data1.save()

    messages.info(request,f"Eco Toxicity Calculated Successfully for {s_id}")
    return redirect("/ecotoxify_home/")



def ecotoxify_report(request):
    data=requirement.objects.filter(edone5 = True)
    return render(request,"ecotoxify/ecotoxify_report.html",{'data':data})