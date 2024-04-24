"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BloodLine_Logistics import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.log),
    path('logout',views.logout),
    path('donorverify',views.donorverify),
    path('accept_donor/<id>/<em>',views.accept_donor),
    path('reject_donor/<id>/<em>',views.reject_donor),
    path('seekerverify',views.seekerverify),
    path('accept_seeker/<id>/<em>',views.accept_seeker),
    path('reject_seeker/<id>/<em>',views.reject_seeker),
    path('verifieddonor',views.verifieddonor),
    path('verifiedseeker',views.verifiedseeker),
    path('viewrequest',views.viewrequest),
    path('verifyrequest/<id>/<bid>',views.verifyrequest),
    path('view_approved_request',views.view_approved_request),
    path('complete_request/<id>',views.complete_request),
    path('reqproceed/<id>',views.reqproceed),
    path('viewhistory',views.viewhistory),
    path('donorhistory',views.donorhistory),
    path('login_post',views.login_post),
    path('admin_login',views.admin_login),
    path('view_blood',views.view_blood),
    path('add_blood',views.add_blood),
    path('add_blood_post',views.add_blood_post),
    path('delete_blood/<id>',views.delete_blood),
    path('blood_stock/<id>',views.blood_stock),
    path('blood_stock_POST/<id>',views.blood_stock_POST),
    path('willing_donor/<id>',views.willing_donor),

    ####################################################3

    path('donor_reg', views.donor_reg),
    path('donor_reg_post', views.donor_reg_post),
    path('view_Donor_Home',views.view_Donor_Home),
    path('donor_index',views.donor_index),
    path('view_Donor_Profile',views.view_Donor_Profile),
    path('donor_update_profile_post',views.donor_update_profile_post),
    path('donor_request',views.donor_request),
    path('donor_willingness/<id>',views.donor_willingness),
    path('donor_accept_req',views.donor_accept_req),
    path('donor_feedback',views.donor_feedback),
    path('donor_feedback_POST',views.donor_feedback_POST),

    ########################################################

    path('seeker_reg', views.seeker_reg),
    path('seeker_reg_post', views.seeker_reg_post),
    path('Seeker_Home', views.Seeker_Home),
    path('view_Seeker_Profile', views.view_Seeker_Profile),
    path('view_Seeker_Profile_POST',views.view_Seeker_Profile_POST),
    path('seeker_feedback',views.seeker_feedback),
    path('seeker_feedback_POST',views.seeker_feedback_POST),
    path('seeker_view_blood',views.seeker_view_blood),
    path('blood_q/<id>',views.blood_q),
    path('blood_q_POST/<id>',views.blood_q_POST),
    path('v_bld_req',views.v_bld_req),


]

