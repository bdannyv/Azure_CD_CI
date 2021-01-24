from django.http import HttpResponse


def index(request):
    return HttpResponse("CI/CD AzureDevOps pipelines training")
