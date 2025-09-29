from django.urls import path , include
from .views import *
from rest_framework.routers import DefaultRouter
from apistudents import views
from rest_framework_simplejwt import TokenObtainPairView , TokenRefreshView

router = DefaultRouter()
router.register("employees" , views.EmployeeViewset , basename="employee")

urlpatterns = [ 
    path('students/' , apiStudent),
    path('students/<int:pk>/' , apiStudentPK),

    


    # path('employee/' , Employee.as_view()),
    # path('employee/<int:pk>/' , Employee_PK.as_view())
    
    path('' , include(router.urls)),
    path('blogs/' , views.BlogView.as_view()),
    path('comments/' , views.CommentView.as_view()),


    path('blogs/' , TokenObtainPairView.as_view()),
    path('blogs/' , TokenRefreshView.as_view()),




    path('blogs/<int:pk>/' , views.BlogDetailsView.as_view()),
    path('comments/<int:pk>/' , views.CommentsDetailsView.as_view()),


 ]
