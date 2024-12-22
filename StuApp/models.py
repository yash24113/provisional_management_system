from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager 

class CustomUser(AbstractUser):
    #username=None
    username=models.CharField(unique=True,max_length=10,default='')
    #phone_no=models.IntegerField(unique=True,max_length=10,default='1')
    email=models.EmailField(unique=True)
    # enrollment = models.IntegerField(unique=True) 
   # USERNAME_FIELD='phone_no'
    REQUIRED_FIELDS=[]
    objects= UserManager()

class Department(models.Model):
    did=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        db_table='Department'
    def __str__(self):
        return self.name

class Course(models.Model):
    cid=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    did = models.ForeignKey(Department, on_delete=models.CASCADE,db_column='did')

    class Meta:
        db_table='Course'
    def __str__(self):
        return self.name
    
class Semester(models.Model):
    sem_id=models.AutoField(primary_key=True)
    sem_name = models.CharField(max_length=10)
   
    cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
    class Meta:
        db_table='Semester'
   
    def __str__(self):
        return self.sem_name
    # def __init__(self, sem_name):
    #     self.value = sem_name
    # def __str__(self, sem_name):
    #     return str(self.sem_name) 
  

class Student(models.Model):
    user = models.OneToOneField(CustomUser, db_column="user" ,on_delete=models.CASCADE)
    sid = models.AutoField( primary_key=True)
    sname = models.CharField(max_length=100) 
    enrollment = models.CharField(max_length=100,default='') 
    #cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
    did = models.ForeignKey(Department, on_delete=models.CASCADE,db_column='did',default='')
    #sem_id = models.ForeignKey(Semester, on_delete=models.CASCADE,db_column='sem_id',default=True)
    class Meta:  
        db_table = "student"
    def __str__(self):
        return self.user.username  # You can customize this as needed



class Provisional_result(models.Model):
    pro_id=models.AutoField(primary_key=True)
    pro_sem = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
   # user = models.OneToOneField(CustomUser, db_column="user" ,on_delete=models.CASCADE,default='')
    sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    
    class Meta:
        db_table='Provisional_result'
    # def __str__(self):
    #     return  self.user.username


class Bonafide_Certificate(models.Model):
    bono_id=models.AutoField(primary_key=True)
    
    reason = models.CharField(max_length=100)
   # user = models.OneToOneField(CustomUser, db_column="user" ,on_delete=models.CASCADE,default='')
    #cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
    sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    
    class Meta:
        db_table='Bonafide_Certificate'
    






class Final_result(models.Model):
    final_id=models.AutoField(primary_key=True)
    
    semester = models.IntegerField()
   # user = models.OneToOneField(CustomUser, db_column="user" ,on_delete=models.CASCADE,default='')
    #cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
    sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    
    class Meta:
        db_table='Final_result'


# class marks(models.Model):
#     m_id=models.AutoField(primary_key=True)
#     marks=models.CharField(max_length=3)
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
#     class Meta:
#         db_table='mark'

# # subject like DWDM   
# class theory_internal_marks(models.Model):
#     i_id1=models.AutoField(primary_key=True)
#     unit_test=models.CharField(max_length=2)
#     practical_test=models.CharField(max_length=2)
#     attendance=models.CharField(max_length=2)
#     oneday=models.CharField(max_length=2)
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
#     class Meta:
#         db_table='theory_internal_mark'


# # subject like Django  
# class project_internal_marks(models.Model):
#     i_id2=models.AutoField(primary_key=True)
#     review1 = models.CharField(max_length=2)
#     review2 = models.CharField(max_length=2)
#     review3 = models.CharField(max_length=2)
#     attendance=models.CharField(max_length=2)
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
#     class Meta:
#         db_table='project_internal_mark'


#  # subject like DWDM  theory paper   
# class theory_external_marks(models.Model):
#     e_id1=models.AutoField(primary_key=True)
#     paper=models.CharField(max_length=2)
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
#     class Meta:
#         db_table='theory_external_mark'
    

# # subject like Django final project
# class project_external_marks(models.Model):
#     e_id2=models.AutoField(primary_key=True)
#     project=models.CharField(max_length=2)
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
#     class Meta:
#         db_table='project_external_mark'

    
# # subject like DWDM practicle schema
# class practical_marks(models.Model):
#     p_id1=models.AutoField(primary_key=True)
#     paper=models.CharField(max_length=2)
#     viva=models.CharField(max_length=2)
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
#     class Meta:
#        db_table='practical_mark'

# # Practicle paper is not take in project subject like djago


# class master_marks1(models.Model):
#     m_id=models.AutoField(primary_key=True)
#     i_id1=models.ForeignKey(theory_internal_marks, on_delete=models.CASCADE,db_column='i_id1',default='')
#     i_id2=models.ForeignKey(project_internal_marks, on_delete=models.CASCADE,db_column='i_id2',default='')
#     e_id1=models.ForeignKey(theory_external_marks, on_delete=models.CASCADE,db_column='e_id1',default='')
#     e_id2=models.ForeignKey(project_external_marks, on_delete=models.CASCADE,db_column='e_id2',default='')
#     p_id1=models.ForeignKey(practical_marks, on_delete=models.CASCADE,db_column='p_id1',default='')
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
#     class Meta:
#        db_table='master_mark1'





    


# **************** Only Theory Subject *********************
# class theory_internal_component(models.Model):
#     iid1= models.AutoField(primary_key=True)
#     unit_test=models.IntegerField()
#     attendance=models.IntegerField()
#     one_day=models.IntegerField()
#     total = models.IntegerField(default=0)
#     type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
#     cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    
#     class Meta:
#         db_table='theory_internal_component'
    
#     # def __str__(self):
#     #     return self.iid1

# class theory_external_component(models.Model):
#     eid1= models.AutoField(primary_key=True)
#     university_exam=models.IntegerField()
#     type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
#     cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    
#     class Meta:
#         db_table='theory_external_component'



# # **************** Theory and Praticle Subject *********************

# class theory_practicle_internal_component(models.Model):
#     iid2= models.AutoField(primary_key=True)
#     unit_test=models.IntegerField()
#     practical_test=models.IntegerField()
#     attendance=models.IntegerField()
#     one_day=models.IntegerField()
#     type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
#     cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    
#     class Meta:
#         db_table='theory_practicle_internal_component'

# class theory_practicle_external_component(models.Model):
#     eid2= models.AutoField(primary_key=True)
#     university_exam=models.IntegerField()
#     practicle_exam=models.IntegerField()
#     viva=models.IntegerField()
#     type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
#     cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    
#     class Meta:
#         db_table='theory_practicle_external_component'


# # **************** Only Praticle Subject *********************

# class practicle_internal_component(models.Model):
#     iid3= models.AutoField(primary_key=True)
#     unit_test=models.IntegerField()
#     attendance=models.IntegerField()
#     capstone=models.IntegerField()
#     type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
#     cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    
#     class Meta:
#         db_table='practicle_internal_component'

# class practicle_external_component(models.Model):
#     eid3= models.AutoField(primary_key=True)
#     practicle_exam=models.IntegerField()
#     viva=models.IntegerField()
#     type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
#     cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    
#     class Meta:
#         db_table='practicle_external_component'


# # **************** Only Project Subject *********************

# class project_internal_component(models.Model):
    
#     iid4= models.AutoField(primary_key=True)
#     review1 = models.IntegerField()
#     review2 = models.IntegerField()
#     review3 = models.IntegerField()
#     attendance=models.IntegerField()
    
#     type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
#     cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    
#     class Meta:
#         db_table='project_internal_component'

# class project_external_component(models.Model):
#     eid4= models.AutoField(primary_key=True)
#     project=models.IntegerField()
#     type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
#     cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    
#     class Meta:
#         db_table='project_external_component'


# # **************** Subject Master *********************

# class subject_master(models.Model):
#     sm_id= models.AutoField(primary_key=True)
    
#     cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
#     type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
   
#     class Meta:
#         db_table='subject_master'


# class subject_marks(models.Model):
#     sub_mark_id = models.AutoField(primary_key=True)
#     iid1 = models.ForeignKey(theory_internal_component, on_delete=models.CASCADE,db_column='iid1',default='')
#     eid1 = models.ForeignKey(theory_external_component, on_delete=models.CASCADE,db_column='eid1',default='')

#     iid2 = models.ForeignKey(theory_practicle_internal_component, on_delete=models.CASCADE,db_column='iid2',default='')
#     eid2 = models.ForeignKey(theory_practicle_external_component, on_delete=models.CASCADE,db_column='eid2',default='')

#     iid3 = models.ForeignKey(practicle_internal_component, on_delete=models.CASCADE,db_column='iid3',default='')
#     eid3 = models.ForeignKey(practicle_external_component, on_delete=models.CASCADE,db_column='eid3',default='')

#     iid4 = models.ForeignKey(project_internal_component, on_delete=models.CASCADE,db_column='iid4',default='')
#     eid4 = models.ForeignKey(project_external_component, on_delete=models.CASCADE,db_column='eid4',default='')

#     type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
#     cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    
#     class Meta:
#         db_table='subject_mark'

  
    
    

# class sem1_marks(models.Model):
#     sem1_id = models.AutoField(primary_key=True)
#     iid1 = models.ForeignKey(theory_internal_component, on_delete=models.CASCADE,db_column='iid1',default='')
#     eid1 = models.ForeignKey(theory_external_component, on_delete=models.CASCADE,db_column='eid1',default='')

#     iid2 = models.ForeignKey(theory_practicle_internal_component, on_delete=models.CASCADE,db_column='iid2',default='')
#     eid2 = models.ForeignKey(theory_practicle_external_component, on_delete=models.CASCADE,db_column='eid2',default='')

#     iid3 = models.ForeignKey(practicle_internal_component, on_delete=models.CASCADE,db_column='iid3',default='')
#     eid3 = models.ForeignKey(practicle_external_component, on_delete=models.CASCADE,db_column='eid3',default='')

#     iid4 = models.ForeignKey(project_internal_component, on_delete=models.CASCADE,db_column='iid4',default='')
#     eid4 = models.ForeignKey(project_external_component, on_delete=models.CASCADE,db_column='eid4',default='')

#     type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
#     cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    
#     class Meta:
#         db_table='sem1'



# class sem2_marks(models.Model):
#     sem2_id = models.AutoField(primary_key=True)
#     iid1 = models.ForeignKey(theory_internal_component, on_delete=models.CASCADE,db_column='iid1',default='')
#     eid1 = models.ForeignKey(theory_external_component, on_delete=models.CASCADE,db_column='eid1',default='')

#     iid2 = models.ForeignKey(theory_practicle_internal_component, on_delete=models.CASCADE,db_column='iid2',default='')
#     eid2 = models.ForeignKey(theory_practicle_external_component, on_delete=models.CASCADE,db_column='eid2',default='')

#     iid3 = models.ForeignKey(practicle_internal_component, on_delete=models.CASCADE,db_column='iid3',default='')
#     eid3 = models.ForeignKey(practicle_external_component, on_delete=models.CASCADE,db_column='eid3',default='')

#     iid4 = models.ForeignKey(project_internal_component, on_delete=models.CASCADE,db_column='iid4',default='')
#     eid4 = models.ForeignKey(project_external_component, on_delete=models.CASCADE,db_column='eid4',default='')

#     type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
#     cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    
#     class Meta:
#         db_table='sem2'


# class sem3_marks(models.Model):
#     sem3_id = models.AutoField(primary_key=True)
#     iid1 = models.ForeignKey(theory_internal_component, on_delete=models.CASCADE,db_column='iid1',default='')
#     eid1 = models.ForeignKey(theory_external_component, on_delete=models.CASCADE,db_column='eid1',default='')

#     iid2 = models.ForeignKey(theory_practicle_internal_component, on_delete=models.CASCADE,db_column='iid2',default='')
#     eid2 = models.ForeignKey(theory_practicle_external_component, on_delete=models.CASCADE,db_column='eid2',default='')

#     iid3 = models.ForeignKey(practicle_internal_component, on_delete=models.CASCADE,db_column='iid3',default='')
#     eid3 = models.ForeignKey(practicle_external_component, on_delete=models.CASCADE,db_column='eid3',default='')

#     iid4 = models.ForeignKey(project_internal_component, on_delete=models.CASCADE,db_column='iid4',default='')
#     eid4 = models.ForeignKey(project_external_component, on_delete=models.CASCADE,db_column='eid4',default='')

#     type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
#     cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    
#     class Meta:
#         db_table='sem3'


# class sem4_marks(models.Model):
#     sem4_id = models.AutoField(primary_key=True)
#     iid1 = models.ForeignKey(theory_internal_component, on_delete=models.CASCADE,db_column='iid1',default='')
#     eid1 = models.ForeignKey(theory_external_component, on_delete=models.CASCADE,db_column='eid1',default='')

#     iid2 = models.ForeignKey(theory_practicle_internal_component, on_delete=models.CASCADE,db_column='iid2',default='')
#     eid2 = models.ForeignKey(theory_practicle_external_component, on_delete=models.CASCADE,db_column='eid2',default='')

#     iid3 = models.ForeignKey(practicle_internal_component, on_delete=models.CASCADE,db_column='iid3',default='')
#     eid3 = models.ForeignKey(practicle_external_component, on_delete=models.CASCADE,db_column='eid3',default='')

#     iid4 = models.ForeignKey(project_internal_component, on_delete=models.CASCADE,db_column='iid4',default='')
#     eid4 = models.ForeignKey(project_external_component, on_delete=models.CASCADE,db_column='eid4',default='')

#     type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
#     cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
#     sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    
#     class Meta:
#         db_table='sem4'





# **************** Subject Type *********************

class subject_type(models.Model):
    type_id = models.AutoField(primary_key=True)
    subject_type = models.CharField(max_length=20)
    class Meta:
        db_table='subject_type'
    def __str__(self):
        return self.subject_type
   


# **************** Component Table *********************

class com_mst(models.Model):
   
    #com_id = models.ForeignKey(com_mst, on_delete=models.CASCADE,db_column='com_id',default='')
    sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    com_id = models.AutoField(primary_key=True)
    type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
    cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
    #****************** Internal Component ******************
    c1 = models.IntegerField()
    c2 = models.IntegerField()
    c3 = models.IntegerField()
    c4 = models.IntegerField()
    total = models.IntegerField(default=0)
    #****************** External Component ******************
    c5 = models.IntegerField()

     #****************** Practical Component ******************
    c6 = models.IntegerField(default=0)

    total1 =  models.IntegerField(default=0)
    class Meta:
        db_table='component_table'
    # def __str__(self):
    #     return self.com_id
    


class com_mst1(models.Model):
   
    #com_id = models.ForeignKey(com_mst, on_delete=models.CASCADE,db_column='com_id',default='')
    sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    com_id = models.AutoField(primary_key=True)
    type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
    cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
    #****************** Internal Component ******************
    c1 = models.IntegerField()
    c2 = models.IntegerField()
    c3 = models.IntegerField()
    c4 = models.IntegerField()
    total = models.IntegerField(default=0)
    #****************** External Component ******************
    c5 = models.IntegerField()
    #****************** Practical Component ******************
    c6 = models.IntegerField(default=0)

    total1 =  models.IntegerField(default=0)
    class Meta:
        db_table='sem2_component_table'



class com_mst2(models.Model):
   
    #com_id = models.ForeignKey(com_mst, on_delete=models.CASCADE,db_column='com_id',default='')
    sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    com_id = models.AutoField(primary_key=True)
    type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
    cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
    #****************** Internal Component ******************
    c1 = models.IntegerField()
    c2 = models.IntegerField()
    c3 = models.IntegerField()
    c4 = models.IntegerField()
    total = models.IntegerField(default=0)
    #****************** External Component ******************
    c5 = models.IntegerField()
    #****************** Practical Component ******************
    c6 = models.IntegerField(default=0)

    total1 =  models.IntegerField(default=0)
    class Meta:
        db_table='sem3_component_table'


class com_mst3(models.Model):
   
    #com_id = models.ForeignKey(com_mst, on_delete=models.CASCADE,db_column='com_id',default='')
    sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    com_id = models.AutoField(primary_key=True)
    type_id = models.ForeignKey(subject_type, on_delete=models.CASCADE,db_column='type_id',default='')
    cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
    #****************** Internal Component ******************
    c1 = models.IntegerField()
    c2 = models.IntegerField()
    c3 = models.IntegerField()
    
    c4 = models.IntegerField()
    total = models.IntegerField(default=0)
    #****************** External Component ******************
    c5 = models.IntegerField()

   
    #****************** Practical Component ******************
    c6 = models.IntegerField(default=0)


    total1 =  models.IntegerField(default=0)
    class Meta:
        db_table='sem4_component_table'


# **************** Subject Table *********************

class subject(models.Model):
    sub_id = models.AutoField(primary_key=True)
    cid = models.ForeignKey(Course, on_delete=models.CASCADE,db_column='cid',default='')
    com_id = models.ForeignKey(com_mst, on_delete=models.CASCADE,db_column='com_id',default='')
    sid = models.ForeignKey(Student, on_delete=models.CASCADE,db_column='sid',default='')
    
    class Meta:
        db_table='subject_table'
    # def __str__(self):
    #     return self.sub_id
    

    

    

class slider1(models.Model):
   
    hotel_Main_Img = models.ImageField(upload_to='media')
    class Meta:
        db_table=('slider11')


class slider2(models.Model):
   
    hotel_Main_Img = models.ImageField(upload_to='media')
    class Meta:
        db_table=('slider2')

class slider3(models.Model):
   
    hotel_Main_Img = models.ImageField(upload_to='media')
    class Meta:
        db_table=('slider3')

class slider4(models.Model):
   
    hotel_Main_Img = models.ImageField(upload_to='media')
    class Meta:
        db_table=('slider4')