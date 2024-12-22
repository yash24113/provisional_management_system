
from django.urls import path  

from django.conf.urls.static import static

from imageupload.views import *
from . import views

urlpatterns = [  
   # path('img/',hotel_image_view,name='image_upload'),
   path('success',success,name='success'),
   path('img/hotel_images/',display_hotel_images,name='hotel_images'),
   path('delete/<int:id>', destroy),  
   path('edit/<int:id>', edit),  
   path('update/<int:id>',update),  
   path('admin_display_hotel_images',views.admin_display_hotel_images),
   path('display_hotel_images',views.display_hotel_images),
   path('home',views.home),
]  


