import paramiko
import os, os.path, time
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from ..models import Connect
from ..forms import NacmForm, IpFormset, UploadForm
from .. import models
from scp import SCPClient
from django.conf import settings

def restore(request):
	ip_list = []

	# hal yang dilakukan ketika melakukan action POST	
	if request.method == 'POST':
		# mengambil nilai dari form
		formm = NacmForm(request.POST or None)
		ipform = IpFormset(request.POST)
		upform = UploadForm(request.POST,request.FILES)
		userValue = formm['username'].value()
		passValue = formm['password'].value()
		# inisialisasi directory upload file
		up_dir = "upload/"
		upload_dir = os.path.join(settings.MEDIA_ROOT, up_dir)
		ssh_client = paramiko.SSHClient()
		ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh_client.load_system_host_keys()

		# jika form valid
		if ipform.is_valid():
			simpanForm = formm.save()

			# perulangan data pada form ipform
			for form in ipform:
				ipaddr = form.cleaned_data.get('ipaddr')
				vendor = form.cleaned_data.get('vendor')
				fileconf = ipaddr+'.rsc'
				collect_config = "<b>Configure on "+str(ipaddr)+" | vendor = "+str(vendor)+"</b></br>"
				print ("true")

				# membaca sytanx konfigurasi dari database
				config_read = str(vendor.sett_restore)	

				# jika menekan tombol "upload"
				if request.POST.get("upload"):
					localfilepath = os.getcwd()
					remotefilepath = 'auto.cfg'
					print('test wanna upload something....')
					mediapath = upload_dir

					# membaca tiap file yang diupload di directory "upload"
					for count, x in enumerate(request.FILES.getlist("files")):
						def process(f):
							with open( upload_dir + f.name, 'wb+') as destination:
								for chunk in f.chunks():
									destination.write(chunk)

							def files(mediapath):
								for file in os.listdir(mediapath):
									if os.path.isfile(os.path.join(mediapath, file)):
										# memisahkan nama file dengan ekstensinnya
										files = file.rsplit('.',1)[0]
										yield files

							# mengirimkan file ke perangkat via protokol scp
							for ftp_con in files(mediapath):
								print (ftp_con)
								fileconf = ftp_con+'.rsc'
									
								print(fileconf)
								ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
								ssh_client.load_system_host_keys()
								ssh_client.connect(hostname=ftp_con,username=userValue,password=passValue)
								print("upload")
								scp = SCPClient(ssh_client.get_transport())
								scp.put(mediapath + fileconf, fileconf)
								scp.close()
								time.sleep(1)				
								os.remove(mediapath+fileconf)
	
						process(x)

					# login ke perangkat melalui protokol SSH untuk mengeksekusi perintah import
					ssh_client.connect(hostname=ipaddr,username=userValue,password=passValue)
					remote_conn=ssh_client.invoke_shell()
					config_send = eval(config_read)
					collect_config = collect_config + config_send+"</br>" 
					# menggunakan non-interactive shell
					try:
						ssh_client.exec_command(config_send+"\n\r")
						time.sleep(1)
						ssh_client.exec_command(" \r\n")
						time.sleep(1)
						print('coba exec')
					except:
						# jika gagal menggunakan interactive shell
						try:
							print ('coba interactive')
							print (config_send+'\n')
							remote_conn.send(config_send+'\n\r')
							time.sleep(1)
							remote_conn.send(' \r\n')
							time.sleep(1)
							results = remote_conn.recv(65535)
							print ('coba interactive 2')
						# jika gagal upload
						except paramiko.ssh_exception.SSHException as e:
							print("error paramiko %s" % e)

					print('testlah habis upload')
				# menyimpan data ke sqlite
				messages.success(request, "sucess restore configuration "+config_send)
				simpanForm.conft = "restore configuration"
				simpanIp = form.save(commit=False)
				simpanIp.connect_id = simpanForm
				print (simpanIp)
				simpanIp.save()
				simpanForm.save()
				formm.save()

			return HttpResponseRedirect('/restore')

	# hal yang dilakukan ketika melakukan action selain POST 
	else:
		formm = NacmForm()
		ipform = IpFormset()
		upform = UploadForm()
		return render(request, 'restore.html', {'form': formm, 'logins': Connect.objects.all(), 'ipform': ipform, 'upform': upform })