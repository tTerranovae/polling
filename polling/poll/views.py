from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Polling


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        if Polling.objects.filter(ip_address=ip):
            return redirect('poll:bye')
        else:

            return render(request, self.template_name)


class Bye(TemplateView):
    template_name = 'thankyou.html'

    def get(self, request, *args, **kwargs):
        obj = Polling.objects.all()
        return render(request, self.template_name, {'obj': obj})


CHECKBOX_MAPPING = {'on': True, 'None': False, 'off': False}


def form_data(request):
    print(request)
    if request.method == 'POST':
        soap_heard = CHECKBOX_MAPPING.get(request.POST.get('soap-heard', 'off'))
        soap_worked = CHECKBOX_MAPPING.get(request.POST.get('soap-worked', 'off'))
        soap_no = CHECKBOX_MAPPING.get(request.POST.get('soap-no', 'off'))

        rest_heard = CHECKBOX_MAPPING.get(request.POST.get('rest-heard', 'off'))
        rest_worked = CHECKBOX_MAPPING.get(request.POST.get('rest-worked', False))
        rest_no = CHECKBOX_MAPPING.get(request.POST.get('rest-no', False))

        django_heard = CHECKBOX_MAPPING.get(request.POST.get('django-heard', 'off'))
        django_worked = CHECKBOX_MAPPING.get(request.POST.get('django-worked', 'off'))
        django_no = CHECKBOX_MAPPING.get(request.POST.get('django-no', 'off'))

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


def polling_result(request):
    print(Polling.objects.all())

    polling_django_know = Polling.objects.filter(django_know=True).count()
    polling_django_unknown = Polling.objects.filter(django_unknown=True).count()
    polling_django_worked = Polling.objects.filter(django_worked=True).count()

    print(polling_django_unknown, polling_django_know, polling_django_worked)
    return render(request, 'poll.html', {'django_worked': polling_django_worked, 'django_know': polling_django_know,
                                         'django_unknown': polling_django_unknown})


from django.http import JsonResponse


class Counts(APIView):
    def get(self, request, format=None):
        c = {}
        soap_know = Polling.objects.filter(soap_know=True).count()
        soap_unknown = Polling.objects.filter(soap_unknown=True).count()
        soap_worked = Polling.objects.filter(soap_worked=True).count()

        rest_know = Polling.objects.filter(rest_know=True).count()
        rest_unknown = Polling.objects.filter(rest_unknown=True).count()
        rest_worked = Polling.objects.filter(rest_worked=True).count()

        django_know = Polling.objects.filter(django_know=True).count()
        django_unknown = Polling.objects.filter(django_unknown=True).count()
        django_worked = Polling.objects.filter(django_worked=True).count()

        graphql_know = Polling.objects.filter(graphql_know=True).count()
        graphql_unknown = Polling.objects.filter(graphql_unknown=True).count()
        graphql_worked = Polling.objects.filter( graphql_worked=True).count()

        ip = Polling.objects.all().count()


        c['soap_know'] = soap_know
        c['soap_unknown'] = soap_unknown
        c['soap_worked'] = soap_worked

        c['rest_know'] = rest_know
        c['rest_unknown'] = rest_unknown
        c['rest_worked'] = rest_worked

        c['django_know'] = django_know
        c['django_unknown'] = django_unknown
        c['django_worked'] = django_worked

        c['graphql_know'] = graphql_know
        c['graphql_unknown'] = graphql_unknown
        c['graphql_worked'] = graphql_worked

        c['ip'] = ip

        return JsonResponse(c)


class Result(TemplateView):
    template_name = 'result.html'
