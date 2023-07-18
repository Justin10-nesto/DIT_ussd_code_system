from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as bs
from .models import Student, UserSelection
from . import Scapper
import random

def checking_back(code):
  code_new = ''
  try:
    code_arr = code.split('00*')
    code_new = code_arr[-1]
  except:
    code_new = code
  return code_new

@csrf_exempt
def index(request):
  response = "CON Dar es salaam Institute of Technology.\n"
  response += "1. View semester result. \n"
  response += "2. Generating control number. \n"
  response += "3. Registration status.\n"
  if request.method == 'POST':
    session_id = request.POST.get('sessionId')
    service_code = request.POST.get('serviceCode')
    phone_number = request.POST.get('phoneNumber')
    text1 = request.POST.get('text')
    text = checking_back(text1)
    
    user = Student.objects.filter(phone_number = phone_number)
    if user.exists():
      response = ""
      
      user_status = user.first()
      if text == "1":
        response = "CON Choose academic year.\n"
        response += "1. General course (GC).\n"
        response += "2. First Year.\n"
        response += "3. Second Year.\n"
        response += "4. Third Year.\n"
        response += "00. Return to the main Menu.\n"
      elif text == "1*1":
        result_type = 1
        UserSelection.objects.create(student=user_status, task='View Results', value=result_type) 
        response = "END your results is"
        
      elif text == "1*00" or text == "2*00" or text == "3*00" or text == "4*00" or text == "2*1*00" or text == "2*2*00":
        text = ''      
        
      elif text == "1*2":
        result_type = 2
        UserSelection.objects.create(student=user_status, task='View Results', value=result_type)
        response = f"END you results is "
        
      elif text == "1*3":
        result_type = 3
        UserSelection.objects.create(student=user_status, task='View Results', value=result_type)
        response = "END you results is"
      elif text == "1*4":
        result_type = 4
        UserSelection.objects.create(student=user_status, task='View Results', value=result_type)
        response = "END you results is"
        
      elif text == "2":
          response = "CON Generating control numbers.\n"
          response += "1. Fees and Direct Cost.\n"
          response += "2. Other Payments. \n"
          response += "00. return to the main Menu.\n"
          
      elif text == "2*1":
        response = "CON Fees and Direct Cost.\n"
        response +="Payable by HELSB.\n"
        response += "1. Tution Fee.\n"
        response += "2. Direct cost. \n"
        response +="Please select amount of tution fee."
        response += "00. return to the main Menu.\n"

      elif text == '2*1*1':
          control_number = random.randint(9900000000, 9999999999)
          response = f"END Your Generated control Number is: {control_number}"
      elif text == '2*1*2':
          control_number = random.randint(9900000000, 9999999999)
          response = f"END Your Generated control Number is: {control_number}"

      elif text == "2*2":
        response = "CON Generating control numbers for other payments.\n"
        response += "1. ID losten.\n"
        response += "2. Transcripts. \n"
        response += "2. Examination results. \n"
        response +="Please select 1. Approve\n 2. Denide.\n"
        response += "00. Return to the main Menu.\n"

      elif text == "2*2*1":
          control_number = random.randint(9900000000, 9999999999)
          response = f"END Your Generated control Number is: {control_number}"

      elif text == "2*3*1":
          control_number = random.randint(9900000000, 9999999999)
          response = f"END Your Generated control Number is: {control_number}"
      elif text == "2*3*2":
          control_number = random.randint(9900000000, 9999999999)
          response = f"END Your Generated control Number is: {control_number}"
      elif text == "2*2*3":
          control_number = random.randint(9900000000, 9999999999)
          response = f"END Your Generated control Number is: {control_number}"

      elif text == "3":
        result_type =0
        UserSelection.objects.create(student=user_status, task='View Registration', value=result_type)
        response = f"END please wait your result will be sent to you shortly\n"
    
      if text == "":
        response = "CON Dar es Salaam Institute of Technology.\n"
        response += "1. View semester results. \n"
        response += "2. Generating control numbers. \n"
        response += "3. Registration status.\n"
        response += "4. Exist"
    
    else:
        response = f"END Please visit to admission office at DIT to register your mobile number so as to access this system.\n"
    return HttpResponse(response)
  return HttpResponse(response)

def checking_registration(email, password):
    print('ok')
    statement = ''
    payment = False
    registration = False
    confirmation = False
    
    login_url = 'https://soma.dit.ac.tz/login'
    secure_url = 'https://soma.dit.ac.tz/'
    session = requests.Session()
    secure_url = 'https://soma.dit.ac.tz/'
    request = session.get(login_url).content
    soup = bs(request,'html.parser')
    csrf = soup.find('input',{'name':'csrf'}).get('value')
    payload = {
            'email': email,
            'password': password,
            'csrf': csrf,
            }
    p = session.post(login_url,data=payload)
    print('ok')
    if 'Welcome, you have successfully logged into your account' in p.text:
        print('login successful')
        t = session.get(secure_url)

        soup = bs(t.text, "html.parser")

        result_url = (f'https://soma.dit.ac.tz/admission/registrationct')
        admision_status = session.get(result_url).text
        admision_statuss = bs(admision_status,'html.parser')
        link =admision_statuss.select('div.row i')
        for index, data in enumerate(link[:3]):
            results = data.get('class')[1]
            if results == 'fa-check-circle':
                if index == 0:
                    payment = True
                elif index == 1:
                    registration = True
                else:
                    confirmation = True
    if confirmation:
         statement = 'You are registered.'
    elif registration and not confirmation:
        statement = 'Please visit admission office for confirmation.'
    elif payment and not registration:
        statement = 'Please just register your modules.'
    else:
        statement = 'Please accomplish tution fee.'
    print(statement)
    return statement