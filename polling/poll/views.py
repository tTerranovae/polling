from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Polling


class IndexView(TemplateView):
    template_name = 'index.html'


class Bye(TemplateView):
    template_name = 'thankyou.html'

    def get(self, request, *args, **kwargs):
        obj = Polling.objects.all()
        return render(request, self.template_name,{'obj':obj})


CHECKBOX_MAPPING = {'on': True, 'None': False, 'off': False}


def form_data(request):
    print(request)
    if request.method == 'POST':
        soap_heard = CHECKBOX_MAPPING.get(request.POST.get('soap-heard', 'off'))
        soap_worked = CHECKBOX_MAPPING.get(request.POST.get('soap-worked','off'))
        soap_no = CHECKBOX_MAPPING.get(request.POST.get('soap-no','off'))

        rest_heard = CHECKBOX_MAPPING.get(request.POST.get('rest-heard','off'))
        rest_worked = CHECKBOX_MAPPING.get(request.POST.get('rest-worked', False))
        rest_no = CHECKBOX_MAPPING.get(request.POST.get('rest-no', False))

        django_heard = CHECKBOX_MAPPING.get(request.POST.get('django-heard', 'off'))
        django_worked = CHECKBOX_MAPPING.get(request.POST.get('django-worked','off'))
        django_no = CHECKBOX_MAPPING.get(request.POST.get('django-no','off'))

        gql_heard = CHECKBOX_MAPPING.get(request.POST.get('gql-heard', 'off'))
        gql_worked = CHECKBOX_MAPPING.get(request.POST.get('gql-worked', 'off'))
        gql_no = CHECKBOX_MAPPING.get(request.POST.get('gql-no', 'off'))


        print(soap_heard, soap_worked, soap_no)
        print(rest_heard, rest_worked, rest_no)
        print(django_heard, django_worked, django_no)
        print(gql_heard, gql_worked, gql_no)

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        print(ip)

        poll = Polling(soap_know=soap_heard, soap_unknown=soap_no, soap_worked=soap_worked,
                       rest_know=rest_heard, rest_unknown=rest_no, rest_worked=rest_worked,
                       django_know=django_heard, django_unknown=django_no, django_worked=django_worked,
                       graphql_know=gql_heard, graphql_unknown=gql_no, graphql_worked=gql_worked,
                       ip_address=ip
                       )
        poll.save()

    return redirect('poll:bye')
