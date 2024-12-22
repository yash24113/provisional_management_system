from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
   path('', views.sign_up),
   path('home', views.home, name='home'),
   path('logout',views.logout_view),
   # path('addstu',views.store_student),
   # path('adddep',views.store_dep),
   # path('addcourse',views.store_course),
    path('add_subject_type',views.store_subject_type),
    path('show_subject_type',views.show_subject_type),

#     path('add_theory_internal_component',views.store_theory_internal_component),
#     path('show_theory_internal_component',views.show_theory_internal_component),


#     path('add_theory_external_component',views.store_theory_external_component),
#     path('show_theory_external_component/',views.show_theory_external_component),

#     path('add_theory_practicle_internal_component',views.store_theory_practicle_internal_component),
#     path('show_theory_practicle_internal_component',views.show_theory_practicle_internal_component),
   
#     path('add_theory_practicle_external_component',views.store_theory_practicle_external_component),
#     path('show_theory_practicle_external_component',views.show_theory_practicle_external_component),
   

#    path('add_practicle_internal_component',views.store_practicle_internal_component),
#     path('show_practicle_internal_component',views.show_practicle_internal_component),
   

#    path('add_practicle_external_component',views.store_practicle_external_component),
#     path('show_practicle_external_component',views.show_practicle_external_component),
   
# path('add_project_internal_component',views.store_project_internal_component),
# path('show_project_internal_component',views.show_project_internal_component),
   
# path('add_subject_master',views.store_subject_master),
# path('show_subject_master',views.show_subject_master),
   
#    path('add_project_external_component',views.store_project_external_component),
#     path('show_project_external_component',views.show_project_external_component),
   
#     path('add_subject_marks',views.store_subject_marks),
#     path('show_subject_marks',views.show_subject_marks),
   
  #  path('add_sem1_marks',views.store_sem1_marks),
#     path('add_sem2_marks',views.store_sem2_marks),
#      path('add_sem3_marks',views.store_sem3_marks),
#       path('add_sem4_marks',views.store_sem4_marks),

   # path('showcourse',views.show_course),
   # path('showstu',views.show_student),
   # path('showsem',views.show_sem),
     path('html_to_pdf', views.html_to_pdf, name='html_to_pdf'),
     #add Urls
   path('addstu',views.store_student),
   path('adddep',views.store_dep),
   path('addcourse',views.store_course),
   path('addcom',views.store_com),
   path('addcomsem2',views.store_com_sem2),
     path('addcomsem3',views.store_com_sem3),
       path('addcomsem4',views.store_com_sem4),
   path('addsub',views.store_sub),
   path('addsem',views.store_sem),
   
   path('add_provisional_request',views.store_provisional_request),
   path('add_bonafide_request',views.store_bonafide_request),
    path('add_final_request',views.store_final_request),
    
   #show related urls
   path('showcourse/',views.show_course),
    path('showcom/',views.show_com),
     path('showcom1/',views.show_com_sem2),
      path('showcom2/',views.show_com_sem3),
       path('showcom3/',views.show_com_sem4),
      path('showsubject/',views.show_sub),
      path('showsem1/',views.show_sem1),
      path('showsem2/',views.show_sem2),
      path('showsem3/',views.show_sem3),
      path('showsem4/',views.show_sem4),

       path('show_final_result/',views.final_history),

       path('final_showsem1/',views.final_show_sem1),
      path('final_showsem2/',views.final_show_sem2),
      path('final_showsem3/',views.final_show_sem3),
      path('final_showsem4/',views.final_show_sem4),

   path('show_dep',views.show_dep),
   
   path('showstu/',views.show_student),
  # path('show_provisional_request/',views.show_student1),
   path('showsem',views.show_sem),
   path('show_provisional_request',views.show_provisional_request),
    path('hod_show_provisional_request',views.hod_show_provisional_request),
   path('show_bonafide_request',views.show_bonafide_request),
    path('hod_show_bonafide_request',views.hod_show_bonafide_request),
    path('show_final_request',views.show_final_request),
    path('hod_show_final_request',views.hod_show_final_request),
   #edit related urls
   path('editcourse/<str:cid>',views.edit_course),
   path('updatecourse/<str:cid>',views.update_course),
   path('editdepart/<str:did>',views.edit_depart),
   path('updatedepart/<str:did>',views.update_depart),
   path('editsem1/<str:com_id>',views.edit_sem1),
   path('updatesem1/<str:com_id>',views.update_sem1),
   path('editstu/<str:sid>',views.edit_student),
   path('updatestu/<str:sid>',views.update_student),
    path('editsem/<str:sem_id>',views.edit_sem),
   path('updatesem/<str:sem_id>',views.update_sem),

   #delete related Urls
   path('deletecourse/<str:cid>',views.delete_course), 
   path('deletedepart/<str:did>',views.delete_depart),
   path('deletestu/<str:sid>',views.delete_student),
  #  path('delete_mark/<str:m_id>',views.delete_mark),
   path('deletesem/<str:sem_id>',views.delete_sem),
path('delete_subject_type/<str:type_id>',views.delete_subject_type),
# path('delete_theory_internal_component/<str:iid1>',views.delete_theory_internal_component),
# path('delete_theory_external_component/<str:eid1>',views.delete_theory_external_component),
# path('delete_theory_practicle_internal_component/<str:iid2>',views.delete_theory_practicle_internal_component),
# path('delete_theory_practicle_external_component/<str:eid2>',views.delete_theory_practicle_external_component),
# path('delete_practicle_internal_component/<str:iid3>',views.delete_practicle_internal_component),
# path('delete_practicle_external_component/<str:eid3>',views.delete_practicle_external_component),
# path('delete_project_internal_component/<str:iid4>',views.delete_project_internal_component),
# path('delete_project_external_component/<str:eid4>',views.delete_project_external_component),
# path('delete_subject_master/<str:sm_id>',views.delete_subject_master),
# path('delete_sem1_marks/<str:sem1_id>',views.delete_sem1_marks),

# path("theory_internal_external",views.theory_internal_external),
# path("theory_practicle_internal_external",views.theory_practicle_internal_external),
# path("practicle_internal_external",views.practicle_internal_external),
# path("project_internal_external",views.project_internal_external),


# path("practicle_internal_external1",views.practicle_internal_external1),

path('subject_component',views.subject_component),

   path('user', views.user_details),
   path('main_admin',views.main_admin),
  path('main_hod',views.main_hod),
  path('hod_show_bonafide_request',views.hod_show_bonafide_request),
  path('delete_hod_show_bonafide_request/<str:bono_id>',views.delete_hod_show_bonafide_request), 
  path('delete_show_bonafide_request/<str:bono_id>',views.delete_show_bonafide_request), 
  path('delete_hod_show_provisional_request/<str:pro_id>',views.delete_hod_show_provisional_request), 
  path('delete_show_provisional_request/<str:pro_id>',views.delete_show_provisional_request), 
   path('delete_hod_show_final_request/<str:final_id>',views.delete_hod_show_final_request), 
  path('delete_show_final_request/<str:final_id>',views.delete_show_final_request), 
  #path('delete_subject_marks/<str:sub_mark_id>',views.delete_subject_marks), 
   # path('editstu/<int:id>',views.edit_student),
   # path('updatestu/<int:id>',views.update_student),
   # path('deletestu/<int:id>',views.delete_student), 

    path('about',views.about),
    path('feedback',views.feedback),
    path('feedback1',views.feedback1),
    path('feedback2',views.feedback2),
    path('feedback3',views.feedback3),
    path('feedback4',views.feedback4),
    path('blog',views.blog),
    path('blog2',views.blog2),

   path('history',views.history),
    path('final_history',views.final_history),
     # path('sem1_history',views.sem1_history),
   #   path('sem2_history',views.sem2_history),
   #   path('sem3_history',views.sem3_history),
   #   path('sem4_history',views.sem4_history),


    path('show_bonafide_certificate',views.show_bonafide_certificate),
    # path('download_bonafide_certificate',views.download_bonafide_certificate),
   

# path('store_theory_external_component',views.store_theory_external_component),


 path('delete_com/<str:com_id>',views.delete_com), 
 path('delete_com_sem2/<str:com_id>',views.delete_com_sem2), 
 path('delete_com_sem3/<str:com_id>',views.delete_com_sem3), 
 path('delete_com_sem4/<str:com_id>',views.delete_com_sem4), 
 path('delete_sub/<str:sub_id>',views.delete_sub), 










  path('addslider',views.slider_image_view),
  path('admin_display_slider_images',views.admin_display_slider_images),
   path('display_slider_images',views.display_slider_images),
    path('delete/<int:id>',views.destroy),  



    path('addslider1',views.slider_image_view1),
  path('admin_display_slider_images1',views.admin_display_slider_images1),
   path('display_slider_images1',views.display_slider_images1),
    path('delete1/<int:id>',views.destroy1),  

    path('edit2/<int:id>',views.slider2_edit),  
   path('update2/<int:id>',views.slider2_update),  

]

