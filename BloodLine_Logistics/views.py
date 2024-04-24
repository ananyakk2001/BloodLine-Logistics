import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from BloodLine_Logistics.models import*


def logout(request):
    request.session['log']=""
    request.session.clear()

    return HttpResponse("<script>alert('Logout Successfully');window.location='/'</script>")

def log(request):
    feed=Feedback.objects.all()
    data=[]
    cnt=0
    for i in feed:
        print(i.LOGIN)
        if cnt<3:
            if i.LOGIN.usertype == "donor":
                don_obj=Donor.objects.get(LOGIN=i.LOGIN)
                data.append({'name':don_obj.name, 'type':"Donor", 'feed':i.feedback, 'date':i.date})
            elif i.LOGIN.usertype == "seeker":
                seek_obj = Seeker.objects.get(LOGIN=i.LOGIN)
                data.append({'name': seek_obj.name, 'type': "Seeker", 'feed': i.feedback, 'date':i.date})
            cnt=cnt+1

    print(data)

    bld=Blood_bank.objects.all()
    return render(request,"newindex.html",{'data': data, 'len':len(data), 'data2':bld})
def blood(request):
    if request.session['log']!="lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    bld=Blood_bank.objects.all()
    return render(request,"newindex.html",{'data':bld})


def donorverify(request):
    if request.session['log']!="lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    dnr = Donor.objects.filter(LOGIN__usertype='pending')
    request.session['head'] = "Verify Donor"
    return render(request,"ADMIN/VIEW_DONOR_AND_VERIFY.html", {'data': dnr})
def accept_donor(request, id,em):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    Login.objects.filter(id=id).update(usertype='donor')
    print(em, "maillllll")
    import smtplib

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("bloodlinelogistics1@gmail.com", "vsgc pqcm pmfx gpca")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "bloodlinelogistics1@gmail.com"
    msg['To'] = em
    msg['Subject'] = "Account verification"
    body = "Your Request Approved "
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)

    return HttpResponse("<script>alert('Verified');window.location='/donorverify'</script>")

def reject_donor(request, id,em):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    Login.objects.filter(id=id).delete()
    print(em, "maillllll")
    import smtplib

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("bloodlinelogistics1@gmail.com", "vsgc pqcm pmfx gpca")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "bloodlinelogistics1@gmail.com"
    msg['To'] = em
    msg['Subject'] = "Account verification"
    body = "Your Request Rejected!! "
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    return HttpResponse("<script>alert('Deleted');window.location='/donorverify'</script>")

def seekerverify(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    skr=Seeker.objects.filter(LOGIN__usertype='pending')
    request.session['head'] = "Verified Seekers"
    return render(request,"ADMIN/VIEW_SEEKER_AND_VERIFY.html",{'data':skr})

def accept_seeker(request,id,em):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    Login.objects.filter(id=id).update(usertype='seeker')
    print(em, "maillllll")
    import smtplib

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("bloodlinelogistics1@gmail.com", "vsgc pqcm pmfx gpca")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "bloodlinelogistics1@gmail.com"
    msg['To'] = em
    msg['Subject'] = "Account verification"
    body = "Your Request Approved "
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    return HttpResponse("<script>alert('Verified');window.location='/seekerverify'</script>")

def reject_seeker(request,id,em):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    Login.objects.filter(id=id).delete()
    print(em, "maillllll")
    import smtplib

    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("bloodlinelogistics1@gmail.com", "vsgc pqcm pmfx gpca")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "bloodlinelogistics1@gmail.com"
    msg['To'] = em
    msg['Subject'] = "Account verification"
    body = "Your Request Rejected "
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    return HttpResponse("<script>alert('Deleted');window.location='/seekerverify'</script>")

def verifieddonor(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    dnr = Donor.objects.filter(LOGIN__usertype='donor')
    request.session['head'] = "Verified Donors"
    return render(request,"ADMIN/VERIFIED_DONORS.html", {'data': dnr})

def verifiedseeker(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/seekerverify'</script>")
    skr=Seeker.objects.filter(LOGIN__usertype='seeker')
    request.session['head'] = "Verified Seekers"
    return render(request,"ADMIN/VERIFIED_SEEKERS.html",{'data': skr})

def viewrequest(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    request.session['head'] = "Request"
    req=Request.objects.filter(~Q(status='Completed'), ~Q(status='Approved'),  date__gte=datetime.datetime.now().strftime("%Y-%m-%d"))

    return render(request, "ADMIN/VIEW_BLOOD_REQUEST.html",{'data': req})

def view_approved_request(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    request.session['head'] = "View Approved Request"
    approve=Request.objects.filter(status='Approved')
    return render(request, "ADMIN/VIEW_APPROVED_REQUEST.html", {'data': approve})

def complete_request(request,id):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    req=Request.objects.get(id=id)
    qty=req.quantity
    bld_id=req.BLOOD_ID_id
    req.status='Completed'
    req.save()
    obj=Blood_bank.objects.get(BLOOD_ID_id=bld_id)
    old_stock=obj.stock
    obj.stock=float(old_stock)-float(qty)
    obj.save()
    return HttpResponse("<script>alert('Completed');window.location='/viewrequest'</script>")

def willing_donor(request, id):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    willing=Request_allocation.objects.filter(REQUEST_id=id)
    return render(request,"ADMIN/VIEW_WILLING_DONORS.html",{'data':willing})

def verifyrequest(request, id,bid):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    print(bid)
    qry=Blood_bank.objects.filter(BLOOD_ID=bid)
    print(qry)
    if qry.exists():

        res=Request.objects.get(id=id)
        res.status='Approved'
        res.save()
        return HttpResponse("<script>alert('Approved');window.location='/viewrequest'</script>")
    return HttpResponse("<script>alert('Currently not Available!!');window.location='/viewrequest'</script>")


def reqproceed(request,id):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")

    res =Request.objects.get(id=id)
    # for i in res:
    r=Donor.objects.filter(BLOOD_ID_id=res.BLOOD_ID.id)
    if r.exists():

        for j in r:
            print(j.email,"maillllll")
            import smtplib

            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.starttls()
            s.login("bloodlinelogistics1@gmail.com", "vsgc pqcm pmfx gpca")
            msg = MIMEMultipart()  # create a message.........."
            msg['From'] = "bloodlinelogistics1@gmail.com"
            msg['To'] = j.email
            msg['Subject'] = "Blood Needed!!"
            body = "Are you willing to donate Blood? "
            msg.attach(MIMEText(body, 'plain'))
            s.send_message(msg)

        Request.objects.filter(id=id).update(status='Needed')
        return HttpResponse("<script>alert('Needed');window.location='/viewrequest'</script>")
    else:
        return HttpResponse("<script>alert('No Donors!!');window.location='/viewrequest'</script>")


# def reqproceed(request,id):
#     if request.session['log'] != "lo":
#         return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
#
#     res =Request.objects.filter(id=id)
#     for i in res:
#         r=Donor.objects.filter(BLOOD_ID_id=i.BLOOD_ID.id)
#         if r.DoesNotExist():
#             return HttpResponse("<script>alert('No Donors!!');window.location='/viewrequest'</script>")
#
#         for j in r:
#             print(j.email,"maillllll")
#             import smtplib
#
#             s = smtplib.SMTP(host='smtp.gmail.com', port=587)
#             s.starttls()
#             s.login("bloodlinelogistics1@gmail.com", "vsgc pqcm pmfx gpca")
#             msg = MIMEMultipart()  # create a message.........."
#             msg['From'] = "bloodlinelogistics1@gmail.com"
#             msg['To'] = j.email
#             msg['Subject'] = "Blood Needed!!"
#             body = "Are you willing to donate Blood? "
#             msg.attach(MIMEText(body, 'plain'))
#             s.send_message(msg)
#
#     Request.objects.filter(id=id).update(status='Needed')
#     return HttpResponse("<script>alert('Needed');window.location='/viewrequest'</script>")

def donorhistory(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    dh=Request_allocation.objects.filter(status='Completed')
    return render(request, "ADMIN/DONOR_HISTORY.html",{'data':dh} )

def viewhistory(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    # reqh=Request.objects.filter(date__lt=datetime.datetime.now().strftime("%Y-%m-%d"))
    reqh = Request.objects.filter(status="Completed")
    print(reqh)
    request.session['head'] = "Donation History"
    return render(request,"ADMIN/VIEW_BLOOD_HISTORY.html",{'data':reqh})

def login_post(request):
    unm=request.POST['textfield']
    psw=request.POST['textfield2']
    res = Login.objects.filter(username=unm, password=psw)
    if res.exists():
        request.session['lid']=res[0].id
        request.session['head']=""
        request.session['log']="lo"
        if res[0].usertype == 'admin':
            return  redirect('/admin_login')
        elif res[0].usertype=='donor':
            return redirect('/donor_index')
        elif res[0].usertype=='seeker':
            return redirect('/Seeker_Home')
        else:
            return HttpResponse("<script>alert('Not Allowed');window.location='/'</script>")
    else:
        return HttpResponse("<script>alert('Invalid Username/Password');window.location='/'</script>")

def admin_login(request):
    # qry=Donor.objects.filter(LOGIN__usertype="pending")
    # dc=len(qry)
    # print("donor_count : ",dc)
    # qry1=Seeker.objects.filter(LOGIN__usertype="pending")
    # sc=len(qry1)
    # print("seeker count :",sc)
    return render(request,"ADMIN/newindex.html")

def add_blood(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    request.session['head'] = "Add Blood"
    return render(request,"ADMIN/add blood.html")

def add_blood_post(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    bloodgroup=request.POST['blood']
    qry=Blood.objects.filter(blood_name=bloodgroup)
    if qry.exists():
        return HttpResponse("<script>alert('Already Added!!');window.location='/add_blood'</script>")

    obj = Blood()
    obj.blood_name=bloodgroup
    obj.save()
    return HttpResponse("<script>alert('Added successfully');window.location='/add_blood'</script>")

def view_blood(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    request.session['head'] = "View Blood"

    vblood=Blood.objects.all()
    data=[]
    for i in vblood:
        qry=Blood_bank.objects.filter(BLOOD_ID=i.id)
        if qry.exists():
            data.append(
                {
                    "id":i.id,
                    "blood_name":i.blood_name,
                    "stock":qry[0].stock
                }
            )
        else:
            data.append(
                {
                    "id": i.id,
                    "blood_name": i.blood_name,
                    "stock": "No stock!"
                }
            )

    return render(request,"ADMIN/VIEW_BLOOD.html",{'data':data})

def delete_blood(request,id):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    Blood.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Deleted');window.location='/view_blood'</script>")

def blood_stock(request, id):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    return render(request,"ADMIN/add_stock.html", {'id':id})

def blood_stock_POST(request, id):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    Stock=request.POST['stock']
    res=Blood_bank.objects.filter(BLOOD_ID_id=id)
    if res.exists():
        res=res[0]
        res.stock=float(Stock)+float(res.stock)
        res.save()
    else:
        obj=Blood_bank()
        obj.BLOOD_ID_id=id
        obj.stock=Stock
        obj.save()
    return HttpResponse("<script>alert('Stock updated');window.location='/view_blood'</script>")




#############################################################################

def view_Donor_Home(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    return render(request,"DONOR/Donor_Home.html")

def donor_index(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    return render(request,"DONOR/donor_index.html")


def view_Donor_Profile(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    request.session['head']="Profile"
    Profile=Donor.objects.get(LOGIN_id=request.session['lid'])
    res=Blood.objects.all()
    print(Profile)
    return render(request,"DONOR/VIEW_PROF_UPDATE.html",{'data':Profile,"data1":res})

def donor_update_profile_post(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    name=request.POST['textfield']
    email=request.POST['textfield2']
    Phone=request.POST['textfield3']
    BLOOD_GROUP=request.POST['select']
    House=request.POST['textfield4']
    Pin=request.POST['textfield5']
    Post=request.POST['textfield6']
    age=request.POST['textfield7']
    Gender=request.POST['radio']
    Donor.objects.filter(LOGIN_id=request.session['lid']).update(name=name, email=email,phone=Phone,house=House,pin=Pin,post=Post,age=age,gender=Gender,BLOOD_ID=BLOOD_GROUP)
    return HttpResponse("<script>alert('Profile updated');window.location='/view_Donor_Profile'</script>")

def donor_request(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    request.session['head']="Blood Request"


    r=Donor.objects.get(LOGIN=request.session['lid'])
    bld=r.BLOOD_ID
    # print(bld,"blooodd")
    req = Request.objects.filter(status='Needed',BLOOD_ID=bld)
    return render(request,"DONOR/VIEW_BLOOD_REQUEST.html",{'data':req})

def donor_willingness(request, id):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    res=Request_allocation.objects.filter(REQUEST_id=id, DONOR=Donor.objects.get(LOGIN_id=request.session['lid']))
    if res.exists():
        return HttpResponse("<script>alert('Already responded');window.location='/donor_request'</script>")
    else:
        Request.objects.filter(id=id).update(status="willing")
        obj=Request_allocation()
        obj.DONOR=Donor.objects.get(LOGIN_id=request.session['lid'])
        obj.REQUEST_id=id
        obj.status="Willing"
        obj.save()
        return HttpResponse("<script>alert('Willingness sent');window.location='/donor_request'</script>")

def donor_accept_req(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    res=Request_allocation.objects.filter(DONOR=Donor.objects.get(LOGIN_id=request.session['lid']), status="Willing")
    return render(request,"DONOR/ACCEPTED_REQUEST.html",{'data':res})

def donor_feedback(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    request.session['head'] = "Feedback"
    return render(request,"DONOR/FEEDBACK.html")

def donor_feedback_POST(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    feed=request.POST['textarea']
    date=datetime.datetime.now().strftime("%d-%m-%Y")
    obj=Feedback()
    obj.date=date
    obj.feedback=feed
    obj.LOGIN_id=request.session['lid']
    obj.save()
    return HttpResponse("<script>alert('Sent');window.location='/donor_feedback'</script>")




def seeker_reg(request):
    res=Blood.objects.all()
    return render(request, "seeker_reg.html", {'data':res})

def seeker_reg_post(request):
    name=request.POST['name']
    email=request.POST['email']
    Phone_number=request.POST['phone']
    Password=request.POST['password']
    # age=request.POST['age']
    Gender=request.POST['radio']
    Blood_Group=request.POST['select']
    res=Login.objects.filter(username=email)
    if res.exists():
        return HttpResponse("<script>alert('Email already exist');window.location='/seeker_reg'</script>")
    log = Login()
    log.username = email
    log.password= Password
    log.usertype="pending"
    log.save()
    obj=Seeker()
    obj.name=name
    obj.email=email
    obj.phone=Phone_number
    # obj.age=age
    obj.gender=Gender
    obj.BLOOD_ID_id=Blood_Group
    obj.LOGIN=log
    obj.save()
    return HttpResponse("<script>alert('Registered Successfully');window.location='/'</script>")

def donor_reg(request):
    res=Blood.objects.all()
    return render(request, "donor_reg.html", {'data':res})
def donor_reg_post(request):
    name=request.POST['name']
    email=request.POST['email']
    Phone_number=request.POST['phone']
    Password=request.POST['password']
    age=request.POST['age']
    Gender=request.POST['radio']
    Blood_Group=request.POST['select']
    house=request.POST['house']
    pin=request.POST['pin']
    post=request.POST['post']
    res = Login.objects.filter(username=email)
    if res.exists():
        return HttpResponse("<script>alert('Email already exist');window.location='/donor_reg'</script>")
    log = Login()
    log.username = email
    log.password= Password
    log.usertype="pending"
    log.save()
    obj=Donor()
    obj.name=name
    obj.email=email
    obj.phone=Phone_number
    obj.age=age
    obj.gender=Gender
    obj.BLOOD_ID_id=Blood_Group
    obj.house=house
    obj.pin=pin
    obj.post=post
    obj.LOGIN=log
    obj.save()
    return HttpResponse("<script>alert('Registered Successfully');window.location='/'</script>")




#######################################             SEEKER

def Seeker_Home(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    return render(request,"SEEKER/newindex.html")


def view_Seeker_Profile(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    request.session['head'] = "Profile"
    Profile=Seeker.objects.get(LOGIN_id=request.session['lid'])
    res=Blood.objects.all()
    print(Profile)
    return render(request,"SEEKER/Update_seeker.html",{'data':Profile,"data1":res})

def view_Seeker_Profile_POST(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    name=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['textfield3']
    BLOOD_ID=request.POST['select']
    gender=request.POST['radio']
    Seeker.objects.filter(LOGIN_id=request.session['lid']).update(name=name, email=email, phone=phone, gender=gender,BLOOD_ID_id=BLOOD_ID)
    return HttpResponse("<script>alert('Profile updated');window.location='/view_Seeker_Profile'</script>")

def seeker_feedback(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    request.session['head'] = "Feedback"
    return render(request,"SEEKER/SFEEDBACK.html")

def seeker_feedback_POST(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/donorverify'</script>")
    feed=request.POST['textarea']
    date=datetime.datetime.now().strftime("%d-%m-%Y")
    obj=Feedback()
    obj.date=date
    obj.feedback=feed
    obj.LOGIN_id=request.session['lid']
    obj.save()
    return HttpResponse("<script>alert('Sent');window.location='/seeker_feedback'</script>")

def seeker_view_blood(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/seekerverify'</script>")
    request.session['head'] = "New Request"
    bld_v= Blood.objects.all()
    return render(request,"SEEKER/S_VIEW_BLOOD.html",{'data':bld_v})

def blood_q(request,id):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/seekerverify'</script>")
    return render(request,"SEEKER/Blood_quantity.html",{'id':id})

def blood_q_POST(request, id):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/seekerverify'</script>")
    bldq=request.POST['textfield']
    print(request.session['lid'])
    date= datetime.datetime.now().strftime("%Y-%m-%d")
    obj=Request()
    obj.status="pending"
    obj.BLOOD_ID_id=id
    obj.date=date
    obj.SEEKER = Seeker.objects.get(LOGIN=request.session['lid'])
    obj.quantity=bldq
    obj.save()
    return HttpResponse("<script>alert('Requested Successfully');window.location='/seeker_feedback'</script>")

def v_bld_req(request):
    if request.session['log'] != "lo":
        return HttpResponse("<script>alert('Logout Successfully');window.location='/seekerverify'</script>")
    request.session['head'] = "Request Status"
    vreq=Request.objects.filter(SEEKER = Seeker.objects.get(LOGIN_id=request.session['lid']))
    return render(request, "SEEKER/S_VIEW_BLOOD_REQUEST_STATUS.html", {'data':vreq})






