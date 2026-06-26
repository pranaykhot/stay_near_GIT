from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from app.models import AdminMaster
from app.models import AddVendors
from app.models import AddPG
from app.models import Register
from app.models import Order
from app.models import Contact, Review
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Sum
from app.models import ForgotPassword


# Create your views here.
def openHome(request):
    return render(request, "web/index.html")


def viewDetails(request):
    if "web_email" in request.session:
        return render(request, "web/pg-details.html")
    else:
        return render(request, "web/login.html")


def viewBookNow(request):
    return render(request, "web/booknow.html")


def viewAbout(request):
    return render(request, "web/about.html")


def viewPGPage(request):
    return render(request, "web/pg.html")


def viewContact(request):
    return render(request, "web/contact.html")


def viewLogin(request):
    return render(request, "web/login.html")


def viewRegister(request):
    return render(request, "web/registration.html")


# admin
def viewAdminIndex(request):
    countPG = AddPG.objects.filter().count()
    countVendors = AddVendors.objects.filter().count()
    countOrder = Order.objects.filter().count()
    countOrderAmt = Order.objects.aggregate(total_amount=Sum("or_total_amount"))[
        "total_amount"
    ]

    context = {
        "countPG": countPG,
        "countVendors": countVendors,
        "countOrder": countOrder,
        "countOrderAmt": countOrderAmt,
    }
    return render(request, "admin/admin_index.html", context)


def viewAdminMaster(request):
    return render(request, "admin/admin_master.html")


def viewBrand(request):
    return render(request, "admin/add_brand.html")


def viewVendor(request):
    return render(request, "admin/add_vendor.html")


def viewBooking(request):
    return render(request, "admin/booking_report.html")


def viewPayment(request):
    return render(request, "admin/payment_details.html")


def booking(request):
    return render(request, "vendor/booking.html")


def viewAdminLogin(request):
    return render(request, "admin/admin_login.html")


def adminContact(request):
    return render(request, "admin/contact.html")


# vendor
def viewIndex_User(request):
    countPG = AddPG.objects.filter(ab_created_by=request.session["email"]).count()
    countVendors = AddVendors.objects.filter().count()
    countOrder = Order.objects.filter(or_created_by=request.session["email"]).count()
    countOrderAmt = Order.objects.filter(
        or_created_by=request.session["email"]
    ).aggregate(total_amount=Sum("or_total_amount"))["total_amount"]

    countOrderAmt = 0 if countOrderAmt is None else countOrderAmt

    context = {
        "countPG": countPG,
        "countVendors": countVendors,
        "countOrder": countOrder,
        "countOrderAmt": countOrderAmt,
    }
    return render(request, "vendor/index_user.html", context)


def viewAddPG(request):
    countPG = AddPG.objects.filter(ab_created_by=request.session["email"]).count()
    context = {"countPG": countPG}

    return render(request, "vendor/add_pg.html", context)


def getSingleItem(request):
    if "web_email" in request.session:
        products_json = AddPG.objects.filter(ab_id=request.POST["txtID"]).values()
        data = list(products_json)
        value = JsonResponse(data, safe=False)
        return value
    else:
        return render(request, "web/login.html")


# admin database
def viewAdd_Admin_Master(request):
    if request.POST["action"] == "add":
        AdminMaster.objects.create(
            ad_name=request.POST["txtName"],
            ad_mobile=request.POST["txtNumber"],
            ad_email=request.POST["txtEmail"],
            ad_password=request.POST["txtPassword"],
            ad_role=request.POST["txtRole"],
        )

    elif request.POST["action"] == "getData":
        data = AdminMaster.objects.filter(ad_status="0").values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values

    elif request.POST["action"] == "update":
        data = AdminMaster.objects.filter(ad_id=request.POST["id"]).update(
            ad_name=request.POST["txtName1"],
            ad_mobile=request.POST["txtNumber1"],
            ad_email=request.POST["txtEmail1"],
            ad_role=request.POST["txtRole1"],
        )

    elif request.POST["action"] == "delete":
        data = AdminMaster.objects.filter(ad_id=request.POST["id"]).update(
            ad_status="1"
        )

    return HttpResponse()


#
def viewAddVendor(request):
    if request.POST["action"] == "add":
        AddVendors.objects.create(
            av_name=request.POST["txtName"],
            av_mobile=request.POST["txtNumber"],
            av_email=request.POST["txtEmail"],
            av_password=request.POST["txtPassword"],
            av_role=request.POST["txtRole"],
        )

    elif request.POST["action"] == "getData":
        data = AddVendors.objects.filter(av_status="0").values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values

    elif request.POST["action"] == "update":
        data = AddVendors.objects.filter(av_id=request.POST["id"]).update(
            av_name=request.POST["txtName1"],
            av_mobile=request.POST["txtNumber1"],
            av_email=request.POST["txtEmail1"],
            av_role=request.POST["txtRole1"],
        )

    elif request.POST["action"] == "delete":
        data = AddVendors.objects.filter(av_id=request.POST["id"]).update(av_status="1")

    return HttpResponse()


#
#
def viewPG(request):
    if request.POST["action"] == "add":
        AddPG.objects.create(
            ab_name=request.POST["txtName"],
            ab_price=request.POST["txtPrice"],
            ab_details=request.POST["txtDetail"],
            ab_address=request.POST["txtAddress"],
            ab_location=request.POST["txtLocation"],
            ab_image=request.FILES["txtImage"],
            ab_created_by=request.session["email"],
        )

    elif request.POST["action"] == "getData":
        data = AddPG.objects.filter(
            ab_status="0", ab_created_by=request.session["email"]
        ).values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values

    elif request.POST["action"] == "update":
        data = AddPG.objects.filter(ab_id=request.POST["id"]).update(
            ab_name=request.POST["txtName1"],
            ab_price=request.POST["txtPrice1"],
            ab_details=request.POST["txtDetail1"],
            ab_address=request.POST["txtAddress1"],
        )

    elif request.POST["action"] == "delete":
        data = AddPG.objects.filter(ab_id=request.POST["id"]).update(ab_status="1")

    return HttpResponse()


def loginAdminDetails(request):
    if AdminMaster.objects.filter(
        ad_email=request.POST["txtEmail"],
        ad_password=request.POST["txtPassword"],
        ad_status=0,
    ).count():
        data = AdminMaster.objects.filter(ad_email=request.POST["txtEmail"]).values()
        data = list(data)
        dictValue = data[0]
        request.session["email"] = dictValue["ad_email"]
        request.session["role"] = dictValue["ad_role"]
        request.session["name"] = dictValue["ad_name"]
        return HttpResponse(dictValue["ad_role"])
    elif AddVendors.objects.filter(
        av_email=request.POST["txtEmail"],
        av_password=request.POST["txtPassword"],
        av_status=0,
    ).count():
        data = AddVendors.objects.filter(av_email=request.POST["txtEmail"]).values()
        data = list(data)
        dictValue = data[0]
        request.session["email"] = dictValue["av_email"]
        request.session["role"] = dictValue["av_role"]
        request.session["name"] = dictValue["av_name"]
        return HttpResponse(dictValue["av_role"])
    return HttpResponse("0")


def checkWebLogin(request):
    if Register.objects.filter(
        rg_email=request.POST["txtEmail"], rg_password=request.POST["txtPassword"]
    ).exists():
        request.session["web_email"] = request.POST["txtEmail"]
        return HttpResponse("1")
    else:
        return HttpResponse("10")


def newRegister(request):
    if Register.objects.filter(
        rg_email=request.POST["txtEmail"], rg_mobile=request.POST["txtMobileNo"]
    ).exists():
        return HttpResponse("10")
    else:
        lclID = Register.objects.count()
        status = "0"
        lclNewID = lclID + 1

        Register.objects.create(
            rg_id=lclNewID,
            rg_name=request.POST["txtName"],
            rg_mobile=request.POST["txtMobileNo"],
            rg_email=request.POST["txtEmail"],
            rg_password=request.POST["txtPassword"],
            rg_address=request.POST["txtAddress"],
        )

        return HttpResponse("0")


def addReview(request):
    Review.objects.create(
        rv_name=request.POST["txtName1"],
        rv_mobile=request.POST["txtMobileNo1"],
        rv_email=request.POST["txtEmail1"],
        rv_review=request.POST["txtReview1"],
        rv_pg_id=request.POST["pgID"],
    )

    return HttpResponse("0")


def addContact(request):
    Contact.objects.create(
        ct_name=request.POST["txtName"],
        ct_mobile=request.POST["txtMobileNo"],
        ct_email=request.POST["txtEmail"],
        ct_subject=request.POST["txtSubject"],
        ct_message=request.POST["txtMessage"],
    )

    return HttpResponse("0")


def getContacts(request):
    data = Contact.objects.filter().values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values


def getHomeDetails(request):
    data = AddPG.objects.filter(ab_status="0").values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values


def saveBooking(request):
    Order.objects.create(
        or_name=request.POST["txtNameBook"],
        or_total_amount=request.POST["totalAmt"],
        or_ordered_by=request.session["web_email"],
        or_transaction_id=request.POST["transaction_id"],
        or_status="Success",
        or_created_by=request.POST["email"],
    )

    send_mail(
        "Booking Confirmation",
        "Thank you for Booking PG",
        settings.EMAIL_HOST_USER,
        [request.session["web_email"]],
        fail_silently=False,
    )

    return HttpResponse()


def getBookings(request):
    # print(request.session['role']);
    if request.session["role"] == "Admin":
        data = Order.objects.filter().values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values

    else:
        data = Order.objects.filter(or_created_by=request.session["email"]).values()
        data = list(data)
        values = JsonResponse(data, safe=False)
        return values


def getMyBookings(request):
    data = Order.objects.filter(or_ordered_by=request.session["web_email"]).values()
    data = list(data)

    for value in data:
        try:
            register_data = AddPG.objects.filter(
                ab_created_by=value["or_created_by"]
            ).values()
            value["ab_name"] = register_data[0]["ab_name"] if register_data else None
            value["ab_price"] = register_data[0]["ab_price"] if register_data else None
            value["ab_location"] = (
                register_data[0]["ab_location"] if register_data else None
            )

        except:
            print("")
    values = JsonResponse(data, safe=False)
    return values


def myBookings(request):
    return render(request, "web/my_bookings.html")


def userProfileDetails(request):
    data = Register.objects.filter(rg_email=request.session["web_email"]).values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values


def getReviews(request):
    data = Review.objects.filter(rv_pg_id=request.POST["pgID"]).values()
    data = list(data)
    values = JsonResponse(data, safe=False)
    return values


def forgot_password(request):
    return render(request, "web/forgot_password.html", {})


def updatePassword(request):
    return render(request, "web/update_password.html", {})


def forgotPassword(request):
    if ForgotPassword.objects.filter(fp_email=request.POST["txtEmail"]).count():
        ForgotPassword.objects.filter(fp_email=request.POST["txtEmail"]).update(
            fp_otp=request.POST["txtOTP"]
        )
    else:
        ForgotPassword.objects.create(
            fp_email=request.POST["txtEmail"], fp_otp=request.POST["txtOTP"]
        )
    send_mail(
        "OTP",
        "Your OTP is " + request.POST["txtOTP"],
        settings.EMAIL_HOST_USER,
        [request.POST["txtEmail"]],
        fail_silently=False,
    )
    return HttpResponse(0)


def validateOTP(request):
    if ForgotPassword.objects.filter(
        fp_email=request.POST["txtEmail"], fp_otp=request.POST["txtOTP"]
    ).count():
        request.session["forgot_email"] = request.POST["txtEmail"]
        return HttpResponse(0)
    else:
        return HttpResponse(10)


def updatePasswordValidate(request):
    Register.objects.filter(rg_email=request.session["forgot_email"]).update(
        rg_password=request.POST["txtPassword"]
    )
    return HttpResponse(0)
