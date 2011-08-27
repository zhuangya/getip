from django.http import HttpResponse
iplog = "/home/dotcloud/iplogfile"

def write_ip(request):
    if request.META['QUERY_STRING'] == "x=ff":
        iplogfile = open(iplog, "w+")
#        iplogfile.write(request.META['REMOTE_ADDR'])
        iplogfile.write(request.META['HTTP_X_FORWARDED_FOR'])
        iplogfile.close()
        return HttpResponse("write..")
    return HttpResponse("")

def read_ip(request):
    iplogfile = open(iplog, "r")
    return HttpResponse([line for line in iplogfile])
    return HttpResponse("")
