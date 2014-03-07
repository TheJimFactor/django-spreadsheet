from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from .models import Sheet
import json
import urllib2
import re
# Create your views here.

def index(request):
    sheets = Sheet.objects.all()
    return render_to_response('sheets/index.html',{
        'sheets':sheets,
        },
            context_instance=RequestContext(request),
    )
def sandbox(request):
    return render_to_response('sheets/sandbox.html',
            context_instance=RequestContext(request),
    )

def loadsheet(request):
    # return HttpResponse('lol')
    print request.POST
    sheet = request.POST.get('sheet')
    print sheet
    dbjson = Sheet.objects.filter(name__exact=sheet)
    # print dbjson[0].sheetjson
    # more jsony
    testdict = {'name': 'there'}
    demodict =  {u'data[3][]': [u'2011', u'4', u'2517', u'4822', u'552', u'6127'], u'data[1][]': [u'2009', u'0', u'2941', u'4303', u'354', u'5814'], u'data[4][]': [u'2012', u'2', u'2422', u'5399', u'776', u'4151'], u'data[0][]': [u'', u'Maserati', u'Mazda', u'Mercedes', u'Mini', u'Mitsubishi'], u'data[5][2]': [u''], u'data[5][1]': [u''], u'data[5][0]': [u''], u'data[5][5]': [u''], u'data[2][]': [u'2010', u'5', u'2905', u'2867', u'412', u'5284'], u'data[5][4]': [u''], u'data[5][3]': [u'']}
    # return HttpResponse(json.dumps(demodict), content_type="application/json", mimetype=None)
    demodict2 = [[u',Maserati,Mazda,Mercedes,Mini,Mitsubishi'], [u'2009,0,2941,4303,354,5814', u'2010,5,2905,2867,412,5284', u'2011,4,2517,4822,552,6127', u'2012,2,2422,5399,776,4151', u',,,,,']]
    jsondict = [["2011", "4", "2517", "4822"], ["2009", "0", "2941", "5399"]]
    jsondict2 = [['', 'Maserati', 'Mazda', 'Mercedes', 'Mini', 'Mitsubishi'], ['2009', '0', '2941', '4303', '354', '5814'], ['2010', '5', '2905', '2867', '412', '5284'], ['2011', '4', '2517', '4822', '552', '6127'], ['2012', '2', '2422', '5399', '776', '4151'], ['', '', '', '', '', '']]
    # return HttpResponse(json.dumps(jsondict), content_type="application/json", mimetype=None)
    # return HttpResponse(json.dumps(demodict2), content_type="application/json", mimetype=None)
    # return HttpResponse(json.dumps(jsondict2), content_type="application/json", mimetype=None)
    return HttpResponse(dbjson[0].sheetjson, content_type="application/json", mimetype=None)

    # return HttpResponse('data=,Maserati,Mazda,Mercedes,Mini,Mitsubishi&data=2009,0,2941,4303,354,5814&data=2010,5,2905,2867,412,5284&data=2011,4,2517,4822,552,6127&data=2012,2,2422,5399,776,4151&data=,,,,,', content_type="application/json", mimetype=None)
    # return HttpResponse('data=,Maserati,Mazda,Mercedes,Mini,Mitsubishi&data=2009,0,2941,4303,354,5814&data=2010,5,2905,2867,412,5284&data=2011,4,2517,4822,552,6127&data=2012,2,2422,5399,776,4151&data=,,,,,')
    # print json.dumps(demodict)
    # return HttpResponse('{"data":[{"lol", "taco"}]}')
    # return HttpResponse('{"data":[{"lol", "taco"}]}', content_type="application/json", mimetype=None)

def savesheet(request):
    if request.method == 'POST':
        # newSheet = Sheet(name=request.POST.get("name"))

        print request.POST
        print request.POST.get('sheet')
        if request.POST.get('sheet') == "Create New":
            print "The text input will be used for the sheet name"
        print request.POST.get('sheetname')
        # print request.raw_post_data
        # print request.POST[u'data']
        print request.body
        # unparse the JSON data with url decode
        print urllib2.unquote(request.body)
        rawdata = urllib2.unquote(request.body)
        # print json.loads(request.body)
        # print json.loads(urllib2.unquote(request.body))

        #TODO:
        # first try enabling json client side http://stackoverflow.com/questions/1208067/wheres-my-json-data-in-my-incoming-django-request
        # parse the request body to allow on &data= and strip the data= at the start, put it into a list
        print rawdata
        # print '-'*5
        # sheet = re.match(r'sheet=([^&]+)')
        # print sheet
        # print '-'*5
        sheet = request.POST.get('sheet')
        newsheetname = request.POST.get('sheetname')
        # print '-'*5
        # print 'Position of &data is: %s'% rawdata.find("&data=")
        # print '-'*5
        # cut off the start of the string
        rawdata = rawdata[rawdata.find("&data=")+len("&data="):]
        print '-'*5
        print rawdata
        # rawdata = rawdata.replace("sheet=&data=", "", 1)
        # rawdata = rawdata.replace("&data=", "", 1)
        rawdata = rawdata.split("&data=")
        print '-'*5 + 'split'
        print rawdata
        for i, val in enumerate(rawdata):
            rawdata[i] = rawdata[i].split(",")
            print '-'*5
        print rawdata

        if sheet == "Create New":
            newSheet = Sheet(name=newsheetname, sheetjson=json.dumps(rawdata))
        else:
            newSheet = Sheet(name=sheet, sheetjson=json.dumps(rawdata))
        newSheet.save()
        print newSheet.name

        # look into payload validation https://gist.github.com/copitux/3778800


        # explode on the commas of each bit to make the inner list of lists

        # http://stackoverflow.com/questions/13349573/how-to-change-a-django-querydict-to-python-dict
        # datadict = request.POST.dict()
        # fuckc
        print '-'*8
        # print datadict
        # print '-'*8
        # print json.dumps(datadict)


        #MAYHEM TESTING!
        # newSheet = Sheet(name='lol', sheetjson=request.POST.get("data"))
        # JSONdata = request.POST.get("data")
        #attempting to get the json data out, naked post reference
        # print 'hi'
        # print request.POST[u'name']
        # print request.POST.get("name")
        # print json.loads(request.POST)
        # JSONData = request.POST.get
        # JSONData = request.POST.get("name")
        # print JSONData
        # print 'hi'
        # datadict = simplejson.JSONDecoder().decode( JSONData )
        # datadict = json.JSONDecoder().decode( request.POST )
        # print request.POST.get("data")
        # print request.POST
        # newSheet.save()
    #     return RequestContext(request, 'sheet saved')
    # return RequestContext(request, 'sheet malformed and not saved')
        # return HttpResponse('lol' + 'hehe' + request.POST.get("data"))
        return HttpResponse('lol')
    return HttpResponse('lol')
