from django.http import HttpResponseRedirect,StreamingHttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
# from .forms import RegisterForm,StudentForm,DepartmentForm,CourseForm,SemesterForm,EditCourseForm,EditDepartmentForm,EditStudentForm
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.template.defaulttags import register

from django.db.models import Sum,Avg

# from WSGIREF.UTIL import FileWrapper

from wsgiref.util import FileWrapper
import mimetypes
import os

import pdfkit
from django.http import HttpResponse
from django.template.loader import get_template

# def html_to_pdf(request):
#     # Load your HTML template
#     template = get_template('show_bonafide_certificate.html')
#     html = template.render({})

#     # Convert HTML to PDF
#     pdf = pdfkit.from_string(html, False)

#     # Create a response with PDF content
#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="output.pdf"'
#     return response
@login_required(login_url="/login")
def html_to_pdf(request):
    # Load your HTML template
    username=CustomUser.objects.filter(username=request.session['username']) 
    print(username)
    value=username.first()
    print(type(value))

    
    students = Student.objects.filter(user=value.id)
    template = get_template('show_bonafide_certificate.html')
   
    html = template.render({'students':students})
    # Specify the path to wkhtmltopdf executable manually
    config = pdfkit.configuration(wkhtmltopdf='H:/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, False, configuration=config)

    # Create a response with PDF content
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bonafide_certificate.pdf" ;'
    return response


# def display_hotel_images(request):
#     if request.method == 'GET':
#        Hotels = Hotel.objects.all()
#     return render(request,'home.html',{'hotel_images': Hotels})

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
        else:

             print("username or password is incorrect")
             messages.warning(request,"username or password is incorrect")
        
        
    else:
        form = RegisterForm()

    return render(request, 'registration/registration.html', {"form": form})


# @login_required(login_url="/login")
def home(request):
    request.session['username']=request.user.username
    
    return render(request,'home.html')

 


def show_sem(request):
    sem = Semester.objects.all()  
    paginator = Paginator(sem, 6)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    return render(request,"show_sem.html",{'sem':pages}) 




def store_sem(request):  
    if request.method == "POST":  
        form = SemesterForm(request.POST)  
        try:
            sem=Semester.objects.get(sem_id=request.POST.get('sem_id',False))
        except Semester.DoesNotExist:
            sem=None
        if sem:
            messages.warning(request,"Semester Already Exists")
            return HttpResponseRedirect(request.path_info)
        else:   
            if form.is_valid():
                try:  
                    form.save()
                    messages.success(request,"Data Stored Sucessfully")  
                    return redirect('/showsem')  
                except:  
                    pass  
    else:  
        form = SemesterForm()  
    return render(request,'add_sem.html',{'form':form}) 

def edit_sem(request, sem_id):  
    sem= Semester.objects.get(sem_id=sem_id) 
    form = EditSemesterForm(instance = sem)  
    return render(request,'edit_sem.html', {'sem':sem,'form':form}) 


def update_sem(request, sem_id):  
    sem = Semester.objects.get(sem_id=sem_id)  
    print(sem)
    form = EditSemesterForm(request.POST, instance = sem)  
    print(form)
    if form.is_valid():  
        form.save() 
       
        messages.info(request,"Data Updated Sucessfully")
        return redirect("/showsem")  
    return render(request, 'edit_course.html', {'sem':sem}) 


def delete_sem(request,sem_id):  
    sem = Semester.objects.get(sem_id=sem_id)  
    sem.delete()  
    return redirect("/showsem")


###############################################################
## Course Related Crud
###############################################################

def store_course(request):  
    if request.method == "POST":  
        form = CourseForm(request.POST)  
        try:
           cou=Course.objects.get(cid=request.POST.get('cid',False))
        except Course.DoesNotExist:
            cou=None
        if cou:
            messages.warning(request,"Cid Already Exists")
            return HttpResponseRedirect(request.path_info)
        else:   
            if form.is_valid():
                try:  
                    form.save()
                    print("Hello Course")
                    messages.success(request,"Data Stored Sucessfully")  
                    print("Hello message course")
                    return redirect('showcourse/')  
                except:  
                    pass  
    else:  
        form = CourseForm()  
    return render(request,'add_course.html',{'form':form}) 



def show_course(request):
    cour = Course.objects.all().order_by('cid')  
    paginator = Paginator(cour, 6)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    return render(request,"show_course.html",{'cour':pages}) 


def edit_course(request, cid):  
    course= Course.objects.get(cid=cid) 
    form = EditCourseForm(instance = course)  
    return render(request,'edit_course.html', {'course':course,'form':form}) 


def update_course(request, cid):  
    course = Course.objects.get(cid=cid)  
    print(course)
    form = EditCourseForm(request.POST, instance = course)  
    print(form)
    if form.is_valid():  
        form.save() 
       
        messages.info(request,"Data Updated Sucessfully")
        return redirect("/showcourse")  
    return render(request, 'edit_course.html', {'course': course}) 


def delete_course(request, cid):  
    course = Course.objects.get(cid=cid)  
    course.delete()  
    return redirect("/showcourse")
################################################################
#  department related Views
################################################################


def store_dep(request):  
    if request.method == "POST":  
        form = DepartmentForm(request.POST)  
        try:
            dep=Department.objects.get(did=request.POST.get('did',False))
        except Department.DoesNotExist:
            dep=None
        if dep:
            messages.warning(request,"department Already Exists")
            return HttpResponseRedirect(request.path_info)
        else:   
            if form.is_valid():
                try:  
                    form.save()
                    messages.success(request,"Data Stored Sucessfully")  
                    return redirect('show_dep')  
                except:  
                    pass  
    else:  
        form = DepartmentForm()  
    return render(request,'add_dept.html',{'form':form}) 



def edit_depart(request, did):  
    dept= Department.objects.get(did=did) 
    form = EditDepartmentForm(instance = dept)  
    return render(request,'edit_department.html', {'dept':dept,'form':form}) 


def update_depart(request, did):  
    dept = Department.objects.get(did=did)  
    form = EditDepartmentForm(request.POST, instance = dept)  
    if form.is_valid():  
        form.save() 
       
        messages.info(request,"Data Updated Sucessfully")
        return redirect("/show_dep")  
    return render(request, 'edit_department.html', {'dept': dept}) 

def edit_sem1(request,com_id):  
    cour= com_mst.objects.get(com_id=com_id) 
    form = Editsem1Form(instance = cour)  
    return render(request,'edit_sem1.html', {'cour':cour,'form':form}) 


def update_sem1(request,com_id):  
    cour = com_mst.objects.get(com_id=com_id)  
    form = Editsem1Form(request.POST, instance = cour)  
    if form.is_valid():  
        form.save() 
       
        messages.info(request,"Data Updated Sucessfully")
        return redirect("/showcom")  
    else:
        print('hii')
    return render(request, 'edit_sem1.html', {'cour': cour}) 


def show_dep(request):
    dep = Department.objects.all().order_by('did')   
    paginator = Paginator(dep, 8)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    return render(request,"show_department.html",{'dep':pages}) 


def delete_depart(request, did):  
    dept = Department.objects.get(did=did)  
    dept.delete()  
    return redirect("/showdepart")

############################################################
# Student Crud Related Views
#############################################################

def store_student(request):  
    # print("h1")
    if request.method == "POST": 
        # print("H2") 
        form = StudentForm(request.POST)  
        try:
            stu=Student.objects.get(sid=request.POST.get('sid',False))
        except Student.DoesNotExist:
            # print("H3 None")
            stu=None
        if stu:
            messages.warning(request,"Sid Already Exists")
            return HttpResponseRedirect(request.path_info)
        else:   
            if form.is_valid():
                # print("H4")
                try:  
                    username = request.session.get('username')
                    user = CustomUser.objects.get(username=username)
                    student = form.save(commit=False)
                    student.user = user
                    student.save()
                    messages.success(request,"Data Stored Sucessfully")  
                    return redirect('/showstu')  
                except:  
                    pass                   
    else:  
        form = StudentForm()  
    return render(request,'add_stu1.html',{'form':form}) 


def show_student(request):

    students = Student.objects.all()   
    paginator = Paginator(students, 2)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    #return render(request,"show_subject_type.html",{'dep':pages}) 
    return render(request,"show_student.html",{'students':pages}) 

def show_student1(request):
    students = Student.objects.all()   
    # user=request.session['username']
    # person = get_object_or_404(Student, username=user)
   
  
    # return render(request,"show_provisional_request.html",{'students':students,'person': person}) 
    return render(request,"show_provisional_request.html",{'students':students})


def edit_student(request, sid):  
    stu= Student.objects.get(sid=sid) 
    form = EditStudentForm(instance = stu)  
    return render(request,'edit_student.html', {'stu':stu,'form':form}) 


def update_student(request, sid):  
    stu = Student.objects.get(sid=sid)  
    form = EditStudentForm(request.POST, instance = stu)  
    if form.is_valid():  
        form.save() 
       
        messages.info(request,"Data Updated Sucessfully")
        return redirect("/showstu")  
        
    return render(request, 'edit_student.html', {'stu': stu})


def delete_student(request, sid):  
    stu = Student.objects.get(sid=sid)  
    stu.delete()  
    return redirect("/showstu")

def logout_view(request):
    logout(request)
    try:
        del request.session['username']
    
    except:
        return redirect('login')
    return redirect('login')


@login_required(login_url="/login")
def user_details(request):
    user_id=request.session['username']

        
    # data = Student.objects.all()  
    #person = get_object_or_404(Student,int(user)=user_id)
    data = Student.objects.get(user=user_id)
    return render(request, 'user_details.html', {'data': data})


def main_admin(request):
    return render(request,'main_admin.html')

@login_required(login_url="/login")
def about(request):
     return render(request,'about.html')

@login_required(login_url="/login")
def feedback(request):
     return render(request,'feedback.html')

@login_required(login_url="/login")
def feedback1(request):
     return render(request,'feedback1.html')

@login_required(login_url="/login")
def feedback2(request):
     return render(request,'feedback2.html')

@login_required(login_url="/login")
def feedback3(request):
     return render(request,'feedback3.html')

@login_required(login_url="/login")
def feedback4(request):
     return render(request,'feedback4.html')

@login_required(login_url="/login")
def blog(request):
     return render(request,'blog.html')

@login_required(login_url="/login")
def blog2(request):
     return render(request,'blog2.html')

@login_required(login_url="/login")
def send_provisional_request(request):
    
     return render(request,'send_provisional_request.html')


@login_required(login_url="/login")
def store_provisional_request(request): 
    
    username=CustomUser.objects.filter(username=request.session['username']) 
    value=username.first()
    students = Student.objects.filter(user=value.id)
    if request.method == "POST":  
        form = Provisional_resultForm(request.POST)  
        try:
            pro=Provisional_result.objects.get(reason=request.POST.get('reason',False))
        except Provisional_result.DoesNotExist:
            pro=None
        if pro:
            messages.warning(request,"Request Already Exists")
            return HttpResponseRedirect(request.path_info)
        else:   
            if form.is_valid():
                try:  
                    form.save()
                    messages.success(request,"Request Stored Sucessfully")  
                    return redirect('show_provisional_request')  
                except:  
                    pass  
    else:  
        form = Provisional_resultForm()  
    return render(request,'send_provisional_request.html',{'form':form,'students':students}) 

    


@login_required(login_url="/login")
def show_provisional_request(request):
    username=CustomUser.objects.filter(username=request.session['username']) 
    print(username)
    value=username.first()
   
    print(value)
    students = Student.objects.filter(user=value.id)

    stu_id=students.first().sid
    print(stu_id)
    pid = Student.objects.filter(sid=stu_id).first()
    print(pid)
    pro = Provisional_result.objects.filter(sid=pid)
    return render(request,"show_provisional_request.html",{'pro':pro,'students':students}) 

def hod_show_provisional_request(request):
    pro = Provisional_result.objects.all()   
    return render(request,"hod_show_provisional_request.html",{'pro':pro}) 












@login_required(login_url="/login")
def store_bonafide_request(request):  
    username=CustomUser.objects.filter(username=request.session['username']) 
    value=username.first()
    students = Student.objects.filter(user=value.id)
    # students = Student.objects.all() 
    if request.method == "POST":  
        form = Bonafide_CertificateForm(request.POST)  
        try:
            pro1=Bonafide_Certificate.objects.get(reason=request.POST.get('reason',False))
        except Bonafide_Certificate.DoesNotExist:
            pro1=None
        if pro1:
            messages.warning(request,"Request Already Exists")
            return HttpResponseRedirect(request.path_info)
        else:   
            if form.is_valid():
                try:  
                    form.save()
                    messages.success(request,"Request Stored Sucessfully")  
                    return redirect('show_bonafide_request')  
                except:  
                    pass  
    else:  
        form =Bonafide_CertificateForm()  
    return render(request,'send_bonafide_request.html',{'form':form,'students':students}) 

    


@login_required(login_url="/login")
def show_bonafide_request(request):
    # username=CustomUser.objects.filter(username=request.session['username']) 
    # print(username)
    # value=username.first()
   
    # print(value)
    # students = Student.objects.filter(user=value.id)
  
  
    # stu_id=students.first().sid
    # print(stu_id)
    # pid = Student.objects.filter(sid=stu_id).first()
    # print(pid)
    # pro = Bonafide_Certificate.objects.filter(sid=pid)
    # return render(request,"show_bonafide_request.html",{'pro':pro,'students':students}) 
    username=CustomUser.objects.filter(username=request.session['username']) 
    print(username)
    value=username.first()
   
    print(value)
    students = Student.objects.filter(user=value.id)

    stu_id=students.first().sid
    print(stu_id)
    pid = Student.objects.filter(sid=stu_id).first()
    print(pid)
    pro = Bonafide_Certificate.objects.filter(sid=pid)
    return render(request,"show_bonafide_request.html",{'pro':pro,'students':students}) 

def hod_show_bonafide_request(request):
    pro = Bonafide_Certificate.objects.all()   
    return render(request,"hod_show_bonafide_request.html",{'pro':pro}) 

def delete_hod_show_bonafide_request(request, bono_id):  
    bono = Bonafide_Certificate.objects.get(bono_id=bono_id)  
    bono.delete()  
    return redirect("/hod_show_bonafide_request") 

@login_required(login_url="/login")
def delete_show_bonafide_request(request, bono_id):  
    bono = Bonafide_Certificate.objects.get(bono_id=bono_id)  
    bono.delete()  
    return redirect("/show_bonafide_request") 


def delete_hod_show_provisional_request(request, pro_id):  
    pro = Provisional_result.objects.get(pro_id=pro_id)  
    pro.delete()  
    return redirect("/hod_show_provisional_request") 

@login_required(login_url="/login")
def delete_show_provisional_request(request,pro_id):  
    pro = Provisional_result.objects.get(pro_id=pro_id)  
    pro.delete()  
    return redirect("/show_provisional_request") 

   

def main_hod(request):
    return render(request,"main_hod.html")

# def hod_show_bonafide_request(request):
#     return render(request,"hod_show_bonafide_request.html")

@login_required(login_url="/login")
def show_bonafide_certificate(request):
    username=CustomUser.objects.filter(username=request.session['username']) 
    print(username)
    value=username.first()
    print(value)
    students = Student.objects.filter(user=value.id)
    # students = Student.objects.all() 
    return render(request,"show_bonafide_certificate.html",{'students':students}) 


#@login_required(login_url="/login")
# def download_bonafide_certificate(request):
#     base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     filename= 'show_bonafide_certificate.html'
#     filepath = base_dir + '/templates/' + filename
#     thefile = filepath
#     filename = os.path.basename(thefile)
#     chunk_size = 8192
#     response = StreamingHttpResponse(FileWrapper(open(thefile, 'rb'),chunk_size),
#         content_type=mimetypes.guess_type(thefile)[0])
#     response['Content-Length']= os.path.getsize(thefile)
#     response['Content-Disposition'] = "Attachment;filename=%s" % filename
#     return response




@login_required(login_url="/login")
def store_final_request(request): 
    
    username=CustomUser.objects.filter(username=request.session['username']) 
    value=username.first()
    students = Student.objects.filter(user=value.id)
    if request.method == "POST":  
        form = Final_resultForm(request.POST)  
        try:
            pro=Final_result.objects.get(final_id=request.POST.get('final_id',False))
        except Final_result.DoesNotExist:
            pro=None
        if pro:
            messages.warning(request,"Request Already Exists")
            return HttpResponseRedirect(request.path_info)
        else:   
            if form.is_valid():
                try:  
                    form.save()
                    messages.success(request,"Request Stored Sucessfully")  
                    return redirect('show_final_request')  
                except:  
                    pass  
    else:  
        form = Final_resultForm() 
        print('fail') 
    return render(request,'send_final_request.html',{'form':form,'students':students}) 

    


@login_required(login_url="/login")
def show_final_request(request):
    username=CustomUser.objects.filter(username=request.session['username']) 
    print(username)
    value=username.first()
   
    print(value)
    students = Student.objects.filter(user=value.id)
  
    # return render(request,"show_provisional_request.html",{'students':students})
    stu_id=students.first()
    print(stu_id)
    pid = Student.objects.filter(sid=stu_id.sid).first()
    print(pid)
    pro = Final_result.objects.filter(sid=pid)

    return render(request,"show_final_request.html",{'pro':pro,'students':students}) 

def hod_show_final_request(request):
    pro = Final_result.objects.all()   
    return render(request,"hod_show_final_request.html",{'pro':pro}) 
    
def delete_hod_show_final_request(request, final_id):  
    pro = Final_result.objects.get(final_id=final_id)  
    pro.delete()  
    return redirect("/hod_show_final_request") 

@login_required(login_url="/login")
def delete_show_final_request(request,final_id):  
    pro = Final_result.objects.get(final_id=final_id)  
    pro.delete()  
    return redirect("/show_final_request")


# def store_mark(request):  
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     value=username.first()
#     students = Student.objects.filter(user=value.id)
    
#     if request.method == "POST":  
#         form = marksForm(request.POST)  
#         try:
#             sem=marks.objects.get(m_id=request.POST.get('m_id',False))
#         except marks.DoesNotExist:
#             sem=None
#         if sem:
#             messages.warning(request,"Marks Id Already Exists")
#             return HttpResponseRedirect(request.path_info)
#         else:   
#             if form.is_valid():
#                 try:  
#                     form.save()
#                     messages.success(request,"Data Stored Sucessfully")  
#                     return redirect('show_mark')  
#                 except:  
#                     pass  
#     else:  
#         form = marksForm()  
#     return render(request,'add_marks.html',{'form':form,'students':students}) 

# def show_mark(request):
#     dep = marks.objects.all().order_by('m_id')   
#     paginator = Paginator(dep, 8)
#     try:
#         page = int(request.GET.get('page','1'))
#     except:
#         page = 1     
#     try:
#         pages = paginator.page(page)
#     except(Paginator.EmptyPage , Paginator.InvalidPage):
#         pages = paginator.page(paginator.num_pages) 
#     return render(request,"show_mark.html",{'students':pages}) 

# def delete_mark(request, m_id):  
#     pro = marks.objects.get(m_id=m_id)  
#     pro.delete()  
#     return redirect("/showmark") 


# ******************** Subject Type ***********************

def store_subject_type(request):  
    # username=CustomUser.objects.filter(username=request.session['username']) 
    # value=username.first()
    # students = Student.objects.filter(user=value.id)
    
    if request.method == "POST":  
        form = subject_typeform(request.POST)  
        try:
            sem=subject_type.objects.get(type_id=request.POST.get('type_id',False))
        except subject_type.DoesNotExist:
            sem=None
        if sem:
            messages.warning(request,"Subject Type Id Already Exists")
            return HttpResponseRedirect(request.path_info)
        else:   
            if form.is_valid():
                try:  
                    form.save()
                    messages.success(request,"Data Stored Sucessfully")  
                    return redirect('show_subject_type')  
                except:  
                    pass  
    else:  
        form = subject_typeform()  
    return render(request,'add_subject_type.html',{'form':form}) 

def show_subject_type(request):
    dep = subject_type.objects.all().order_by('type_id')   
    paginator = Paginator(dep, 2)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    return render(request,"show_subject_type.html",{'dep':pages}) 

def delete_subject_type(request,type_id):  
    stype = subject_type.objects.get(type_id=type_id)  
    stype.delete()  
    return redirect("/show_subject_type")


# def store_theory_internal_component(request):  
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     value=username.first()
#     students = Student.objects.filter(user=value.id)
    
#     # theory= theory_internal_component.objects.all()
#     # value= theory.first()
#     # th = theory_internal_component.filter()

#     if request.method == "POST":  
#         form = theory_internal_componentform(request.POST)  
#         try:
#             sem=theory_internal_component.objects.get(type_id=request.POST.get('iid1',False))
#         except theory_internal_component.DoesNotExist:
#             sem=None
#         if sem:
#             messages.warning(request," Id Already Exists")
#             return HttpResponseRedirect(request.path_info)
#         else:   
#             if form.is_valid():
#                 try:  
#                     internal = form.save(commit = False) 
                     
#                     total = internal.unit_test + internal.attendance + internal.one_day

#                     internal.total = total

#                     internal.save()

#                     messages.success(request,"Data Stored Sucessfully")  
#                     return redirect('/show_theory_internal_component')  
#                 except:  
#                     pass  
#     else:  
#         form = theory_internal_componentform()  
#     return render(request,'add_theory_internal_component.html',{'form':form,'studnets':students}) 

# def show_theory_internal_component(request):
#     dep = theory_internal_component.objects.all().order_by('iid1')   
#     paginator = Paginator(dep, 2)
#     try:
#         page = int(request.GET.get('page','1'))
#     except:
#         page = 1     
#     try:
#         pages = paginator.page(page)
#     except(Paginator.EmptyPage , Paginator.InvalidPage):
#         pages = paginator.page(paginator.num_pages) 
#     return render(request,"show_theory_internal_component.html",{'dep':pages}) 

# def delete_theory_internal_component(request,iid1):  
#     stype = theory_internal_component.objects.get(iid1=iid1)  
#     stype.delete()  
#     return redirect("/show_theory_internal_component")





# def store_theory_external_component(request):  
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     value=username.first()
#     students = Student.objects.filter(user=value.id)
    
#     # theory= theory_internal_component.objects.all()
#     # value= theory.first()
#     # th = theory_internal_component.filter()

#     if request.method == "POST":  
#         form = theory_external_componentform(request.POST)  
#         try:
#             sem=theory_external_component.objects.get(type_id=request.POST.get('eid1',False))
#         except theory_external_component.DoesNotExist:
#             sem=None
#         if sem:
#             messages.warning(request," Id Already Exists")
#             return HttpResponseRedirect(request.path_info)
#         else:   
#             if form.is_valid():
#                 try:  
#                     form.save()
#                     messages.success(request,"Data Stored Sucessfully")  
#                     return redirect('/show_theory_external_component')  
#                 except:  
#                     pass  
#     else:  
#         form = theory_external_componentform()  
#     return render(request,'add_theory_external_component.html',{'form':form,'studnets':students}) 

# def show_theory_external_component(request):
#     dep = theory_external_component.objects.all().order_by('eid1')   
#     paginator = Paginator(dep, 2)
#     try:
#         page = int(request.GET.get('page','1'))
#     except:
#         page = 1     
#     try:
#         pages = paginator.page(page)
#     except(Paginator.EmptyPage , Paginator.InvalidPage):
#         pages = paginator.page(paginator.num_pages) 
#     return render(request,"show_theory_external_component.html",{'dep':pages}) 

# def delete_theory_external_component(request,eid1):  
#     stype = theory_external_component.objects.get(eid1=eid1)  
#     stype.delete()  
#     return redirect("/show_theory_external_component")




# def store_theory_practicle_internal_component(request):  
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     value=username.first()
#     students = Student.objects.filter(user=value.id)
    
#     # theory= theory_internal_component.objects.all()
#     # value= theory.first()
#     # th = theory_internal_component.filter()

#     if request.method == "POST":  
#         form = theory_practicle_internal_componentform(request.POST)  
#         try:
#             sem=theory_practicle_internal_component.objects.get(iid2=request.POST.get('iid2',False))
#         except theory_practicle_internal_component.DoesNotExist:
#             sem=None
#         if sem:
#             messages.warning(request," Id Already Exists")
#             return HttpResponseRedirect(request.path_info)
#         else:   
#             if form.is_valid():
#                 try:  
#                     form.save()
#                     messages.success(request,"Data Stored Sucessfully")  
#                     return redirect('/show_theory_practicle_internal_component')  
#                 except:  
#                     pass    
#     else:  
#         form = theory_practicle_internal_componentform()  
#     return render(request,'add_theory_practicle_internal_component.html',{'form':form,'studnets':students}) 

# def show_theory_practicle_internal_component(request):
#     dep = theory_practicle_internal_component.objects.all().order_by('iid2')   
#     paginator = Paginator(dep, 2)
#     try:
#         page = int(request.GET.get('page','1'))
#     except:
#         page = 1     
#     try:
#         pages = paginator.page(page)
#     except(Paginator.EmptyPage , Paginator.InvalidPage):
#         pages = paginator.page(paginator.num_pages) 
#     return render(request,"show_theory_practicle_internal_component.html",{'dep':pages}) 

# def delete_theory_practicle_internal_component(request,iid2):  
#     stype = theory_practicle_internal_component.objects.get(iid2=iid2)  
#     stype.delete()  
#     return redirect("/show_theory_practicle_internal_component")





# def store_theory_practicle_external_component(request):  
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     value=username.first()
#     students = Student.objects.filter(user=value.id)
    
#     # theory= theory_internal_component.objects.all()
#     # value= theory.first()
#     # th = theory_internal_component.filter()

#     if request.method == "POST":  
#         form = theory_practicle_external_componentform(request.POST)  
#         try:
#             sem=theory_practicle_external_component.objects.get(eid2=request.POST.get('eid2',False))
#         except theory_practicle_external_component.DoesNotExist:
#             sem=None
#         if sem:
#             messages.warning(request," Id Already Exists")
#             return HttpResponseRedirect(request.path_info)
#         else:   
#             if form.is_valid():
#                 try:  
#                     form.save()
#                     messages.success(request,"Data Stored Sucessfully")  
#                     return redirect('/show_theory_practicle_external_component')  
#                 except:  
#                     pass  
#     else:  
#         form = theory_practicle_external_componentform()  
#     return render(request,'add_theory_practicle_external_component.html',{'form':form,'studnets':students}) 

# def show_theory_practicle_external_component(request):
#     dep = theory_practicle_external_component.objects.all().order_by('eid2')   
#     paginator = Paginator(dep, 2)
#     try:
#         page = int(request.GET.get('page','1'))
#     except:
#         page = 1     
#     try:
#         pages = paginator.page(page)
#     except(Paginator.EmptyPage , Paginator.InvalidPage):
#         pages = paginator.page(paginator.num_pages) 
#     return render(request,"show_theory_practicle_external_component.html",{'dep':pages}) 

# def delete_theory_practicle_external_component(request,eid2):  
#     stype = theory_practicle_external_component.objects.get(eid2=eid2)  
#     stype.delete()  
#     return redirect("/show_theory_practicle_external_component")





# def store_practicle_internal_component(request):  
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     value=username.first()
#     students = Student.objects.filter(user=value.id)
    
#     # theory= theory_internal_component.objects.all()
#     # value= theory.first()
#     # th = theory_internal_component.filter()

#     if request.method == "POST":  
#         form = practicle_internal_componentform(request.POST)  
#         try:
#             sem=practicle_internal_component.objects.get(iid3=request.POST.get('iid3',False))
#         except practicle_internal_component.DoesNotExist:
#             sem=None
#         if sem:
#             messages.warning(request," Id Already Exists")
#             return HttpResponseRedirect(request.path_info)
#         else:   
#             if form.is_valid():
#                 try:  
#                     form.save()
#                     messages.success(request,"Data Stored Sucessfully")  
#                     return redirect('/show_practicle_internal_component')  
#                 except:  
#                     pass    
#     else:  
#         form = practicle_internal_componentform()  
#     return render(request,'add_practicle_internal_component.html',{'form':form,'studnets':students}) 

# def show_practicle_internal_component(request):
#     dep = practicle_internal_component.objects.all().order_by('iid3')   
#     paginator = Paginator(dep, 2)
#     try:
#         page = int(request.GET.get('page','1'))
#     except:
#         page = 1     
#     try:
#         pages = paginator.page(page)
#     except(Paginator.EmptyPage , Paginator.InvalidPage):
#         pages = paginator.page(paginator.num_pages) 
#     return render(request,"show_practicle_internal_component.html",{'dep':pages}) 

# def delete_practicle_internal_component(request,iid3):  
#     stype = practicle_internal_component.objects.get(iid3=iid3)  
#     stype.delete()  
#     return redirect("/show_practicle_internal_component")




# def store_practicle_external_component(request):  
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     value=username.first()
#     students = Student.objects.filter(user=value.id)
    
#     # theory= theory_internal_component.objects.all()
#     # value= theory.first()
#     # th = theory_internal_component.filter()

#     if request.method == "POST":  
#         form = practicle_external_componentform(request.POST)  
#         try:
#             sem=practicle_external_component.objects.get(eid3=request.POST.get('eid3',False))
#         except practicle_external_component.DoesNotExist:
#             sem=None
#         if sem:
#             messages.warning(request," Id Already Exists")
#             return HttpResponseRedirect(request.path_info)
#         else:   
#             if form.is_valid():
#                 try:  
#                     form.save()
#                     messages.success(request,"Data Stored Sucessfully")  
#                     return redirect('/show_practicle_external_component')  
#                 except:  
#                     pass    
#     else:  
#         form = practicle_external_componentform()  
#     return render(request,'add_practicle_external_component.html',{'form':form,'studnets':students}) 

# def show_practicle_external_component(request):
#     dep = practicle_external_component.objects.all().order_by('eid3')   
#     paginator = Paginator(dep, 2)
#     try:
#         page = int(request.GET.get('page','1'))
#     except:
#         page = 1     
#     try:
#         pages = paginator.page(page)
#     except(Paginator.EmptyPage , Paginator.InvalidPage):
#         pages = paginator.page(paginator.num_pages) 
#     return render(request,"show_practicle_external_component.html",{'dep':pages}) 

# def delete_practicle_external_component(request,eid3):  
#     stype = practicle_external_component.objects.get(eid3=eid3)  
#     stype.delete()  
#     return redirect("/show_practicle_external_component")





# def store_project_external_component(request):  
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     value=username.first()
#     students = Student.objects.filter(user=value.id)
    
#     # theory= theory_internal_component.objects.all()
#     # value= theory.first()
#     # th = theory_internal_component.filter()

#     # theory= theory_internal_component.objects.all()
#     # value= theory.first()
#     # th = theory_internal_component.objects.filter(type_id=value)

#     if request.method == "POST":  
#         form = project_external_componentform(request.POST)  
#         try:
#             sem=project_external_component.objects.get(eid4=request.POST.get('eid4',False))
#         except project_external_component.DoesNotExist:
#             sem=None
#         if sem:
#             messages.warning(request," Id Already Exists")
#             return HttpResponseRedirect(request.path_info)
#         else:   
#             if form.is_valid():
#                 try:  
#                     form.save()
#                     messages.success(request,"Data Stored Sucessfully")  
#                     return redirect('/show_project_external_component')  
#                 except:  
#                     pass    
#     else:  
#         form = project_external_componentform()  
#     return render(request,'add_project_external_component.html',{'form':form,'studnets':students}) 

# def show_project_external_component(request):
   
#     dep = project_external_component.objects.all().order_by('eid4')   
#     paginator = Paginator(dep, 2)
#     try:
#         page = int(request.GET.get('page','1'))
#     except:
#         page = 1     
#     try:
#         pages = paginator.page(page)
#     except(Paginator.EmptyPage , Paginator.InvalidPage):
#         pages = paginator.page(paginator.num_pages) 
#     return render(request,"show_project_external_component.html",{'dep':pages}) 

# def delete_project_external_component(request,eid4):  
#     stype = project_external_component.objects.get(eid4=eid4)  
#     stype.delete()  
#     return redirect("/show_project_external_component")





# def store_project_internal_component(request):  
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     value=username.first()
#     students = Student.objects.filter(user=value.id)
    
#     # theory= theory_internal_component.objects.all()
#     # value= theory.first()
#     # th = theory_internal_component.filter()

#     if request.method == "POST":  
#         form = project_internal_componentform(request.POST)  
#         try:
#             sem=project_internal_component.objects.get(iid4=request.POST.get('iid4',False))
#         except project_internal_component.DoesNotExist:
#             sem=None
#         if sem:
#             messages.warning(request," Id Already Exists")
#             return HttpResponseRedirect(request.path_info)
#         else:   
#             if form.is_valid():
#                 try:  
#                     form.save()
#                     messages.success(request,"Data Stored Sucessfully")  
#                     return redirect('/show_project_internal_component')  
#                 except:  
#                     pass    
#     else:  
#         form = project_internal_componentform()  
#     return render(request,'add_project_internal_component.html',{'form':form,'studnets':students}) 

# def show_project_internal_component(request):
#     dep = project_internal_component.objects.all().order_by('iid4')   
#     paginator = Paginator(dep, 2)
#     try:
#         page = int(request.GET.get('page','1'))
#     except:
#         page = 1     
#     try:
#         pages = paginator.page(page)
#     except(Paginator.EmptyPage , Paginator.InvalidPage):
#         pages = paginator.page(paginator.num_pages) 
#     return render(request,"show_project_internal_component.html",{'dep':pages}) 

# def delete_project_internal_component(request,iid4):  
#     stype = project_internal_component.objects.get(iid4=iid4)  
#     stype.delete()  
#     return redirect("/show_project_internal_component")





# def store_subject_master(request):  
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     value=username.first()
#     students = Student.objects.filter(user=value.id)
    
#     # theory= theory_internal_component.objects.all()
#     # value= theory.first()
#     # th = theory_internal_component.filter()

#     if request.method == "POST":  
#         form = subject_masterform(request.POST)  
#         try:
#             sem=subject_master.objects.get(sm_id=request.POST.get('sm_id',False))
#         except subject_master.DoesNotExist:
#             sem=None
#         if sem:
#             messages.warning(request," Id Already Exists")
#             return HttpResponseRedirect(request.path_info)
#         else:   
#             if form.is_valid():
#                 try:  
#                     form.save()
#                     messages.success(request,"Data Stored Sucessfully")  
#                     return redirect('/show_subject_master')  
#                 except:  
#                     pass    
#     else:  
#         form = subject_masterform()  
#     return render(request,'add_subject_master.html',{'form':form,'studnets':students}) 

# def show_subject_master(request):
#     dep = subject_master.objects.all().order_by('sm_id')   
#     paginator = Paginator(dep, 2)
#     try:
#         page = int(request.GET.get('page','1'))
#     except:
#         page = 1     
#     try:
#         pages = paginator.page(page)
#     except(Paginator.EmptyPage , Paginator.InvalidPage):
#         pages = paginator.page(paginator.num_pages) 
#     return render(request,"show_subject_master.html",{'dep':pages}) 

# def delete_subject_master(request,sm_id):  
#     stype = subject_master.objects.get(sm_id=sm_id)  
#     stype.delete()  
#     return redirect("/show_subject_master")


# def practicle_internal_external1(request):
#     return render(request,"add_practicle_internal_external1.html")





# def theory_internal_external(request):
#     return render(request,"add_theory_internal_external.html")

# def theory_practicle_internal_external(request):
#     return render(request,"add_theory_practicle_internal_external.html")

# def practicle_internal_external(request):
#     return render(request,"add_practicle_internal_external.html")

# def project_internal_external(request):
#     return render(request,"add_project_internal_external.html")

def subject_component(request):
     return render(request,"subject_component.html")




# def store_subject_marks(request):  
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     value=username.first()
#     students = Student.objects.filter(user=value.id)
    
#     # theory= theory_internal_component.objects.all()
#     # value= theory.first()
#     # th = theory_internal_component.filter()

#     if request.method == "POST":  
#         form = subject_marksform(request.POST)  
#         try:
#             sem=subject_marks.objects.get(sub_mark_id=request.POST.get('sub_mark_id',False))
#         except subject_marks.DoesNotExist:
#             sem=None
#         if sem:
#             messages.warning(request," Id Already Exists")
#             return HttpResponseRedirect(request.path_info)
#         else:   
#             if form.is_valid():
#                 try:  
#                     form.save()
#                     messages.success(request,"Data Stored Sucessfully")  
#                     return redirect('/show_subject_marks')  
#                 except:  
#                     pass    
#     else:  
#         form = subject_marksform()  
#     return render(request,'add_subject_marks.html',{'form':form,'student':students}) 

# def show_subject_marks(request):
#     dep = subject_marks.objects.all().order_by('sub_mark_id')   
#     paginator = Paginator(dep, 2)
#     try:
#         page = int(request.GET.get('page','1'))
#     except:
#         page = 1     
#     try:
#         pages = paginator.page(page)
#     except(Paginator.EmptyPage , Paginator.InvalidPage):
#         pages = paginator.page(paginator.num_pages) 
#     return render(request,"show_subject_marks.html",{'dep':pages}) 

# def delete_subject_marks(request,sub_mark_id):  
#     stype = subject_marks.objects.get(sub_mark_id=sub_mark_id)  
#     stype.delete()  
#     return redirect("/show_subject_marks")

# def add(request):
#     r1= int(request.get('review1'))
#     r2= int(request.get('review2'))
#     total = r1+r2
#     return render(request,"show_subject_marks.html",{'total':total}) 






def history(request):
     return render(request,"history.html")

def final_history(request):
     return render(request,"final_history.html")


# def store_sem1_marks(request):  
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     value=username.first()
#     students = Student.objects.filter(user=value.id)
    
#     # theory= theory_internal_component.objects.all()
#     # value= theory.first()
#     # th = theory_internal_component.filter()

#     if request.method == "POST":  
#         form = sem1_marksform(request.POST)  
#         try:
#             sem=sem1_marks.objects.get(sem1_id=request.POST.get('sem1_id',False))
#         except sem1_marks.DoesNotExist:
#             sem=None
#         if sem:
#             messages.warning(request," Id Already Exists")
#             return HttpResponseRedirect(request.path_info)
#         else:   
#             if form.is_valid():
#                 try:  
#                     form.save()
#                     messages.success(request,"Data Stored Sucessfully")  
#                     return redirect('/sem1_history')  
#                 except:  
#                     pass    
#     else:  
#         form = sem1_marksform()  
#     return render(request,'add_sem1_marks.html',{'form':form,'student':students}) 


# def sem1_history(request):
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     print(username)
#     value=username.first()
#     print(value)
#     students = Student.objects.filter(user=value.id)
#     dep = sem1_marks.objects.all().order_by('sem1_id') 
#     return render(request,"sem1_history.html",{'dep':dep,'students':students}) 

# def delete_sem1_marks(request,sem1_id):  
#     stype = sem1_marks.objects.get(sem1_id=sem1_id)  
#     stype.delete()  
#     return redirect("/sem1_history")

# def store_sem2_marks(request):  
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     value=username.first()
#     students = Student.objects.filter(user=value.id)
    
#     # theory= theory_internal_component.objects.all()
#     # value= theory.first()
#     # th = theory_internal_component.filter()

#     if request.method == "POST":  
#         form = sem2_marksform(request.POST)  
#         try:
#             sem=sem2_marks.objects.get(sem2_id=request.POST.get('sem2_id',False))
#         except sem2_marks.DoesNotExist:
#             sem=None
#         if sem:
#             messages.warning(request," Id Already Exists")
#             return HttpResponseRedirect(request.path_info)
#         else:   
#             if form.is_valid():
#                 try:  
#                     form.save()
#                     messages.success(request,"Data Stored Sucessfully")  
#                     return redirect('/sem2_history')  
#                 except:  
#                     pass    
#     else:  
#         form = sem2_marksform()  
#     return render(request,'add_sem2_marks.html',{'form':form,'student':students}) 

# def sem2_history(request):
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     print(username)
#     value=username.first()
#     print(value)
#     students = Student.objects.filter(user=value.id)
#     dep = sem2_marks.objects.all().order_by('sem2_id') 
#     return render(request,"sem2_history.html",{'dep':dep,'students':students}) 


# def store_sem3_marks(request):  
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     value=username.first()
#     students = Student.objects.filter(user=value.id)
    
#     # theory= theory_internal_component.objects.all()
#     # value= theory.first()
#     # th = theory_internal_component.filter()

#     if request.method == "POST":  
#         form = sem1_marksform(request.POST)  
#         try:
#             sem=sem3_marks.objects.get(sem3_id=request.POST.get('sem3_id',False))
#         except sem3_marks.DoesNotExist:
#             sem=None
#         if sem:
#             messages.warning(request," Id Already Exists")
#             return HttpResponseRedirect(request.path_info)
#         else:   
#             if form.is_valid():
#                 try:  
#                     form.save()
#                     messages.success(request,"Data Stored Sucessfully")  
#                     return redirect('/sem3_history')  
#                 except:  
#                     pass    
#     else:  
#         form = sem3_marksform()  
#     return render(request,'add_sem3_marks.html',{'form':form,'student':students}) 

# def sem3_history(request):
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     print(username)
#     value=username.first()
#     print(value)
#     students = Student.objects.filter(user=value.id)
#     dep = sem3_marks.objects.all().order_by('sem3_id') 
#     return render(request,"sem3_history.html",{'dep':dep,'students':students}) 



# def store_sem4_marks(request):  
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     value=username.first()
#     students = Student.objects.filter(user=value.id)
    
#     # theory= theory_internal_component.objects.all()
#     # value= theory.first()
#     # th = theory_internal_component.filter()

#     if request.method == "POST":  
#         form = sem4_marksform(request.POST)  
#         try:
#             sem=sem4_marks.objects.get(sem4_id=request.POST.get('sem4_id',False))
#         except sem4_marks.DoesNotExist:
#             sem=None
#         if sem:
#             messages.warning(request," Id Already Exists")
#             return HttpResponseRedirect(request.path_info)
#         else:   
#             if form.is_valid():
#                 try:  
#                     form.save()
#                     messages.success(request,"Data Stored Sucessfully")  
#                     return redirect('/sem4_history')  
#                 except:  
#                     pass    
#     else:  
#         form = sem4_marksform()  
#     return render(request,'add_sem4_marks.html',{'form':form,'student':students}) 

# def sem4_history(request):
#     username=CustomUser.objects.filter(username=request.session['username']) 
#     print(username)
#     value=username.first()
#     print(value)
#     students = Student.objects.filter(user=value.id)
#     dep = sem4_marks.objects.all().order_by('sem4_id') 
#     return render(request,"sem4_history.html",{'dep':dep,'students':students}) 


#**********************   Sem 1  ***********************
def store_com(request):  
    username=CustomUser.objects.filter(username=request.session['username']) 
    value=username.first()
    students = Student.objects.filter(user=value.id)
    if request.method == "POST":  
        form = com_form(request.POST)  
        try:
           internal = form.save(commit = False) 
                     
           total = internal.c1 + internal.c2 + internal.c3 + internal.c4 

           internal.total = total


           total1 = internal.c5 + internal.c6+ total
           internal.total1 = total1

           #per1  = total1*100/800

           #internal.per1 = per1

        #    external = form.save(commit = False) 
        #    total1 = total + external.c5
        #    external.total1 = total1

           internal.save()
           cou=com_mst.objects.get(com_id=request.POST.get('com_id',False))
        except com_mst.DoesNotExist:
            cou=None
        if cou:
            messages.warning(request,"Comonent id Already Exists")
            return HttpResponseRedirect(request.path_info)
        else:   
            if form.is_valid():
                try:  
                    form.save()
                    print("Hello Course")
                    messages.success(request,"Data Stored Sucessfully")  
                    print("Hello message course")
                    return redirect('showcom/')  
                except:  
                    pass  
    else:  
        form = com_form()  
    return render(request,'add_com.html',{'students':students,'form':form}) 






def show_com(request):
    cour = com_mst.objects.all().order_by('com_id')  
  #  spi = com_mst.objects.all().order_by('com_id')  
    sum=  com_mst.objects.aggregate(Sum('total1'))

    per =  com_mst.objects.aggregate(Avg('total1'))

   # per  = Avg('sum1')

    #per = sum1 * 100 / 600

    # v1 = sum1.get('key1',None)

    # context = {
    #     'v1':v1,
    # }


    summ = list(sum.values())[0]


    print(summ)


    # summ = [item for item in sum1]

    # con = {'summ':summ}

    

    # Now result_list contains all the values from the loop
   #summ = {'result_list': result_list}
    #per = sum1 * 100 / 800

    # print(sum)
    # print(per)

   # spi = com_mst.objects.aggregate(Avg('total1')) 

    
    # if per>85. and per<100:
    #     spi = print(10)
    # else :
    #     spi = print('fail')

    paginator = Paginator(cour, 4)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    return render(request,"show_com.html",{'sum':sum,'cour':pages,'per':per}) 


def delete_com(request,com_id):  
    com = com_mst.objects.get(com_id=com_id)  
    com.delete()  
    return redirect("/showcom")
    

#**********************   Sem 2  ***********************

def store_com_sem2(request):  
    username=CustomUser.objects.filter(username=request.session['username']) 
    value=username.first()
    students = Student.objects.filter(user=value.id)
    if request.method == "POST":  
        form = sem2_com_form(request.POST)  
        try:
           internal = form.save(commit = False) 
                     
           total = internal.c1 + internal.c2 + internal.c3 + internal.c4 

           internal.total = total


           total1 = internal.c5 + internal.c6+ total
           internal.total1 = total1

           per1  = total1*100/800

           internal.per1 = per1

        #    external = form.save(commit = False) 
        #    total1 = total + external.c5
        #    external.total1 = total1

           internal.save()
           cou=com_mst1.objects.get(com_id=request.POST.get('com_id',False))
        except com_mst1.DoesNotExist:
            cou=None
        if cou:
            messages.warning(request,"Comonent id Already Exists")
            return HttpResponseRedirect(request.path_info)
        else:   
            if form.is_valid():
                try:  
                    form.save()
                    print("Hello Course")
                    messages.success(request,"Data Stored Sucessfully")  
                    print("Hello message course")
                    return redirect('showcom1/')  
                except:  
                    pass  
    else:  
        form = sem2_com_form()  
    return render(request,'add_com_sem2.html',{'students':students,'form':form}) 



def show_com_sem2(request):
    cour = com_mst1.objects.all().order_by('com_id')  
  #  spi = com_mst.objects.all().order_by('com_id')  
    sum=  com_mst1.objects.aggregate(Sum('total1'))

    per =  com_mst1.objects.aggregate(Avg('total1'))

    summ = list(sum.values())[0]


    print(summ)

    #per = sum * 100 / 800

    # print(sum)
    # print(per)

   # spi = com_mst.objects.aggregate(Avg('total1')) 

    
    # if per>85. and per<100:
    #     spi = print(10)
    # else :
    #     spi = print('fail')

    paginator = Paginator(cour, 4)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    return render(request,"show_com_sem2.html",{'cour':pages,'sum':sum,'per':per}) 


def delete_com_sem2(request,com_id):  
    com = com_mst1.objects.get(com_id=com_id)  
    com.delete()  
    return redirect("/showcom1")




#**********************   Sem 3  ***********************

def store_com_sem3(request):  
    username=CustomUser.objects.filter(username=request.session['username']) 
    value=username.first()
    students = Student.objects.filter(user=value.id)
    if request.method == "POST":  
        form = sem3_com_form(request.POST)  
        try:
           internal = form.save(commit = False) 
                     
           total = internal.c1 + internal.c2 + internal.c3 + internal.c4 

           internal.total = total


           total1 = internal.c5 + internal.c6+ total
           internal.total1 = total1

           per1  = total1*100/800

           internal.per1 = per1

        #    external = form.save(commit = False) 
        #    total1 = total + external.c5
        #    external.total1 = total1

           internal.save()
           cou=com_mst2.objects.get(com_id=request.POST.get('com_id',False))
        except com_mst2.DoesNotExist:
            cou=None
        if cou:
            messages.warning(request,"Comonent id Already Exists")
            return HttpResponseRedirect(request.path_info)
        else:   
            if form.is_valid():
                try:  
                    form.save()
                    print("Hello Course")
                    messages.success(request,"Data Stored Sucessfully")  
                    print("Hello message course")
                    return redirect('showcom2/')  
                except:  
                    pass  
    else:  
        form = sem2_com_form()  
    return render(request,'add_com_sem3.html',{'students':students,'form':form}) 



def show_com_sem3(request):
    cour = com_mst2.objects.all().order_by('com_id')  
  #  spi = com_mst.objects.all().order_by('com_id')  
    sum=  com_mst2.objects.aggregate(Sum('total1'))

    per =  com_mst2.objects.aggregate(Avg('total1'))

     

    #per = sum * 100 / 800

    # print(sum)
    # print(per)

   # spi = com_mst.objects.aggregate(Avg('total1')) 

    
    # if per>85. and per<100:
    #     spi = print(10)
    # else :
    #     spi = print('fail')

    paginator = Paginator(cour, 4)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    return render(request,"show_com_sem3.html",{'cour':pages,'sum':sum,'per':per}) 


def delete_com_sem3(request,com_id):  
    com = com_mst2.objects.get(com_id=com_id)  
    com.delete()  
    return redirect("/showcom2")




#**********************   Sem 4  ***********************

def store_com_sem4(request):  
    username=CustomUser.objects.filter(username=request.session['username']) 
    value=username.first()
    students = Student.objects.filter(user=value.id)
    if request.method == "POST":  
        form = sem4_com_form(request.POST)  
        try:
           internal = form.save(commit = False) 
                     
           total = internal.c1 + internal.c2 + internal.c3 + internal.c4 

           internal.total = total


           total1 = internal.c5 +  internal.c6+total
           internal.total1 = total1

           per1  = total1*100/800

           internal.per1 = per1

        #    external = form.save(commit = False) 
        #    total1 = total + external.c5
        #    external.total1 = total1

           internal.save()
           cou=com_mst3.objects.get(com_id=request.POST.get('com_id',False))
        except com_mst3.DoesNotExist:
            cou=None
        if cou:
            messages.warning(request,"Comonent id Already Exists")
            return HttpResponseRedirect(request.path_info)
        else:   
            if form.is_valid():
                try:  
                    form.save()
                    print("Hello Course")
                    messages.success(request,"Data Stored Sucessfully")  
                    print("Hello message course")
                    return redirect('showcom3/')  
                except:  
                    pass  
    else:  
        form = sem4_com_form()  
    return render(request,'add_com_sem4.html',{'students':students,'form':form}) 



def show_com_sem4(request):
    cour = com_mst3.objects.all().order_by('com_id')  
  #  spi = com_mst.objects.all().order_by('com_id')  
    sum=  com_mst3.objects.aggregate(Sum('total1'))

    #per =  com_mst3.objects.aggregate(Avg('total1'))

     

  #  per = sum * 100 / 800

    # print(sum)
    # print(per)

   # spi = com_mst.objects.aggregate(Avg('total1')) 

    
    # if per>85 and per<100:
    #     spi = print(10)
    # else :
    #     spi = print('fail')

    paginator = Paginator(cour, 4)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    return render(request,"show_com_sem4.html",{'cour':pages,'sum':sum}) 


def delete_com_sem4(request,com_id):  
    com = com_mst3.objects.get(com_id=com_id)  
    com.delete()  
    return redirect("/showcom3")




def store_sub(request):  
    if request.method == "POST":  
        form = subject_form(request.POST)  
        try:
            dep=subject.objects.get(sub_id=request.POST.get('sub_id',False))
        except subject.DoesNotExist:
            dep=None
        if dep:
            messages.warning(request,"department Already Exists")
            return HttpResponseRedirect(request.path_info)
        else:   
            if form.is_valid():
                try:  
                    form.save()
                    messages.success(request,"Data Stored Sucessfully")  
                    return redirect('show_sub')  
                except:  
                    pass  
    else:  
        form = subject_form()  
    return render(request,'add_sub.html',{'form':form}) 


def show_sub(request):
    cour = subject.objects.all().order_by('sub_id')  
   
    paginator = Paginator(cour, 6)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    return render(request,"show_sub.html",{'cour':pages}) 







def show_sem1(request):
    username=CustomUser.objects.filter(username=request.session['username']) 
    print(username)
    value=username.first()
   
    print(value)
    students = Student.objects.filter(user=value.id)
  
    # return render(request,"show_provisional_request.html",{'students':students})
    stu_id=students.first()
    print(stu_id)
    pid = Student.objects.filter(sid=stu_id.sid).first()
    # print(pid)
    #pro = Final_result.objects.filter(sid=pid)

    #return render(request,"show_final_request.html",{'pro':pro,'students':students}) 

    #stu = Student.objects.all()   
    cour = com_mst.objects.filter(sid=pid)
    #cour = com_mst.objects.all().order_by('com_id')  
  #  spi = com_mst.objects.all().order_by('com_id')  
    sum=  com_mst.objects.filter(sid=pid).aggregate(Sum('total1'))

    #per =  com_mst.objects.filter(sid=pid).aggregate(Avg('total1'))


    summ = list(sum.values())[0]


    per = summ*100/800

    if per >90 and per<100:
        spi = 10
    elif per >80 and per<90:
         spi = 9
    else:
        spi = 0

    print(per)

    print(summ)


    # summ = [item for item in sum]

    # con = {'summ':summ}
    #per =sum * 100 / 800
    ## print(sum)
    # print(per)

   # spi = com_mst.objects.aggregate(Avg('total1')) 

    
    # if per>85. and per<100:
    #     spi = print(10)
    # else :
    #     spi = print('fail')

    paginator = Paginator(cour, 7)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    return render(request,"sem1_history.html",{'stu':students,'cour':pages,'sum':sum,'per':per,'spi':spi}) 



def show_sem2(request):
    username=CustomUser.objects.filter(username=request.session['username']) 
    print(username)
    value=username.first()
   
    print(value)
    students = Student.objects.filter(user=value.id)
  
    # return render(request,"show_provisional_request.html",{'students':students})
    stu_id=students.first()
    print(stu_id)
    pid = Student.objects.filter(sid=stu_id.sid).first()
    # print(pid)
    #pro = Final_result.objects.filter(sid=pid)

    #return render(request,"show_final_request.html",{'pro':pro,'students':students}) 

    #stu = Student.objects.all()   
    cour = com_mst1.objects.filter(sid=pid)
    #cour = com_mst.objects.all().order_by('com_id')  
  #  spi = com_mst.objects.all().order_by('com_id')  
    sum=  com_mst1.objects.filter(sid=pid).aggregate(Sum('total1'))

    #per =  com_mst.objects.filter(sid=pid).aggregate(Avg('total1'))


    summ = list(sum.values())[0]


    per = summ*100/800

    # if per >90 and per<100:
    #     spi = 10
    # elif per >80 and per<90:
    #      spi = 9
    # else:
    #     spi = 0

    print(per)

    print(summ)


    # summ = [item for item in sum]

    # con = {'summ':summ}
    #per =sum * 100 / 800
    ## print(sum)
    # print(per)

   # spi = com_mst.objects.aggregate(Avg('total1')) 

    
    # if per>85. and per<100:
    #     spi = print(10)
    # else :
    #     spi = print('fail')

    paginator = Paginator(cour, 7)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    return render(request,"sem2_history.html",{'stu':students,'cour':pages,'sum':sum,'per':per}) 



def show_sem3(request):
    username=CustomUser.objects.filter(username=request.session['username']) 
    print(username)
    value=username.first()
   
    print(value)
    students = Student.objects.filter(user=value.id)
  
    # return render(request,"show_provisional_request.html",{'students':students})
    stu_id=students.first()
    print(stu_id)
    pid = Student.objects.filter(sid=stu_id.sid).first()
    # print(pid)
    #pro = Final_result.objects.filter(sid=pid)

    #return render(request,"show_final_request.html",{'pro':pro,'students':students}) 

    #stu = Student.objects.all()   
    cour = com_mst2.objects.filter(sid=pid)
    #cour = com_mst.objects.all().order_by('com_id')  
  #  spi = com_mst.objects.all().order_by('com_id')  
    sum=  com_mst2.objects.filter(sid=pid).aggregate(Sum('total1'))

    #per =  com_mst.objects.filter(sid=pid).aggregate(Avg('total1'))


    summ = list(sum.values())[0]


    per = summ*100/800

    # if per >90 and per<100:
    #     spi = 10
    # elif per >80 and per<90:
    #      spi = 9
    # else:
    #     spi = 0

    print(per)

    print(summ)


    # summ = [item for item in sum]

    # con = {'summ':summ}
    #per =sum * 100 / 800
    ## print(sum)
    # print(per)

   # spi = com_mst.objects.aggregate(Avg('total1')) 

    
    # if per>85. and per<100:
    #     spi = print(10)
    # else :
    #     spi = print('fail')

    paginator = Paginator(cour, 7)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    return render(request,"sem3_history.html",{'stu':students,'cour':pages,'sum':sum,'per':per}) 




def show_sem4(request):
    username=CustomUser.objects.filter(username=request.session['username']) 
    print(username)
    value=username.first()
   
    print(value)
    students = Student.objects.filter(user=value.id)
  
    # return render(request,"show_provisional_request.html",{'students':students})
    stu_id=students.first()
    print(stu_id)
    pid = Student.objects.filter(sid=stu_id.sid).first()
    # print(pid)
    #pro = Final_result.objects.filter(sid=pid)

    #return render(request,"show_final_request.html",{'pro':pro,'students':students}) 

    #stu = Student.objects.all()   
    cour = com_mst3.objects.filter(sid=pid)
    #cour = com_mst.objects.all().order_by('com_id')  
  #  spi = com_mst.objects.all().order_by('com_id')  
    sum=  com_mst3.objects.filter(sid=pid).aggregate(Sum('total1'))

    #per =  com_mst.objects.filter(sid=pid).aggregate(Avg('total1'))


    summ = list(sum.values())[0]


    per = summ*100/800

    if per >90 and per<100:
        spi = 10
    elif per >80 and per<90:
         spi = 9
    else:
        spi = 0

    print(per)

    print(summ)


    # summ = [item for item in sum]

    # con = {'summ':summ}
    #per =sum * 100 / 800
    ## print(sum)
    # print(per)

   # spi = com_mst.objects.aggregate(Avg('total1')) 

    
    # if per>85. and per<100:
    #     spi = print(10)
    # else :
    #     spi = print('fail')

    paginator = Paginator(cour, 7)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    return render(request,"sem4_history.html",{'stu':students,'cour':pages,'sum':sum,'per':per,'spi':spi}) 






















def final_show_sem1(request):
    username=CustomUser.objects.filter(username=request.session['username']) 
    print(username)
    value=username.first()
   
    print(value)
    students = Student.objects.filter(user=value.id)
  
    # return render(request,"show_provisional_request.html",{'students':students})
    stu_id=students.first()
    print(stu_id)
    pid = Student.objects.filter(sid=stu_id.sid).first()
    # print(pid)
    #pro = Final_result.objects.filter(sid=pid)

    #return render(request,"show_final_request.html",{'pro':pro,'students':students}) 

    #stu = Student.objects.all()   
    cour = com_mst.objects.filter(sid=pid)
    #cour = com_mst.objects.all().order_by('com_id')  
  #  spi = com_mst.objects.all().order_by('com_id')  
    sum=  com_mst.objects.filter(sid=pid).aggregate(Sum('total1'))

    #per =  com_mst.objects.filter(sid=pid).aggregate(Avg('total1'))


    summ = list(sum.values())[0]


    per = summ*100/800

    if per >95 and per<100:
        spi = 10
    elif per >90 and per<96:
        spi = 9.5
    elif per >85 and per<91:
         spi = 9
    elif per >80 and per<86:
         spi = 8.5
    elif per >75 and per<81:
         spi = 8
    elif per >70 and per<76:
         spi = 7.5
    elif per >65 and per<71:
         spi = 7
    elif per >60 and per<66:
         spi = 6.5
    elif per >55 and per<61:
         spi = 6
    elif per >50 and per<56:
         spi = 5.5
    elif per >45 and per<51:
         spi = 5
    elif per >40 and per<46:
         spi = 4.5
    else:
        spi = 0


    

    if per >95 and per<100:
        ppi = 10
    elif per >90 and per<96:
        ppi = 9.5
    elif per >85 and per<91:
        ppi = 9
    elif per >80 and per<86:
         ppi = 8.5
    elif per >75 and per<81:
         ppi = 8
    elif per >70 and per<76:
        ppi = 7.5
    elif per >65 and per<71:
         ppi = 7
    elif per >60 and per<66:
         ppi = 6.5
    elif per >55 and per<61:
        ppi = 6
    elif per >50 and per<56:
        ppi = 5.5
    elif per >45 and per<51:
       ppi = 5
    elif per >40 and per<46:
        ppi= 4.5
    else:
       ppi = 0



    
    if spi>6.99 and spi<10.1:
        Class = "First Class With Distinction"
    elif spi>6 and spi<6.99:
        Class = "First Class"
    elif spi>5.5 and spi<6:
        Class = "Higher Second Class"
    elif spi>5 and spi<5.51:
        Class = "Second Class"
    elif spi>4 and spi<5.1:
        Class = "Pass Class"
    else:
        Class = "Fail"



    if Class=="Fail":
        result = "FAIL"
    else:
        result = "PASS"
    


    print(per)

    print(summ)


    # summ = [item for item in sum]

    # con = {'summ':summ}
    #per =sum * 100 / 800
    ## print(sum)
    # print(per)

   # spi = com_mst.objects.aggregate(Avg('total1')) 

    
    # if per>85. and per<100:
    #     spi = print(10)
    # else :
    #     spi = print('fail')

    paginator = Paginator(cour, 7)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    return render(request,"final_sem1.html",{'stu':students,'cour':pages,'sum':sum,'per':per,'spi':spi,'Class':Class,'result': result,'ppi':ppi}) 



def final_show_sem2(request):
    username=CustomUser.objects.filter(username=request.session['username']) 
    print(username)
    value=username.first()
   
    print(value)
    students = Student.objects.filter(user=value.id)
  
    # return render(request,"show_provisional_request.html",{'students':students})
    stu_id=students.first()
    print(stu_id)
    pid = Student.objects.filter(sid=stu_id.sid).first()
    # print(pid)
    #pro = Final_result.objects.filter(sid=pid)

    #return render(request,"show_final_request.html",{'pro':pro,'students':students}) 

    #stu = Student.objects.all()   
    cour = com_mst1.objects.filter(sid=pid)
    #cour = com_mst.objects.all().order_by('com_id')  
  #  spi = com_mst.objects.all().order_by('com_id')  
    sum=  com_mst1.objects.filter(sid=pid).aggregate(Sum('total1'))

    #per =  com_mst.objects.filter(sid=pid).aggregate(Avg('total1'))


    summ = list(sum.values())[0]


    per = summ*100/800

    if per >95 and per<100:
        spi = 10
    elif per >90 and per<96:
        spi = 9.5
    elif per >85 and per<91:
         spi = 9
    elif per >80 and per<86:
         spi = 8.5
    elif per >75 and per<81:
         spi = 8
    elif per >70 and per<76:
         spi = 7.5
    elif per >65 and per<71:
         spi = 7
    elif per >60 and per<66:
         spi = 6.5
    elif per >55 and per<61:
         spi = 6
    elif per >50 and per<56:
         spi = 5.5
    elif per >45 and per<51:
         spi = 5
    elif per >40 and per<46:
         spi = 4.5
    else:
        spi = 0


    

    if per >95 and per<100:
        ppi = 10
    elif per >90 and per<96:
        ppi = 9.5
    elif per >85 and per<91:
        ppi = 9
    elif per >80 and per<86:
         ppi = 8.5
    elif per >75 and per<81:
         ppi = 8
    elif per >70 and per<76:
        ppi = 7.5
    elif per >65 and per<71:
         ppi = 7
    elif per >60 and per<66:
         ppi = 6.5
    elif per >55 and per<61:
        ppi = 6
    elif per >50 and per<56:
        ppi = 5.5
    elif per >45 and per<51:
       ppi = 5
    elif per >40 and per<46:
        ppi= 4.5
    else:
       ppi = 0



    
    if spi>6.99 and spi<10.1:
        Class = "First Class With Distinction"
    elif spi>6 and spi<6.99:
        Class = "First Class"
    elif spi>5.5 and spi<6:
        Class = "Higher Second Class"
    elif spi>5 and spi<5.51:
        Class = "Second Class"
    elif spi>4 and spi<5.1:
        Class = "Pass Class"
    else:
        Class = "Fail"


    if Class=="Fail":
        result = "FAIL"
    else:
        result = "PASS"
    


    print(per)

    print(summ)


    # summ = [item for item in sum]

    # con = {'summ':summ}
    #per =sum * 100 / 800
    ## print(sum)
    # print(per)

   # spi = com_mst.objects.aggregate(Avg('total1')) 

    
    # if per>85. and per<100:
    #     spi = print(10)
    # else :
    #     spi = print('fail')

    paginator = Paginator(cour, 7)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    return render(request,"final_sem2.html",{'stu':students,'cour':pages,'sum':sum,'per':per,'spi':spi,'Class':Class,'result': result,'ppi':ppi}) 



def final_show_sem3(request):
    username=CustomUser.objects.filter(username=request.session['username']) 
    print(username)
    value=username.first()
   
    print(value)
    students = Student.objects.filter(user=value.id)
  
    # return render(request,"show_provisional_request.html",{'students':students})
    stu_id=students.first()
    print(stu_id)
    pid = Student.objects.filter(sid=stu_id.sid).first()
    # print(pid)
    #pro = Final_result.objects.filter(sid=pid)

    #return render(request,"show_final_request.html",{'pro':pro,'students':students}) 

    #stu = Student.objects.all()   
    cour = com_mst2.objects.filter(sid=pid)
    #cour = com_mst.objects.all().order_by('com_id')  
  #  spi = com_mst.objects.all().order_by('com_id')  
    sum=  com_mst2.objects.filter(sid=pid).aggregate(Sum('total1'))

    #per =  com_mst.objects.filter(sid=pid).aggregate(Avg('total1'))


    summ = list(sum.values())[0]


    per = summ*100/800

    if per >95 and per<100:
        spi = 10
    elif per >90 and per<96:
        spi = 9.5
    elif per >85 and per<91:
         spi = 9
    elif per >80 and per<86:
         spi = 8.5
    elif per >75 and per<81:
         spi = 8
    elif per >70 and per<76:
         spi = 7.5
    elif per >65 and per<71:
         spi = 7
    elif per >60 and per<66:
         spi = 6.5
    elif per >55 and per<61:
         spi = 6
    elif per >50 and per<56:
         spi = 5.5
    elif per >45 and per<51:
         spi = 5
    elif per >40 and per<46:
         spi = 4.5
    else:
        spi = 0


    

    if per >95 and per<100:
        ppi = 10
    elif per >90 and per<96:
        ppi = 9.5
    elif per >85 and per<91:
        ppi = 9
    elif per >80 and per<86:
         ppi = 8.5
    elif per >75 and per<81:
         ppi = 8
    elif per >70 and per<76:
        ppi = 7.5
    elif per >65 and per<71:
         ppi = 7
    elif per >60 and per<66:
         ppi = 6.5
    elif per >55 and per<61:
        ppi = 6
    elif per >50 and per<56:
        ppi = 5.5
    elif per >45 and per<51:
       ppi = 5
    elif per >40 and per<46:
        ppi= 4.5
    else:
       ppi = 0



    
    if spi>6.99 and spi<10.1:
        Class = "First Class With Distinction"
    elif spi>6 and spi<6.99:
        Class = "First Class"
    elif spi>5.5 and spi<6:
        Class = "Higher Second Class"
    elif spi>5 and spi<5.51:
        Class = "Second Class"
    elif spi>4 and spi<5.1:
        Class = "Pass Class"
    else:
        Class = "Fail"


    if Class=="Fail":
        result = "FAIL"
    else:
        result = "PASS"
    


    print(per)

    print(summ)



    # summ = [item for item in sum]

    # con = {'summ':summ}
    #per =sum * 100 / 800
    ## print(sum)
    # print(per)

   # spi = com_mst.objects.aggregate(Avg('total1')) 

    
    # if per>85. and per<100:
    #     spi = print(10)
    # else :
    #     spi = print('fail')

    paginator = Paginator(cour, 7)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    return render(request,"final_sem3.html",{'stu':students,'cour':pages,'sum':sum,'per':per,'spi':spi,'Class':Class,'result': result,'ppi':ppi}) 




def final_show_sem4(request):
    username=CustomUser.objects.filter(username=request.session['username']) 
    print(username)
    value=username.first()
   
    print(value)
    students = Student.objects.filter(user=value.id)
  
    # return render(request,"show_provisional_request.html",{'students':students})
    stu_id=students.first()
    print(stu_id)
    pid = Student.objects.filter(sid=stu_id.sid).first()
    # print(pid)
    #pro = Final_result.objects.filter(sid=pid)

    #return render(request,"show_final_request.html",{'pro':pro,'students':students}) 

    #stu = Student.objects.all()   
    cour = com_mst3.objects.filter(sid=pid)
    #cour = com_mst.objects.all().order_by('com_id')  
  #  spi = com_mst.objects.all().order_by('com_id')  
    sum=  com_mst3.objects.filter(sid=pid).aggregate(Sum('total1'))

    #per =  com_mst.objects.filter(sid=pid).aggregate(Avg('total1'))


    summ = list(sum.values())[0]


    per = summ*100/800

    if per >95 and per<100:
        spi = 10
    elif per >90 and per<96:
        spi = 9.5
    elif per >85 and per<91:
         spi = 9
    elif per >80 and per<86:
         spi = 8.5
    elif per >75 and per<81:
         spi = 8
    elif per >70 and per<76:
         spi = 7.5
    elif per >65 and per<71:
         spi = 7
    elif per >60 and per<66:
         spi = 6.5
    elif per >55 and per<61:
         spi = 6
    elif per >50 and per<56:
         spi = 5.5
    elif per >45 and per<51:
         spi = 5
    elif per >40 and per<46:
         spi = 4.5
    else:
        spi = 0


    

    if per >95 and per<100:
        ppi = 10
    elif per >90 and per<96:
        ppi = 9.5
    elif per >85 and per<91:
        ppi = 9
    elif per >80 and per<86:
         ppi = 8.5
    elif per >75 and per<81:
         ppi = 8
    elif per >70 and per<76:
        ppi = 7.5
    elif per >65 and per<71:
         ppi = 7
    elif per >60 and per<66:
         ppi = 6.5
    elif per >55 and per<61:
        ppi = 6
    elif per >50 and per<56:
        ppi = 5.5
    elif per >45 and per<51:
       ppi = 5
    elif per >40 and per<46:
        ppi= 4.5
    else:
       ppi = 0



    
    if spi>6.99 and spi<10.1:
        Class = "First Class With Distinction"
    elif spi>6 and spi<6.99:
        Class = "First Class"
    elif spi>5.5 and spi<6:
        Class = "Higher Second Class"
    elif spi>5 and spi<5.51:
        Class = "Second Class"
    elif spi>4 and spi<5.1:
        Class = "Pass Class"
    else:
        Class = "Fail"





    print(per)

    print(summ)
    print(spi)

    print(Class)

    # print(ppi)


    # summ = [item for item in sum]

    # con = {'summ':summ}
    #per =sum * 100 / 800
    ## print(sum)
    # print(per)

   # spi = com_mst.objects.aggregate(Avg('total1')) 

    
    # if per>85. and per<100:
    #     spi = print(10)
    # else :
    #     spi = print('fail')

    if Class=="Fail":
        result = "FAIL"
    else:
        result = "PASS"

    paginator = Paginator(cour, 7)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1     
    try:
        pages = paginator.page(page)
    except(Paginator.EmptyPage , Paginator.InvalidPage):
        pages = paginator.page(paginator.num_pages) 
    return render(request,"final_sem4.html",{'stu':students,'cour':pages,'sum':sum,'per':per,'spi':spi,'ppi':ppi,'Class':Class,'result':result}) 






def delete_sub(request,sub_id):  
    com = subject.objects.get(sub_id=sub_id)  
    com.delete()  
    return redirect("/showsub")




#*****************  Home Slider Image ****************** 


def slider_image_view(request):
    if request.method == 'POST':
        form = slider1Form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/admin_display_slider_images')
            
    else:
        form =slider1Form()
    return render(request,'home_slider_image_form.html', {'form': form })

def display_slider_images(request):
    if request.method == 'GET':
       slider = slider1.objects.all()
    return render(request,'home.html',{'slider': slider})

def admin_display_slider_images(request):
    if request.method == 'GET':
       slider = slider1.objects.all()
    return render(request,'display_home_slider_image.html',{'slider': slider})

def destroy(request, id):  
    slider =  slider1.objects.get(id=id)  
    slider.delete()  
    messages.success(request,"Delete Image successfully")
    return redirect("/admin_display_slider_images")














def slider_image_view1(request):
    if request.method == 'POST':
        form = slider2Form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/admin_display_slider_images1')
        else:
            print("hii")
            
    else:
        form =slider2Form()
    return render(request,'home_slider_image_form1.html', {'form': form })

def display_slider_images1(request):
    if request.method == 'GET':
       slider1 = slider2.objects.all()
    return render(request,'home1.html',{'slider1': slider1})

def admin_display_slider_images1(request):
    if request.method == 'GET':
       slider1 = slider2.objects.all()
    return render(request,'display_home_slider_image1.html',{'slider1': slider1})

def destroy1(request, id):  
    slider1 =  slider2.objects.get(id=id)  
    slider1.delete()  
    messages.success(request,"Delete Image successfully")
    return redirect("/admin_display_slider_images1")


def slider2_edit(request, id):  
    slider1 = slider2.objects.get(id=id)  
    return render(request,'edit_image.html', {'slider1':slider1})  

def slider2_update(request, id):  
    slider1 = slider2.objects.get(id=id)  
    form = slider2Form(request.POST, request.FILES ,instance = slider1)  
    if form.is_valid():  
        form.save()  
        return redirect("/admin_display_slider_images1") 

    
     
    return render(request, 'edit_image.html', {'slider1': slider1}) 