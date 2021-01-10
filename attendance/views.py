from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from . import models
from . import forms
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

###############################################################
# Client
###############################################################


class ClientListView(LoginRequiredMixin, ListView):
    model = models.Client
    template_name = 'attendance/client/client_list.html'


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = models.Client
    template_name = 'attendance/client/client_detail.html'


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Client
    fields = ['client_name', 'head_office', 'contact_person_name', 'mobile_number']
    template_name = 'attendance/client/client_form.html'

    def get_success_url(self):
        return reverse('client-detail', args=[self.object.id])


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = models.Client
    fields = ['client_name', 'head_office', 'contact_person_name', 'mobile_number']
    template_name = 'attendance/client/client_form.html'

    def get_success_url(self):
        return reverse('client-detail', args=[self.object.id])

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ClientCreateView, self).form_valid(form)


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Client
    template_name = 'attendance/client/client_delete.html'

    def get_success_url(self):
        return reverse('client-list')

###############################################################
# Vendor
###############################################################


class VendorListView(LoginRequiredMixin, ListView):
    model = models.Vendor
    template_name = 'attendance/vendor/vendor_list.html'

    def get_queryset(self):
        client = get_object_or_404(models.Client, id=self.kwargs.get('client_id'))
        return models.Vendor.objects.filter(client=client)

    def render_to_response(self, context, **response_kwargs):
        context['client_id'] = self.kwargs.get('client_id')
        return super(VendorListView, self).render_to_response(context)


class VendorDetailView(LoginRequiredMixin, DetailView):
    model = models.Vendor
    template_name = 'attendance/vendor/vendor_detail.html'

    def render_to_response(self, context, **response_kwargs):
        context['client_id'] = self.kwargs.get('client_id')
        return super(VendorDetailView, self).render_to_response(context)


class VendorUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Vendor
    fields = ['vendor_name', 'office_address', 'contact_person', 'mobile_number']
    template_name = 'attendance/vendor/vendor_form.html'

    def get_success_url(self):
        return reverse('vendor-detail', args=[self.kwargs.get('client_id'), self.object.id])


class VendorCreateView(LoginRequiredMixin, CreateView):
    model = models.Vendor
    fields = ['vendor_name', 'office_address', 'contact_person', 'mobile_number']
    template_name = 'attendance/vendor/vendor_form.html'

    def get_success_url(self):
        return reverse('vendor-detail', args=[self.kwargs.get('client_id'), self.object.id])

    def form_valid(self, form):
        client = get_object_or_404(models.Client, id=self.kwargs.get('client_id'))
        form.instance.client = client
        return super(VendorCreateView, self).form_valid(form)


class VendorDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Vendor
    template_name = 'attendance/vendor/vendor_delete.html'

    def get_success_url(self):
        return reverse('vendor-list', args=[self.kwargs.get('client_id')])

    def render_to_response(self, context, **response_kwargs):
        context['client_id'] = self.kwargs.get('client_id')
        return super(VendorDeleteView, self).render_to_response(context)


###############################################################
# Sub Vendor
###############################################################


class SubVendorListView(LoginRequiredMixin, ListView):
    model = models.SubVendor
    template_name = 'attendance/sub_vendor/sub_vendor_list.html'

    def get_queryset(self):
        vendor = get_object_or_404(models.Vendor, id=self.kwargs.get('vendor_id'))
        return models.SubVendor.objects.filter(vendor=vendor)

    def render_to_response(self, context, **response_kwargs):
        context['vendor_id'] = self.kwargs.get('vendor_id')
        return super(SubVendorListView, self).render_to_response(context)


class SubVendorDetailView(LoginRequiredMixin, DetailView):
    model = models.SubVendor
    template_name = 'attendance/sub_vendor/sub_vendor_detail.html'

    def render_to_response(self, context, **response_kwargs):
        context['vendor_id'] = self.kwargs.get('vendor_id')
        return super(SubVendorDetailView, self).render_to_response(context)


class SubVendorUpdateView(LoginRequiredMixin, UpdateView):
    model = models.SubVendor
    fields = ['sub_vendor_name', 'office_address', 'contact_person', 'mobile_number']
    template_name = 'attendance/sub_vendor/sub_vendor_form.html'

    def get_success_url(self):
        return reverse('sub-vendor-detail', args=[self.kwargs.get('vendor_id'), self.object.id])


class SubVendorCreateView(LoginRequiredMixin, CreateView):
    model = models.SubVendor
    fields = ['sub_vendor_name', 'office_address', 'contact_person', 'mobile_number']
    template_name = 'attendance/sub_vendor/sub_vendor_form.html'

    def get_success_url(self):
        return reverse('sub-vendor-detail', args=[self.kwargs.get('vendor_id'), self.object.id])

    def form_valid(self, form):
        vendor = get_object_or_404(models.Vendor, id=self.kwargs.get('vendor_id'))
        form.instance.vendor = vendor
        return super(SubVendorCreateView, self).form_valid(form)


class SubVendorDeleteView(LoginRequiredMixin, DeleteView):
    model = models.SubVendor
    template_name = 'attendance/sub_vendor/sub_vendor_delete.html'

    def get_success_url(self):
        return reverse('sub-vendor-list', args=[self.kwargs.get('vendor_id')])

    def render_to_response(self, context, **response_kwargs):
        context['vendor_id'] = self.kwargs.get('vendor_id')
        return super(SubVendorDeleteView, self).render_to_response(context)

###############################################################
# Team
###############################################################


class TeamListView(LoginRequiredMixin, ListView):
    model = models.Team
    template_name = 'attendance/team/team_list.html'

    def get_queryset(self):
        sub_vendor = get_object_or_404(models.SubVendor, id=self.kwargs.get('sub_vendor_id'))
        return models.Team.objects.filter(sub_vendor=sub_vendor)

    def render_to_response(self, context, **response_kwargs):
        context['sub_vendor_id'] = self.kwargs.get('sub_vendor_id')
        return super(TeamListView, self).render_to_response(context)


class TeamDetailView(LoginRequiredMixin, DetailView):
    model = models.Team
    template_name = 'attendance/team/team_detail.html'

    def render_to_response(self, context, **response_kwargs):
        context['sub_vendor_id'] = self.kwargs.get('sub_vendor_id')
        return super(TeamDetailView, self).render_to_response(context)


class TeamUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Team
    form_class = forms.TeamForm
    template_name = 'attendance/team/team_form.html'

    def get_success_url(self):
        return reverse('team-detail', args=[self.kwargs.get('sub_vendor_id'), self.object.id])


class TeamCreateView(LoginRequiredMixin, CreateView):
    model = models.Team
    form_class = forms.TeamForm
    template_name = 'attendance/team/team_form.html'

    def get_success_url(self):
        return reverse('team-detail', args=[self.kwargs.get('sub_vendor_id'), self.object.id])

    def form_valid(self, form):
        sub_vendor = get_object_or_404(models.SubVendor, id=self.kwargs.get('sub_vendor_id'))
        form.instance.sub_vendor = sub_vendor
        return super(TeamCreateView, self).form_valid(form)


class TeamDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Team
    template_name = 'attendance/team/team_delete.html'

    def get_success_url(self):
        return reverse('team-list', args=[self.kwargs.get('sub_vendor_id')])

    def render_to_response(self, context, **response_kwargs):
        context['sub_vendor_id'] = self.kwargs.get('sub_vendor_id')
        return super(TeamDeleteView, self).render_to_response(context)

###############################################################
# Employee
###############################################################


class EmployeeListView(LoginRequiredMixin, ListView):
    model = models.Employee
    template_name = 'attendance/employee/employee_list.html'

    def get_queryset(self):
        team = get_object_or_404(models.Team, id=self.kwargs.get('team_id'))
        return models.Employee.objects.filter(team=team)

    def render_to_response(self, context, **response_kwargs):
        context['team_id'] = self.kwargs.get('team_id')
        return super(EmployeeListView, self).render_to_response(context)


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = models.Employee
    template_name = 'attendance/employee/employee_detail.html'

    def render_to_response(self, context, **response_kwargs):
        context['team_id'] = self.kwargs.get('team_id')
        return super(EmployeeDetailView, self).render_to_response(context)


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Employee
    form_class = forms.EmployeeForm
    template_name = 'attendance/employee/employee_form.html'

    def get_success_url(self):
        return reverse('employee-detail', args=[self.kwargs.get('team_id'), self.object.id])


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = models.Employee
    form_class = forms.EmployeeForm
    template_name = 'attendance/employee/employee_form.html'

    def get_success_url(self):
        return reverse('employee-detail', args=[self.kwargs.get('team_id'), self.object.id])

    def form_valid(self, form):
        team = get_object_or_404(models.Team, id=self.kwargs.get('team_id'))
        form.instance.team = team
        return super(EmployeeCreateView, self).form_valid(form)


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Employee
    template_name = 'attendance/employee/employee_delete.html'

    def get_success_url(self):
        return reverse('employee-list', args=[self.kwargs.get('team_id')])

    def render_to_response(self, context, **response_kwargs):
        context['team_id'] = self.kwargs.get('team_id')
        return super(EmployeeDeleteView, self).render_to_response(context)

###############################################################
# Attendance
###############################################################


@login_required
def mark_attendance(request: WSGIRequest):
    if request.method == 'GET':
        context = {}
        request_query = request.GET.get('team_name')

        if request_query is not None:
            team = get_object_or_404(models.Team, team_name=request_query)
            employees = models.Employee.objects.filter(team=team)
            attendance_form_list: list = []

            for employee in employees:
                attendance_form_list.append(forms.AttendanceForm(initial={'employee': employee}))

            context['forms'] = attendance_form_list

            return render(request=request, template_name='attendance/attendance/mark_attendance.html', context=context)
        else:
            teams = models.Team.objects.all()
            context['teams'] = teams
            return render(request, template_name='attendance/attendance/select_team_mark_attendance.html', context=context);

    elif request.method == 'POST':
        forms.AttendanceForm(request.POST).save()
        return HttpResponse("<h1>Done</h1>")


@login_required
def view_attendance(request: WSGIRequest):
    request_query_team_name = request.GET.get('team_name')

    if request_query_team_name is not None:
        team = get_object_or_404(models.Team, team_name=request_query_team_name)
        employees = models.Employee.objects.filter(team=team)

        attendance_list = []

        for employee in employees:
            attendance_list += employee.attendance_set.all()

        return render(request, 'attendance/attendance/view_attendance.html', context={'attendance_list': attendance_list})

    else:
        teams = models.Team.objects.all()
        return render(request, template_name='attendance/attendance/select_team_mark_attendance.html', context={'teams': teams});
