from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector
from . import urls
from . import forms
import random, string, os,binascii


def display(request):
  #Database connection
  mydb = mysql.connector.connect(
  host="<database hostname>",
  user="username",
  password="password",
  database="database name"
)
  mycursor = mydb.cursor(dictionary=True)
  sql = f"SELECT * FROM router_details"
  mycursor.execute(sql)
  results = mycursor.fetchall()
  return render(request,'rmanagement/display.html',{'st':results})

def create_rval(request):
  #Database connection
  mydb = mysql.connector.connect(
  host="<database hostname>",
  user="username",
  password="password",
  database="database name"
)
  mycursor = mydb.cursor()
  form = forms.FormName()
  if request.method == 'POST':
    form = forms.FormName(request.POST)
    if form.is_valid():
      sapid = form.cleaned_data['sapid']
      hostname = form.cleaned_data['hostname']
      loopback = form.cleaned_data['loopback']
      macaddress = form.cleaned_data['macaddress']
      sql = f"INSERT INTO router_details (Sapid, Hostname, Loopback, MACaddress) VALUES ('{sapid}', '{hostname}', '{loopback}', '{macaddress}')"
      mycursor.execute(sql)
      mydb.commit()
    form = forms.FormName()
  return render(request,'rmanagement/formpage.html', {'form':form, 'page':'Create'})

def update_rval(request):
  #Database connection
  mydb = mysql.connector.connect(
  host="<database hostname>",
  user="username",
  password="password",
  database="database name"
)
  mycursor = mydb.cursor()
  form = forms.FormName()
  if request.method == 'POST':
    form = forms.FormName(request.POST)
    if form.is_valid():
      sapid = form.cleaned_data['sapid']
      hostname = form.cleaned_data['hostname']
      loopback = form.cleaned_data['loopback']
      macaddress = form.cleaned_data['macaddress']
      sql = f"UPDATE router_details SET Sapid = '{sapid}', Hostname = '{hostname}', Loopback = '{loopback}', MACaddress = '{macaddress}' WHERE Sapid = '{sapid}'"
      print(sql)
      mycursor.execute(sql)
      mydb.commit()
  return render(request,'rmanagement/formpage.html', {'form':form, 'page':'Update'})

def delete_rval(request):
  #Database connection
  mydb = mysql.connector.connect(
  host="<database hostname>",
  user="username",
  password="password",
  database="database name"
)
  mycursor = mydb.cursor()
  form = forms.FormName_delete()
  if request.method == 'POST':
    form = forms.FormName_delete(request.POST)
    if form.is_valid():
      sapid = form.cleaned_data['sapid']
      sql = f"DELETE FROM router_details WHERE Sapid = '{sapid}'"
      mycursor.execute(sql)
      mydb.commit()
  return render(request,'rmanagement/delete.html', {'form':form})

def index(request):
  #Database connection
  mydb = mysql.connector.connect(
  host="<database hostname>",
  user="username",
  password="password",
  database="database name"
)
  mycursor = mydb.cursor(dictionary=True)
  form = forms.FormName_generate()
  n = 0
  if request.method == 'POST':
    form = forms.FormName_generate(request.POST)
    if form.is_valid():
      n = form.cleaned_data['num']
  Sapid, Hostname, Loopback, MACaddress = ([] for _ in range(4))
  for _ in range(n):
      macdata = str(binascii.b2a_hex(os.urandom(6))).split("'")[1]
      macdata = ':'.join(macdata[i:i+2] for i in range(0, len(macdata), 2))
      print ('Generated mac', macdata)

      hostdata = 'host_'+''.join(random.choices(string.ascii_letters + string.digits, k=9))
      print ('Generated host', hostdata)

      ipdata=str(random.randint(0, 255))
      for _ in range(3):
        ipdata += '.'
        ipdata += str(random.randint(0, 255))
      print ('Generated ip', ipdata)

      sapiddata = str(binascii.b2a_hex(os.urandom(9))).split("'")[1]
      print ('Generated sapid', sapiddata)
      Sapid.append(sapiddata)
      Hostname.append(hostdata)
      Loopback.append(ipdata)
      MACaddress.append(macdata)

  # Insert generated data into connected Database
  for x in range(len(Sapid)):
    # print(f'Sapid({Sapid[x]}) \tHostname({Hostname[x]}) \tLoopback({Loopback[x]}) \tMACaddress({MACaddress[x]})')
    sql = f"INSERT INTO router_details (Sapid, Hostname, Loopback, MACaddress) VALUES ('{Sapid[x]}', '{Hostname[x]}', '{Loopback[x]}', '{MACaddress[x]}')"
    mycursor.execute(sql)

  mydb.commit()
  sql = f"SELECT * FROM router_details"
  mycursor.execute(sql)
  results = mycursor.fetchall()
  mycursor.close()
  mydb.close()
  return render(request,'rmanagement/index.html',{'st':results, 'form':form})

