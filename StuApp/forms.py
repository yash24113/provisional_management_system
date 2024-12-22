from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]
        

class StudentForm(forms.ModelForm): 
    class Meta:  
        model = Student 
        fields = ["sid","sname","enrollment","did"] 

class EditStudentForm(forms.ModelForm): 
    class Meta:  
        model = Student 
        fields = ["sid","sname","enrollment","did"]
        widgets = {
            'sid': forms.TextInput(attrs={'readonly': 'readonly'}),
        }        
    

class DepartmentForm(forms.ModelForm):  
    class Meta:  
        model = Department  
        fields = "__all__"

class EditDepartmentForm(forms.ModelForm):  
    class Meta:  
        model = Department  
        fields = "__all__"
        widgets = {
            'did': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

class CourseForm(forms.ModelForm):  
    class Meta:  
        model = Course  
        fields = "__all__"

class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        widgets = {
            'cid': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


class SemesterForm(forms.ModelForm):  
    class Meta:  
        model = Semester 
        # fields = ["sem_id","sem_name","sid"] 
        # exclude = "__all__"
        # fields = "__all__"
        fields = ["sem_id","sem_name","cid"]

class EditSemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = "__all__"
        widgets = {
            'sem_id': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


class Provisional_resultForm(forms.ModelForm): 
    class Meta:  
        model =  Provisional_result
        fields = ["pro_id","pro_sem","reason","sid"] 

class Bonafide_CertificateForm(forms.ModelForm): 
    class Meta:  
        model =  Bonafide_Certificate
        fields = ["bono_id","reason","sid"] 






class Final_resultForm(forms.ModelForm): 
    class Meta:  
        model =  Final_result
        fields = ["final_id","semester","sid"] 


# class marksForm(forms.ModelForm): 
#     class Meta:  
#         model =  marks
#         fields = ["m_id","marks","sid"] 

# # subject like 150 as DWDM
# class thoery_internal_marksForm(forms.ModelForm):
#     class Meta:
#         model = theory_internal_marks
#         fields = ["i_id1","unit_test","practical_test","attendance","oneday","sid"]

# class theory_external_marksForm(forms.ModelForm):
#     class Meta:
#         model = theory_external_marks
#         fields = ["e_id1","paper","sid"]

# class practical_marksForm(forms.ModelForm):
#     class Meta:
#         model = practical_marks
#         fields = ["p_id1","paper","viva","sid"]




# # subject like 100 as Django
# class project_internal_marksForm(forms.ModelForm):
#     class Meta:
#         model = project_internal_marks
#         fields = ["i_id2","review1","review2","review3","attendance","sid"]

# class project_external_marksForm(forms.ModelForm):
#     class Meta:
#         model = project_external_marks
#         fields = ["e_id2","project","sid"]


# # Master Table of Marks
# class master_markform(forms.ModelForm):
#     class Meta:
#         model = master_marks1
#         fields = ["i_id1","i_id2","e_id1","e_id2","p_id1","sid"]


class subject_typeform(forms.ModelForm):
    class Meta:
        model = subject_type
        fields = ["type_id","subject_type"]

class com_form(forms.ModelForm):
    class Meta:
        model = com_mst
        fields = ["sid","com_id","type_id","cid","c1","c2","c3","c4","c5","c6"]
        widgets = {
             'total' : forms.HiddenInput(),
             
        }
        widgets = {
              'total1' : forms.HiddenInput(),
        }

class Editsem1Form(forms.ModelForm):
    class Meta:
        model = com_mst
        fields = ["sid","com_id","type_id","cid","c1","c2","c3","c4","c5","c6"]
        widgets = {
             'total' : forms.HiddenInput(),
             
        }
        widgets = {
              'total1' : forms.HiddenInput(),
        }

class sem2_com_form(forms.ModelForm):
    class Meta:
        model = com_mst1
        fields = ["sid","com_id","type_id","cid","c1","c2","c3","c4","c5","c6"]
        widgets = {
             'total' : forms.HiddenInput(),
             
        }
        widgets = {
              'total1' : forms.HiddenInput(),
        }

class sem3_com_form(forms.ModelForm):
    class Meta:
        model = com_mst2
        fields = ["sid","com_id","type_id","cid","c1","c2","c3","c4","c5","c6"]
        widgets = {
             'total' : forms.HiddenInput(),
             
        }
        widgets = {
              'total1' : forms.HiddenInput(),
        }


class sem4_com_form(forms.ModelForm):
    class Meta:
        model = com_mst3
        fields = ["sid","com_id","type_id","cid","c1","c2","c3","c4","c5","c6"]
        widgets = {
             'total' : forms.HiddenInput(),
             
        }
        widgets = {
              'total1' : forms.HiddenInput(),
        }


class subject_form(forms.ModelForm):
    class Meta:
        model =  subject
        fields = ["sub_id","cid","com_id","sid"]

# class theory_internal_componentform(forms.ModelForm):
#     class Meta:
#         model = theory_internal_component
#         fields = ["iid1","unit_test","attendance","one_day","type_id","cid","sid"]
#         widgets = {
#             'total' : forms.HiddenInput(),
#         }

# class theory_external_componentform(forms.ModelForm):
#     class Meta:
#         model = theory_external_component
#         fields = ["eid1","university_exam","type_id","cid","sid"]

# class theory_practicle_internal_componentform(forms.ModelForm):
#     class Meta:
#         model =  theory_practicle_internal_component
#         fields = ["iid2","unit_test","practical_test","attendance","one_day","type_id","cid","sid"]

# class theory_practicle_external_componentform(forms.ModelForm):
#     class Meta:
#         model =  theory_practicle_external_component
#         fields = ["eid2","university_exam","practicle_exam","viva","type_id","cid","sid"]

# class practicle_internal_componentform(forms.ModelForm):
#     class Meta:
#         model = practicle_internal_component
#         fields = ["iid3","unit_test","attendance","capstone","type_id","cid","sid"]

# class practicle_external_componentform(forms.ModelForm):
#     class Meta:
#         model =  practicle_external_component
#         fields = ["eid3","practicle_exam","viva","type_id","cid","sid"]


# class project_internal_componentform(forms.ModelForm):
#     class Meta:
#         model = project_internal_component
#         fields = ["iid4","review1","review2","review3","attendance","type_id","cid","sid"]

# class project_external_componentform(forms.ModelForm):
#     class Meta:
#         model =  project_external_component
#         fields = ["eid4","project","type_id","cid","sid"]


# class subject_masterform(forms.ModelForm):
#     class Meta:
#         model = subject_master
#         fields = ["sm_id","cid","type_id"]


# class subject_marksform(forms.ModelForm):
#     class Meta:
#         model = subject_marks
#         fields = ["sub_mark_id","iid1","eid1","iid2","eid2","iid3","eid3","iid4","eid4","type_id","cid","sid"]

# class sem1_marksform(forms.ModelForm):
#     class Meta:
#         model =  sem1_marks
#         fields = ["sem1_id","iid1","eid1","iid2","eid2","iid3","eid3","iid4","eid4","type_id","cid","sid"]

# class sem2_marksform(forms.ModelForm):
#     class Meta:
#         model = sem2_marks
#         fields = ["sem2_id","iid1","eid1","iid2","eid2","iid3","eid3","iid4","eid4","type_id","cid","sid"]

# class sem3_marksform(forms.ModelForm):
#     class Meta:
#         model =  sem3_marks
#         fields = ["sem3_id","iid1","eid1","iid2","eid2","iid3","eid3","iid4","eid4","type_id","cid","sid"]

# class sem4_marksform(forms.ModelForm):
#     class Meta:
#         model =  sem4_marks
#         fields = ["sem4_id","iid1","eid1","iid2","eid2","iid3","eid3","iid4","eid4","type_id","cid","sid"]








class slider1Form(forms.ModelForm):  
    class Meta:  
        model = slider1
        fields = "__all__"  

class slider2Form(forms.ModelForm):  
    class Meta:  
        model = slider2
        fields = "__all__"  

class slider3Form(forms.ModelForm):  
    class Meta:  
        model = slider3
        fields = "__all__"  

class slider4Form(forms.ModelForm):  
    class Meta:  
        model = slider4
        fields = "__all__"  
