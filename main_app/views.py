from django.shortcuts import render
import pandas as pd
from bs4 import BeautifulSoup

from django.http import HttpResponse
from django_tables2.tables import Table

# Create your views here.


def index(request):

    return render(request, 'index.html')


def show_data(request):

        csvfile = request.FILES['csv_file']
        data = pd.read_csv(csvfile)
        # data = data.to_html(classes=["table-bordered", "table-striped", "table-hover"])
        data = BeautifulSoup(data.to_html(), "html.parser")
        data.find('table')['id'] = 'my_table'
        data.find('table')['data-toggle'] = 'table'
        data.find('table')['data-toolbar'] = "#toolbar"
        data.find('table')['data-search'] = 'true'
        data.find('table')['data-show-refresh'] = 'true'
        data.find('table')['data-show-toggle'] = 'true'
        data.find('table')['data-show-fullscreen'] = 'true'
        data.find('table')['data-show-columns'] = 'true'
        data.find('table')['data-detail-view'] = 'true'
        data.find('table')['data-show-export'] = 'true'
        data.find('table')['data-click-to-select'] = 'true'
        data.find('table')['data-detail-formatter'] = "detailFormatter"
        data.find('table')['data-minimum-count-columns'] = '2'
        data.find('table')['data-show-pagination-switch'] = 'true'
        data.find('table')['data-pagination'] = 'true'
        data.find('table')['data-page-list'] = '[10, 25, 50, 100, all]'
        data.find('table')['data-show-footer'] = 'true'
        data.find('table')['data-side-pagination'] = 'server'
        data.find('table')['data-response-handler'] = 'responseHandler'


        print(data)
        # data = data.to_json(orient='split')
        return render(request, 'show_data.html', {'data': data})
        # df_table = Table(data.to_dict(orient='list'))
        # return render(request, "data_show.html", {'df_table': df_table})

        # return render(request, 'list.html', locals())