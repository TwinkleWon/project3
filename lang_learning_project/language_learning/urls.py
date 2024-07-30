from django.urls import path
from . import views

app_name = 'language_learning'

urlpatterns = [
    path('', views.index, name='index'),
    path('word/create/', views.word_create, name='word_create'),
    path('word/<int:word_id>/update/', views.word_update, name='word_update'),
    path('word/<int:word_id>/delete/', views.word_delete, name='word_delete'),
    path('word/<int:word_id>/', views.word_detail, name='word_detail'),
    path('word/<int:word_id>/edit-pronunciation/', views.edit_pronunciation, name='edit_pronunciation'),
    path('word/<int:word_id>/edit-category/', views.edit_category, name='edit_category'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz/result/<int:word_id>/<str:correct>/', views.quiz_result, name='quiz_result'),
]
