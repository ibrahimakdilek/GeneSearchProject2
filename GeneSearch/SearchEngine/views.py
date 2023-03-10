from csv import reader
from optparse import Values
from select import select
from tracemalloc import start
from django.http import HttpResponse
from django.template import loader 
from django.db.models import Q
from .models import *
from django.shortcuts import render
import sqlite3



def get_approved_symbols():
    con = sqlite3.connect("GeneCard.db")
    con.row_factory = sqlite3.Row 
    cur = con.cursor()
    result = []
    for row in cur.execute(f'SELECT ApprovedSymbol FROM GeneStudy'):
        row=list(row)
        result.append(row[0])
    return result



def index(request):
    data=[]
    if request.method=='POST':


        dataapprovedsymbol=GeneList.objects.filter(approved_symbol__iexact=request.POST['query'])

        data=list(dataapprovedsymbol)



    context= {
        'listData':[]
    }


    for res in data: 
        graphdata = []
    

        if res.linked_genes:

            citationqueries=res.linked_genes.split('|')
            citationqueries.append(request.POST['query'])
            
            citations=[]
            con = sqlite3.connect("GraphDates.db")
            con.row_factory = sqlite3.Row 
            cur = con.cursor()

            for query in citationqueries:
                for row in cur.execute(f'SELECT * FROM GraphDates WHERE "Date" = "{query}"'):
                    row=list(row)
                    graphdata.append(row)
        else:
            context['resultFound'] = True

        context['listData'].append({
            'ApprovedSymbol':res.approved_symbol,
            'DateNameChanged':res.date_name_changed,
            'PreviousSymbols':res.previous_symbol,
            'Synonyms':res.synonyms,      
            'GraphData':graphdata,
        })
        
    template=loader.get_template('index.html')
    return HttpResponse(template.render(context, request,))








  


    
        


