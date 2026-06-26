"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.openHome),
    path("index/", views.openHome),
    path("pg-details/", views.viewDetails),
    path("booknow/", views.viewBookNow),
    path("about/", views.viewAbout),
    path("pg/", views.viewPGPage),
    path("contact/", views.viewContact),
    path("login/", views.viewLogin),
    path("registration/", views.viewRegister),
    path("booking/", views.booking),
    path("add_review/", views.addReview),
    # admin
    path("admin_index/", views.viewAdminIndex),
    path("admin_master/", views.viewAdminMaster),
    path("add_brand/", views.viewBrand),
    path("add_vendor/", views.viewVendor),
    path("booking_report/", views.viewBooking),
    path("payment_details/", views.viewPayment),
    path("admin_login/", views.viewAdminLogin),
    path("admin_login_details/", views.loginAdminDetails, name="login"),
    # admin database
    path("addAdmin_Master/", views.viewAdd_Admin_Master),
    path("addVendor/", views.viewAddVendor),
    path("add_register/", views.newRegister, name="home"),
    path("add_contact/", views.addContact, name="home"),
    path("admin_contact/", views.adminContact, name="home"),
    path("get_contacts/", views.getContacts, name="home"),
    path("check_web_login/", views.checkWebLogin, name=""),
    # vendor
    path("index_user/", views.viewIndex_User),
    path("add_pg/", views.viewAddPG),
    path("addPG/", views.viewPG),
    path("get_single_item/", views.getSingleItem, name=""),
    path("get_home_details/", views.getHomeDetails, name=""),
    path("web_booking/", views.saveBooking, name=""),
    path("get_bookings/", views.getBookings, name=""),
    path("get_my_bookings/", views.getMyBookings, name=""),
    path("my_bookings/", views.myBookings, name=""),
    path("user_profile_details/", views.userProfileDetails),
    path("get_reviews/", views.getReviews),
    path("forgot_password/", views.forgot_password),
    path("forgot_password_otp/", views.forgotPassword),
    path("validate_otp/", views.validateOTP),
    path("update_password/", views.updatePassword),
    path("update_password_validate/", views.updatePasswordValidate),
]
