from django.http import HttpResponse
import os
import datetime
import subprocess

def htop_view(request):
    name = "Your Full Name"
    username = os.getlogin()
    ist_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput('top -b -n 1')

    response_data = f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h3>Server Time (IST): {ist_time}</h3>
    <pre>{top_output}</pre>
    """
    return HttpResponse(response_data)
