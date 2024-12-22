from django.shortcuts import render,redirect,HttpResponse
from imageupload.forms import  *
from django.contrib import messages
# Create your views here.


# def hotel_image_view(request):
#     if request.method == 'POST':
#         form = HotelForm(request.POST, request.FILES)

#         if form.is_valid():
#             form.save()
#             return redirect('/admin_display_hotel_images')
            
#     else:
#         form = HotelForm()
#     return render(request,'home_slider_image_form.html', {'form': form })

def hotel_image_view1(request):
    if request.method == 'POST':
        form = HotelForm1(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/admin_display_hotel_images1')
            
    else:
        form = HotelForm1()
    return render(request,'home_slider_image_form1.html', {'form': form })

def hotel_image_view2(request):
    if request.method == 'POST':
        form = HotelForm2(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/admin_display_hotel_images2')
            
    else:
        form = HotelForm2()
    return render(request,'home_slider_image_form2.html', {'form': form })

def hotel_image_view3(request):
    if request.method == 'POST':
        form = HotelForm3(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/admin_display_hotel_images3')
            
    else:
        form = HotelForm3()
    return render(request,'home_slider_image_form3.html', {'form': form })

def hotel_image_view4(request):
    if request.method == 'POST':
        form = HotelForm4(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/admin_display_hotel_images4')
            
    else:
        form = HotelForm4()
    return render(request,'home_slider_image_form4.html', {'form': form })


def success(request):
    #return HttpResponse('Successfully Upload Image.....!')
    return render(request,'success.html')


def display_hotel_images(request):
    if request.method == 'GET':
       Hotels = Hotel.objects.all()
    return render(request,'home.html',{'hotel_images': Hotels})

def home(request):
    if request.method == 'GET':
       Hotels = Hotel.objects.all()
    return render(request,'home.html',{'hotel_images': Hotels})


def display_hotel_images1(request):
    if request.method == 'GET':
       Hotels1 = Hotel1.objects.all()
    return render(request,'home.html',{'hotel_images1': Hotels1})

def display_hotel_images2(request):
    if request.method == 'GET':
       Hotels2 = Hotel2.objects.all()
    return render(request,'home.html',{'hotel_images2': Hotels2})

def display_hotel_images3(request):
    if request.method == 'GET':
       Hotels3 = Hotel3.objects.all()
    return render(request,'home.html',{'hotel_images3': Hotels3})

def display_hotel_images4(request):
    if request.method == 'GET':
       Hotels4 = Hotel4.objects.all()
    return render(request,'home.html',{'hotel_images4': Hotels4})




def admin_display_hotel_images(request):
    if request.method == 'GET':
       Hotels = Hotel.objects.all()
    return render(request,'display_home_slider_image.html',{'hotel_images': Hotels})

def admin_display_hotel_images1(request):
    if request.method == 'GET':
       Hotels1 = Hotel1.objects.all()
    return render(request,'admin_display_hotel_images1.html',{'hotel_images1': Hotels1})

def admin_display_hotel_images2(request):
    if request.method == 'GET':
       Hotels2 = Hotel2.objects.all()
    return render(request,'admin_display_hotel_images2.html',{'hotel_images2': Hotels2})

def admin_display_hotel_images3(request):
    if request.method == 'GET':
       Hotels3 = Hotel3.objects.all()
    return render(request,'admin_display_hotel_images3.html',{'hotel_images3': Hotels3})

def admin_display_hotel_images4(request):
    if request.method == 'GET':
       Hotels4 = Hotel4.objects.all()
    return render(request,'admin_display_hotel_images4.html',{'hotel_images4': Hotels4})


def destroy(request, id):  
    hotel = Hotel.objects.get(id=id)  
    hotel.delete()  
    messages.success(request,"Delete Image successfully")
    return redirect("/admin_display_hotel_images")

def destroy1(request, id):  
    hotel1 = Hotel1.objects.get(id=id)  
    hotel1.delete()  
    messages.success(request,"Delete Image successfully")
    return redirect("/hotel_images1")

def destroy2(request, id):  
    hotel2 = Hotel2.objects.get(id=id)  
    hotel2.delete()  
    messages.success(request,"Delete Image successfully")
    return redirect("/hotel_images2")

def destroy3(request, id):  
    hotel3 = Hotel3.objects.get(id=id)  
    hotel3.delete()  
    messages.success(request,"Delete Image successfully")
    return redirect("/hotel_images3")

def destroy4(request, id):  
    hotel4 = Hotel4.objects.get(id=id)  
    hotel4.delete()  
    messages.success(request,"Delete Image successfully")
    return redirect("/hotel_images4")





def edit1(request, id):  
    hotel1 = Hotel1.objects.get(id=id)  
    return render(request,'edit_image1.html', {'hotel1':hotel1})  
def edit2(request, id):  
    hotel2 = Hotel2.objects.get(id=id)  
    return render(request,'edit_image2.html', {'hotel2':hotel2})  
def edit3(request, id):  
    hotel3 = Hotel3.objects.get(id=id)  
    return render(request,'edit_image3.html', {'hotel3':hotel3})  
def edit4(request, id):  
    hotel4 = Hotel4.objects.get(id=id)  
    return render(request,'edit_image4.html', {'hotel4':hotel4})  

def edit(request, id):  
    hotel = Hotel.objects.get(id=id)  
    return render(request,'edit_image.html', {'hotel':hotel})  
def update(request, id):  
    hotel = Hotel.objects.get(id=id)  
    form = HotelForm(request.POST, request.FILES ,instance = hotel)  
    if form.is_valid():  
        form.save()  
        return redirect("/admin_display_hotel_images")  
    return render(request, 'edit_image.html', {'hotel': hotel})  
def update1(request, id):  
    hotel1 = Hotel1.objects.get(id=id)  
    form = HotelForm1(request.POST, request.FILES ,instance = hotel1)  
    if form.is_valid():  
        form.save()  
        return redirect("/hotel_images1")  
    return render(request, 'edit_image1.html', {'hotel1': hotel1})  
def update2(request, id):  
    hotel2 = Hotel2.objects.get(id=id)  
    form = HotelForm2(request.POST, request.FILES ,instance = hotel2)  
    if form.is_valid():  
        form.save()  
        return redirect("/hotel_images2")  
    return render(request, 'edit_image2.html', {'hotel2': hotel2})  
def update3(request, id):  
    hotel3 = Hotel3.objects.get(id=id)  
    form = HotelForm3(request.POST, request.FILES ,instance = hotel3)  
    if form.is_valid():  
        form.save()  
        return redirect("/hotel_images3")  
    return render(request, 'edit_image3.html', {'hotel3': hotel3})  
def update4(request, id):  
    hotel4 = Hotel4.objects.get(id=id)  
    form = HotelForm4(request.POST, request.FILES ,instance = hotel4)  
    if form.is_valid():  
        form.save()  
        return redirect("/hotel_images4")  
    return render(request, 'edit_image4.html', {'hotel4': hotel4}) 

