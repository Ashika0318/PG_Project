from django.db import models

# Create your models here.
class registration(models.Model):
    name=models.CharField(max_length=50)
    phone = models.PositiveBigIntegerField()
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    status = models.CharField(max_length=50,null=True,default="Pending")

    approve = models.BooleanField(null=True, default=False)
    reject = models.BooleanField(null=True, default=False)
    s_id = models.CharField(null=True, max_length=50)
    cdone=models.BooleanField(null=True, default=False)
    upload=models.BooleanField(null=True, default=False)

    fdone =models.BooleanField(null=True, default=False)
    tdone = models.BooleanField(null=True, default=False)
    sdone = models.BooleanField(null=True, default=False)
    edone=models.BooleanField(null=True, default=False)
    final=models.BooleanField(null=True, default=False)

    login = models.BooleanField(null=True, default=False)
    logout = models.BooleanField(null=True, default=False)



class requirement(models.Model):
    s_id = models.CharField(null=True, max_length=50)
    tree_species=models.CharField(max_length=50)
    tree_origin = models.CharField(max_length=50)
    wood_color=models.CharField(max_length=50)
    wood_grain_pattern=models.CharField(max_length=50)

    #Commencify
    age= models.PositiveBigIntegerField(null=True)
    wood_property = models.CharField(null=True, max_length=50)
    density= models.FloatField(null=True)
    hardness= models.PositiveBigIntegerField(null=True)
    grain_pattern= models.CharField(null=True, max_length=50)
    durability= models.FloatField(null=True)
    eco_toxicology= models.CharField(null=True, max_length=50)
    eco_toxicity= models.FloatField(null=True)
    eco_sustainability= models.CharField(null=True, max_length=50)

    cdone1 = models.BooleanField(null=True, default=False)
    fdone2 = models.BooleanField(null=True, default=False)
    tdone3 = models.BooleanField(null=True, default=False)
    sdone4 = models.BooleanField(null=True, default=False)
    edone5 = models.BooleanField(null=True, default=False)

    capprove = models.BooleanField(null=True, default=False)
    creject = models.BooleanField(null=True, default=False)

    fview= models.BooleanField(null=True, default=False)
    fapprove = models.BooleanField(null=True, default=False)
    freject = models.BooleanField(null=True, default=False)

    eapprove = models.BooleanField(null=True, default=False)
    ereject = models.BooleanField(null=True, default=False)

    finalreportview= models.BooleanField(null=True, default=False)

    finalreportapprove = models.BooleanField(null=True, default=False)
    finalreportreject = models.BooleanField(null=True, default=False)


    #Fire Resistence
    thickness_inches = models.FloatField(null=True)
    charring_rate_inches_hour = models.FloatField(null=True)
    critical_section_depth_inches =models.FloatField(null=True)
    fire_resistance_h = models.FloatField(null=True)
    fire_resistance_level = models.CharField(null=True, max_length=50)
    fire_resistance_plot = models.ImageField(upload_to='Fire_Resistence/', null=True)

    #Thermal Insulation
    T1 = models.FloatField(null=True)
    T2= models.FloatField(null=True)
    rate_of_difference_in_thermal_conductivity= models.FloatField(null=True)
    avg_thermal_conductivity= models.FloatField(null=True)
    thermal_conductivity=models.FloatField(null=True)
    thermal_conductivity_level=models.CharField(null=True, max_length=50)
    thermal_insulation_level = models.CharField(null=True, max_length=50)
    thermal_insulation_plot = models.ImageField(upload_to='Thermal_Insulation/', null=True)

    #Sound Absorption
    coefficient_of_reflection= models.FloatField(null=True)
    coefficient_of_transmission= models.FloatField(null=True)
    sound_absorption= models.FloatField(null=True)
    sound_absorption_level=models.CharField(null=True, max_length=50)
    sound_absorption_plot = models.ImageField(upload_to='Sound_Absorption/', null=True)

    #Fibroanalysis Result
    f_report=models.FileField(upload_to='Fibroanalysis_Report/', null=True)

    #Eco-Toxicify
    ecotoxicity= models.FloatField(null=True)
    acute_toxicity_humans=models.CharField(null=True, max_length=50)
    acute_toxicity_wildlife=models.CharField(null=True, max_length=50)
    chronic_toxicity_humans=models.CharField(null=True, max_length=50)
    chronic_toxicity_wildlife=models.CharField(null=True, max_length=50)

    # CP FINAL Result
    cp_final_report = models.FileField(upload_to='ChePrint_Final_Report/', null=True)
