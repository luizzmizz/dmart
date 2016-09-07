from django.shortcuts import render
from datetime import datetime
# Create your views here.
from models import query
from django.http import HttpResponse
from django.template import loader
from django.db import connections

import django_tables2 as tables
import os

class mytable(tables.Table):
    contract_number=tables.Column()
    nuno_name=tables.Column()
    active_on=tables.DateColumn()
    cancel_on=tables.DateColumn()
    billing_start_on=tables.DateColumn()
    billing_end_on=tables.DateColumn()
    state_name=tables.Column()
    status_name=tables.Column()
    linea_tec_name=tables.Column()
    contacto_name=tables.Column()
    owner_name=tables.Column()
    created_on=tables.DateColumn()
    merge_status=tables.Column()
    last_opp_renewal=tables.DateColumn()
    contract_version=tables.Column()
    class Meta:
      attrs = {"class": "paleblue"}

def runQuery(query,params,request):
    cursor=connections['nexus'].cursor().execute(query,params)
    results = cursor.fetchall()
    x = cursor.description
    resultsList = []
    for r in results:
        i = 0
        d = {}
        while i < len(x):
            d[x[i][0].lower()] = r[i]
            i = i+1
        resultsList.append(d)
    cursor.close()
    table=mytable(resultsList)
    tables.RequestConfig(request,paginate=False).configure(table)
    return HttpResponse(loader.get_template('contracts/result.html').render({'result': table,'STATIC_URL':'/static/'}, request))

def index(request):
    sdate=request.GET('sdate',datetime.now())
    edate=request.GET('edate',datetime.now())
    query="""select c.contract_number,c.external_contract_number,c.nuno_name,c.fase,
           c.active_on,c.expired_on-1 hey,c.cancel_on,
           c.billing_start_on,c.billing_end_on,
           c.state_name,c.status_name,
           c.linea_tec_name,
           c.contacto_name,c.owner_name,c.created_on,c.merge_status,
           c.last_opp_renewal,
           c.contract_version
      from
      uni_mscrm.contracts c
      where to_number(to_char(c.expired_on-1,'yy'))>=:year
        and to_number(to_char(c.active_on,'yy'))<=:year
        and c.linea_tec_name in ('Sistemas','Google Enterprise Solutions')              """
    params={'year':sdate}
    return runQuery(query,params,request)

def listqueries(request):
    return HttpResponse(loader.get_template('contracts/listqueries.html').render({ 'queries': query.objects.all() }, request))
