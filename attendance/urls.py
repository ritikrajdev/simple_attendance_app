from django.urls import path
from . import views

urlpatterns = [
    path('client/', views.ClientListView.as_view(), name='client-list'),
    path('client/<int:pk>/', views.ClientDetailView.as_view(), name='client-detail'),
    path('client/<int:pk>/update/', views.ClientUpdateView.as_view(), name='client-update'),
    path('client/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client-delete'),
    path('client/create/', views.ClientCreateView.as_view(), name='client-create'),

    path('client/<int:client_id>/vendor/', views.VendorListView.as_view(), name='vendor-list'),
    path('client/<int:client_id>/vendor/<int:pk>/', views.VendorDetailView.as_view(), name='vendor-detail'),
    path('client/<int:client_id>/vendor/<int:pk>/update/', views.VendorUpdateView.as_view(), name='vendor-update'),
    path('client/<int:client_id>/vendor/<int:pk>/delete/', views.VendorDeleteView.as_view(), name='vendor-delete'),
    path('client/<int:client_id>/vendor/create/', views.VendorCreateView.as_view(), name='vendor-create'),

    path('vendor/<int:vendor_id>/sub-vendor/', views.SubVendorListView.as_view(), name='sub-vendor-list'),
    path('vendor/<int:vendor_id>/sub-vendor/<int:pk>/', views.SubVendorDetailView.as_view(), name='sub-vendor-detail'),
    path('vendor/<int:vendor_id>/sub-vendor/<int:pk>/update/', views.SubVendorUpdateView.as_view(),
         name='sub-vendor-update'),
    path('vendor/<int:vendor_id>/sub-vendor/<int:pk>/delete/', views.SubVendorDeleteView.as_view(),
         name='sub-vendor-delete'),
    path('vendor/<int:vendor_id>/sub-vendor/create/', views.SubVendorCreateView.as_view(), name='sub-vendor-create'),

    path('sub-vendor/<int:sub_vendor_id>/team/', views.TeamListView.as_view(), name='team-list'),
    path('sub-vendor/<int:sub_vendor_id>/team/<int:pk>/', views.TeamDetailView.as_view(), name='team-detail'),
    path('sub-vendor/<int:sub_vendor_id>/team/<int:pk>/update/', views.TeamUpdateView.as_view(), name='team-update'),
    path('sub-vendor/<int:sub_vendor_id>/team/<int:pk>/delete/', views.TeamDeleteView.as_view(), name='team-delete'),
    path('sub-vendor/<int:sub_vendor_id>/team/create/', views.TeamCreateView.as_view(), name='team-create'),

    path('team/<int:team_id>/employee/', views.EmployeeListView.as_view(), name='employee-list'),
    path('team/<int:team_id>/employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('team/<int:team_id>/employee/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee-update'),
    path('team/<int:team_id>/employee/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee-delete'),
    path('team/<int:team_id>/employee/create/', views.EmployeeCreateView.as_view(), name='employee-create'),

    path('mark-attendance/', views.mark_attendance, name='mark-attendance'),
    path('view-attendance/', views.view_attendance, name='view-attendance'),
]
