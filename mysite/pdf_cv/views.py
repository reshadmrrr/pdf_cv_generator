from django import template
from .models import Profile
from django.shortcuts import render
import pdfkit
from django.http import HttpResponse, response
from django.template import loader
import io

# Create your views here.

def accept(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summery = request.POST.get("summery", "")
        degree = request.POST.get("degree", "")
        school = request.POST.get("school", "")
        university = request.POST.get("university", "")
        previous_work = request.POST.get("previous_work", "")

        profile = Profile(name=name, email=email, phone=phone, summery=summery, degree=degree, school=school, university=university, previous_work=previous_work)
        profile.save()
    return render(request, 'pdf_cv/accept.html')\

def resume(request, id):
    user = Profile.objects.get(pk=id)
    template = loader.get_template('pdf_cv/resume.html')
    html = template.render( {'user':user})
    options = {
        'page-size':'A4',
        'encoding': 'UTF-8',
    }
    config = pdfkit.configuration(wkhtmltopdf="C:\\src\\wkhtmltox\\bin\\wkhtmltopdf.exe")
    pdf = pdfkit.from_string(html, False, options, configuration=config)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = 'resume.pdf'

    return response
    # return render(request, 'pdf_cv/resume.html', {'user':user})