from csv import reader
from optparse import Values
from select import select
from tracemalloc import start
from django.http import HttpResponse, JsonResponse
from django.template import loader 
from django.db.models import Q
from .models import *
from django.shortcuts import render
import sqlite3


def search_autocomplete_view(request):
    query = request.GET.get('query', '')
    results = GeneList.objects.filter(approved_symbol__startswith=query).values_list('approved_symbol', flat=True)
    results = list(results)[0:10] #shows first 10 results
    matched_results = [result for result in results if query.lower() in result.lower()]
    

    return JsonResponse(matched_results, safe=False)


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
    
    query = ''
    if request.POST:
        query=request.POST['query']
    query=query.split(',')
        
    for gene in query: #gene is the name of any searched element that are splitted by a comma#
        gene=gene.strip() #clear white space at start and end of the gene name#
        
        if request.method=='POST':

            dataapprovedsymbol=GeneList.objects.filter(approved_symbol__iexact=gene)
            data=data+list(dataapprovedsymbol)
            



    context= {
        'listData':[]
    }

    for res in data: 
        graphdata = []
        citationqueries=[res.approved_symbol]
        if res.previous_symbol:
            citationqueries=citationqueries+res.previous_symbol.split('|')
        if res.synonyms:
            citationqueries=citationqueries+res.synonyms.split('|')
            
            
        citations=[]
        con = sqlite3.connect("GraphDates.db")
        con.row_factory = sqlite3.Row 
        cur = con.cursor()

        for query in citationqueries:
            for row in cur.execute(f'SELECT * FROM GraphDates WHERE "Date" = "{query}"'):
                row=list(row)
                graphdata.append(row)


        context['listData'].append({
            'ApprovedSymbol':(res.approved_symbol+' (Discontunied)'if res.approved_symbol.endswith('~') else res.approved_symbol),
            'htmlfiles':'html_files/' + res.approved_symbol.split('~')[0] + '.html',
            'DateNameChanged':res.date_name_changed,
            'PreviousSymbols':res.previous_symbol,
            'Synonyms':res.synonyms,      
            'GraphData':graphdata,
        })
        
    template=loader.get_template('index.html')
    return HttpResponse(template.render(context, request,))








  


    
        


