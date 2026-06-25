from urllib import request

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
import os
import time

from .models import *


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact_us(request):
    return render(request, 'contact_us.html')


def show_cars_all(request):
    obj1 = Cardata.objects.all()
    data = carphotos.objects.all()
    return render(request,'show_cars_all.html',{'key1': obj1,'data': data})

def author(request):
    return render(request, 'author.html')

def login(request):
    if request.method == 'POST':


        email = request.POST['T1']
        password = request.POST['T2']

        obj= logindata.objects.get(email=email,password=password)
        usertype=obj.usertype

        request.session['userid'] = obj.email
        request.session['usertype'] = usertype
        request.session['email'] = email
        if usertype == 'admin':
            return HttpResponseRedirect('/show_car/')
        elif usertype == 'user':
            return HttpResponseRedirect('/show_car/')
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'login.html')


def logout(request):
    try:
        del request.session['usertype']
        del request.session['email']
    except:
        pass
    return HttpResponseRedirect('/login/')

def adminhome(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'admin':
            obj=admindata.objects.all()
            return render(request, 'adminhome.html',{'obj':obj})
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def userhome(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'user':
            obj=userdata.objects.all()
            return render(request, 'userhome.html',{'key1':obj})
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')



def studentreg(request):
    if request.method == 'POST':

        obj = Student()
        obj1 = logindata()

        a = request.POST['T1']
        b = request.POST['T2']
        c = request.POST['T3']
        d = request.POST['T4']
        e = 'student'

        obj.name = a
        obj.branch = b
        obj.email = c

        obj1.email = c
        obj1.password = d
        obj1.usertype = e

        obj.save()
        obj1.save()
        return render(request, 'studentreg.html', {'data': "success"})
    else:
        return render(request, 'studentreg.html')

def carreg(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST' :
                obj1=Cardata()

                a = request.POST['T1']
                b = request.POST['T2']
                c = request.POST['T3']
                d = request.POST['T4']
                e = request.POST['T5']
                f = request.POST['T6']
                g = request.POST['T7']
                h = request.POST['T8']

                obj1.Car_Name=a
                obj1.Price_Per_Day=b
                obj1.Car_Model=c
                obj1.Car_Number=d
                obj1.Fuel_Type=e
                obj1.Transmissio=f
                obj1.Seating_Capacity=g
                obj1.Availability_Status=h

                obj1.save()

                return render(request, 'carreg.html', {'data': "success"})
            else:
                return render(request, 'carreg.html')
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def adminreg(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':

                obj=logindata()
                obj1=admindata()

                a = request.POST['T1']
                b = request.POST['T2']
                c= request.POST['T3']
                d = request.POST['T4']
                e = request.POST['T5']
                f='admin'

                obj1.name=a
                obj1.email=b
                obj1.phone=c

                obj.email=b
                obj.password=d
                obj.usertype=f


                obj1.save()
                obj.save()

                return render(request, 'adminreg.html', {'data': "success"})
            else:
                return render(request, 'adminreg.html')
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def show_admin(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'admin':
            obj=admindata.objects.all()
            return render(request, 'showadmin.html', {'key1': obj})
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def userreg(request):
    if request.method == 'POST':
        obj=logindata()
        obj1=userdata()
        a=request.POST['T1']
        b=request.POST['T2']
        c=request.POST['T3']
        d=request.POST['T4']
        e=request.POST['T5']
        f=request.POST['T6']
        g='user'
        obj1.name=a
        obj1.email=b
        obj1.phone=c
        obj1.address=d

        obj.email=b
        obj.password=e
        obj.usertype=g

        obj1.save()
        obj.save()

        return HttpResponse ("""
        <script>
        alert('Registration Successful');
        window.location.href='/login/';
        </script>
        """)
    else:
        return render(request, 'author.html')

def show_user_reg(request):
    return render(request, 'userreg.html')

def show_user_profile(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype =='user':
            obj=userdata.objects.all()
            return render(request, 'show_user_profile.html', {'key1': obj})
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def show_user(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'admin':
            obj=userdata.objects.all()
            return render(request, 'showuser.html', {'key1': obj})
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def edit_admin_profile(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                email=request.POST['email']
                obj=admindata.objects.filter(email=email)
                return render(request, 'edit_admin_profile.html', {'obj': obj})
            else:
                return redirect('/adminhome/')
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def save_edit_admin_profile(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST':
                name=request.POST['name']
                email=request.POST['email']
                phone=request.POST['phone']

                obj=admindata.objects.get(email=email)
                obj.name=name
                obj.email=email
                obj.phone=phone
                obj.save()
                return HttpResponse("""
                               <script>
                               alert('Profile Updated Successfully');
                               window.location='/adminhome/';
                               </script>
                               """)
            else:
                return redirect('/adminhome/')

        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')


def edit_user_profile(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'user':
            if request.method == 'POST':
                userid = request.POST['userid']
                obj = userdata.objects.filter(userid=userid)
                return render(request, 'edit_user_profile.html',{'key1': obj})
            return redirect('/user_profile/')
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def save_edit_user_profile(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'user':
            if request.method == 'POST':

                userid = request.POST['id']
                name = request.POST['T1']
                email = request.POST['T2']
                phone = request.POST['T3']
                address = request.POST['T4']
                obj=userdata.objects.get(userid=userid)

                obj.userid=userid
                obj.name=name
                obj.email=email
                obj.phone=phone
                obj.address=address

                obj.save()
                return HttpResponse("""
                <script>
                alert('Profile Updated Successfully');
                window.location='/show_user_profile/';
                </script>
                """)
            else:
                return redirect('/user_profile/')
        else:
            return render(request, 'author.html')

    else:
        return render(request, 'author.html')

def edit_user_password(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'user':
            if request.method == 'POST':
                email=request.POST['email']
                obj=logindata.objects.filter(email=email)
                return render(request, 'edit_user_password.html', {'key1': obj})
            return redirect('/user_profile/')
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def save_edit_user_password(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'user':
            if request.method == 'POST':
                email=request.POST['email']
                old_password = request.POST['T1']
                new_password = request.POST['T2']
                confirm_password = request.POST['T3']
                obj=logindata.objects.get(email=email)

                obj.email=email
                obj.password=new_password

                obj.save()
                return HttpResponse("""
                <script>
                alert('password Updated Successfully');
                window.location='/show_user_profile/';
                </script>
                """)
            else:
                return redirect('/user_profile/')
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')




def show_car(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'user' :
            obj1=Cardata.objects.all()
            data = carphotos.objects.all()
            obj2=userdata.objects.all()
            return render(request, 'showcars.html', {'key1': obj1, 'data': data, 'key2': obj2,'j':"j",'block':'m3'})
        elif usertype == 'admin':
            obj1 = Cardata.objects.all()
            data = carphotos.objects.all()
            obj2 = userdata.objects.all()
            return render(request, 'show_cars_admin.html', {'key1': obj1, 'data': data, 'key2': obj2,'k':"k",'block':'m1'})

        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def upload_car_photos(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'admin':
            if request.method == 'POST' and 'F2' not in request.FILES:

                carid = request.POST['id']

                request.session['carid'] = carid

                return render(request, 'uploadcarphotos.html')

            elif request.method == 'POST' and 'F2' in request.FILES:

                carid = request.session['carid']

                upload_file = request.FILES['F2']

                print("harish")

                path = os.path.basename(upload_file.name)

                file_ext = os.path.splitext(path)[1][1:]

                filename = str(int(time.time())) + '.' + file_ext

                fs = FileSystemStorage()

                fs.save(filename, upload_file)

                car = Cardata.objects.get(id=carid)

                obj = carphotos()

                obj.carid = carid
                obj.Car_Name = car.Car_Name
                obj.Car_Photo = filename

                obj.save()

                return HttpResponse("""
                <script>
                alert('Photo Updated Successfully');
                window.location='/show_car/';
                </script>
                """)
            else:
                return render(request, 'author.html')
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def edit_cars(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == ('admin'):
            if request.method == 'POST':
                id=request.POST['id']
                obj=Cardata.objects.filter(id=id)
                return render(request, 'edit_cars.html', {'key1': obj})
            else:
                return redirect('/show_car')
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def save_edit_cars(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == ('admin'):
            if request.method == 'POST':
                id=request.POST['id']
                a = request.POST['T1']
                b = request.POST['T2']
                c = request.POST['T3']
                d = request.POST['T4']
                e = request.POST['T5']
                f = request.POST['T6']
                g = request.POST['T7']
                h = request.POST['T8']

                obj1=Cardata.objects.get(id=id)
                obj1.Car_Name=a
                obj1.Price_Per_Day=b
                obj1.Car_Model=c
                obj1.Car_Number=d
                obj1.Fuel_Type=e
                obj1.Transmissio=f
                obj1.Seating_Capacity=g
                obj1.Availability_Status=h

                obj1.save()
                return HttpResponse("""
                <script>
                alert('Updated Successfully');
                window.location='/show_car/';
                </script>
                """)
            else:
                return redirect('/show_car/')
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def delete_car(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            id = request.POST['id']
            image=request.POST['image']
            obj=Cardata.objects.get(id=id)
            obj.delete()
            obj1=carphotos.objects.get(id=id)
            obj1.delete()
            return HttpResponse("""
            <script>
            alert('Deleted Successfully');
            window.location='/show_car/';
            </script>
            """)
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def add_to_cart(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        print('usertype=',usertype)
        if usertype == 'user':

            carid = request.POST['carid']
            userid = request.session['email']
            check = AddToCart.objects.filter(userid=userid,carid=carid)
            if check.exists():
                return HttpResponse("""
                   <script>
                       alert('Car Already Added In Cart');
                       window.location='/show_car/';
                   </script>
                   """)
            Car_Photo=request.POST['Car_Photo']
            Car_Name=request.POST['Car_Name']
            car_price=request.POST['car_price']
            Car_Model=request.POST['Car_Model']
            Car_Number=request.POST['Car_Number']
            Fuel_Type=request.POST['Fuel_Type']
            Seating_Capacity=request.POST['Seating_Capacity']

            userid = request.session['email']
            print('userid:',userid)
            print('carid:',carid)
            obj=AddToCart()
            obj.userid=userid
            obj.carid=carid
            obj.Car_Photo=Car_Photo
            obj.Car_Name=Car_Name
            obj.Price_Per_Day=car_price
            obj.Car_Model=Car_Model
            obj.Car_Number=Car_Number
            obj.Fuel_Type=Fuel_Type
            obj.Seating_Capacity=Seating_Capacity

            obj.save()
            print('save successfully')
            return redirect('/show_car/')
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')


def show_add_to_car(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'user':
            obj=AddToCart.objects.all()
            total = 0
            for d in obj:
                total = total + d.Price_Per_Day
            return render(request, 'showaddtocart.html', {'key1': obj,'total': total})
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def delete_cart(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'user':
            userid=request.POST['userid']
            obj=AddToCart.objects.get(userid=userid)
            obj.delete()
            return redirect('/show_add_to_car')
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def booknow(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'user':
            userid=request.session['email']
            total = request.POST['total']
            carid=request.POST['carid']
            Car_Name = request.POST.getlist('Car_Name')

            Car_Number = request.POST.getlist('Car_Number')

            context = {
                'userid': userid,
                'carid': carid,
                'Car_Name': Car_Name,
                'Car_Number': Car_Number,
                 'total':total,
                 }

            return render(request, 'booknow.html',context)
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def save_booking(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'user':
            obj=BookNow()

            userid=request.session['email']
            total = request.POST['total']
            carid=request.POST['carid']
            Car_Name = request.POST['Car_Name']
            Car_Number = request.POST['Car_Number']
            AddToCart.objects.filter(userid=userid,carid=carid).delete()

            a=request.POST['Full_Name']
            b=request.POST['Email']
            c=request.POST['Mobile_Number']
            d=request.POST['Address']
            e=request.POST['driver_license']
            f=request.FILES['f']
            g=request.POST['g']
            h=request.POST['h']
            i=request.POST['i']
            j=request.POST['j']
            k=request.POST['k']
            l=request.POST['l']

            obj.userid=userid
            obj.Car_Name = Car_Name
            obj.Car_Number = Car_Number
            obj.Full_Name=a
            obj.Email=b
            obj.Mobile_Number=c
            obj.Address=d
            obj.driver_license=e
            obj.Driver_License_Photo=f
            obj.Pickup_Date=g
            obj.Pickup_Time=h
            obj.Return_Date=i
            obj.Return_Time=j
            obj.Pickup_Location=k
            obj.Drop_Location=l
            context={
                'Car_Name': Car_Name,
                'userid': userid,
                'total': total,
                'Full_Name': a,
                'Email': b,
                'Mobile_Number': c,
                'Address': d,
                'driver_license': e,
            }

            obj.save()
            return render(request,'payment.html',context)
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def pay(request):
    if request.session.has_key('usertype'):

        usertype = request.session['usertype']

        if usertype == 'user':

            obj = Payment()

            bookingid = request.POST['bookingid']



            obj.Amount = request.POST['amount']

            obj.Payment_Method = request.POST['payment']

            obj.Payment_Status = "Paid"

            obj.save()

            return redirect('/show_car/',"Payment Successfully")

        else:
            return render(request, 'author.html')

    else:
        return render(request, 'author.html')


def show_user_history(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'user':
            obj=BookNow.objects.all()
            obj1=Payment.objects.all()
            return render(request, 'show_user_history.html', {'key1': obj,'total': obj,'key2': obj1})
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def Accept_booking(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'admin':
            bookingid=request.POST['bookingid']
            obj=BookNow.objects.get(bookingid=bookingid)
            obj.Status="Accepted"
            obj.save()
            return HttpResponse("""
                               <script>
                                   alert('Accepted');
                                   window.location='/show_all_bookings/';
                               </script>
                               """)

        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def Reject_booking(request):
    if request.session.has_key('usertype'):
        usertype = request.session['usertype']
        if usertype == 'admin':
            bookingid = request.POST['bookingid']
            obj = BookNow.objects.get(bookingid=bookingid)
            obj.Status = "Rejected"
            obj.save()
            return redirect('/show_all_bookings/')
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')

def show_all_bookings(request):
    if request.session.has_key('usertype'):
        usertype=request.session['usertype']
        if usertype == 'admin':
            obj = BookNow.objects.all()
            return render(request,'show_all_car_bookings.html',{'key1':obj})
        else:
            return render(request, 'author.html')
    else:
        return render(request, 'author.html')
