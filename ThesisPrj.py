from flask import Flask,render_template,request,flash
import urllib, json
import pymysql
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import os

# import matplotlib.patches as mpatches
import numpy as np
import base64
import StringIO
from timegraph import timetrandesgr3,timedelgr1,timedelgr2,timedelgr3,timetransrcgr1,timetransrcgr2,timetransrcgr3,timetrandesgr1,timetrandesgr2

app = Flask(__name__)

con = pymysql.connect(host = 'localhost',user = 'root',passwd = '',db = 'jsondet')
cursor = con.cursor()




@app.route('/')
def main():
        timedelgr1()
        plottimecpb=timedelgr2()
        plottimeoscer=timedelgr3()
        plottimetransrcuta=timetransrcgr1()
        plottimetransrccpb=timetransrcgr2()
        plottimetransrcosc=timetransrcgr3()
        plottimetrandesuta=timetrandesgr1()
        plottimetrandescpb=timetrandesgr2()
        plottimetrandesosc=timetrandesgr3()
        return render_template('home.html',plottimecpb=plottimecpb,
                               plottimetransrcuta=plottimetransrcuta,plottimetransrccpb=plottimetransrccpb,
                               plottimeoscer=plottimeoscer,plottimetransrcosc=plottimetransrcosc,
                               plottimetrandesuta=plottimetrandesuta,plottimetrandescpb=plottimetrandescpb,
                               plottimetrandesosc=plottimetrandesosc,
                               ddval='0',allsites='visible',utasites='none',cpbsites='none',oscsites='none')

# def test():
#
#     y0 = []
#     y1 = []
#     y2 = []
#     x=[]
#     query="select sum(Pfiles) as pfiles, sum(dfiles) as dfiles, sum(ffiles) as ffiles, BatchId from delclusterhistory "\
#            "where Destinationsite = 'OU_OSCER_ATLAS' and " \
#             "batchId = (select max(BatchId) from delclusterhistory)"
#     x.append(1)
#     for h in range(1, 24):
#       query += " union all select sum(Pfiles) as pfiles,sum(dfiles) as dfiles,sum(ffiles) as ffiles,BatchId from delclusterhistory where Destinationsite='OU_OSCER_ATLAS'" \
#                         "and BatchId = (select max(BatchId) -"+str(h )+" from delclusterhistory)"
#       x.append(h+1)
#
#     print query
#     cursor.execute(query)
#     datatimegr = cursor.fetchall()
#     # count=0
#     for row in datatimegr:
#             # count = count+1
#             # x.append(int(count))
#             print row[0]
#             print row[1]
#             print row[2]
#             if (str(row[0]) == 'None'):
#                 y0.append(0)
#             else:
#                 y0.append(int(row[0]))
#             if (str(row[1]) == 'None'):
#                 y1.append(0)
#             else:
#                 y1.append(int(row[1]))
#             if (str(row[2]) == 'None'):
#                 y2.append(0)
#             else:
#                 y2.append(int(row[2]))
#
#     img = StringIO.StringIO()
#
#
#     plt.ylabel('No.of Files')
#     plt.title('UTA_SWT2 - Deletion')
#
#     plt.xlabel("Time in hours (Last 24 hrs)")
#     plt.ylabel("No.of files")
#             # plt.xticks(x)
#     plt.xticks(numpy.arange(0, 24, step=2))
#     plt.plot(x, y0, marker='o', color='blue', label='Planned')
#     plt.plot(x, y1, marker='^', color='green', label='Done')
#     plt.plot(x, y2, marker='*', color='red', label='Failed')
#     plt.legend(loc='upper center', bbox_to_anchor=(0.5,1.17), shadow=True, ncol=3)
#     plt.savefig(img, format='png')
#     img.seek(0)
#     plot_url = base64.b64encode(img.getvalue()).decode()
#     plt.gcf().clear()
#     return plot_url

@app.route("/deletion/uta_swt2.html")
def viewdelgraph1():
    plottimeuta = timedelgr1()
    return render_template('deletion/uta2.html',plottimeuta=plottimeuta)

@app.route("/deletion/swt2_cpb.html")
def viewdelgraph2():
    plottimecpb = timedelgr2()
    return render_template('deletion/cpb.html',plottimecpb=plottimecpb)

@app.route("/deletion/oscer_atlas.html")
def viewdelgraph3():
    plottimeoscer = timedelgr3()
    return render_template('deletion/oscer.html', plottimeoscer=plottimeoscer)

@app.route("/transfer/source/uta_swt2.html")
def viewtransrcgraph1():
    plottimetransrcuta = timetransrcgr1()
    return render_template('transfer/source/uta2.html', plottimetransrcuta=plottimetransrcuta)

@app.route("/transfer/source/swt2_cpb.html")
def viewtransrcgraph2():
    plottimetransrccpb = timetransrcgr2()
    return render_template('transfer/source/cpb.html', plottimetransrccpb=plottimetransrccpb)

@app.route("/transfer/source/oscer_atlas.html")
def viewtransrcgraph3():
    plottimetransrcosc = timetransrcgr3()
    return render_template('transfer/source/oscer.html', plottimetransrcosc=plottimetransrcosc)

@app.route("/transfer/destination/uta_swt2.html")
def viewtrandesgraph1():
    plottimetrandesuta = timetrandesgr1()
    return render_template('transfer/destination/uta2.html', plottimetrandesuta=plottimetrandesuta)

@app.route("/transfer/destination/swt2_cpb.html")
def viewtrandesgraph2():
    plottimetrandescpb = timetrandesgr2()
    return render_template('transfer/destination/cpb.html', plottimetrandescpb=plottimetrandescpb)

@app.route("/transfer/destination/oscer_atlas.html")
def viewtrandesgraph3():
    plottimetrandesosc = timetrandesgr3()
    return render_template('transfer/destination/oscer.html', plottimetrandesosc=plottimetrandesosc)

# @app.route('/line')
# def line():
#     labels = [
#         'JAN', 'FEB', 'MAR', 'APR',
#         'MAY', 'JUN', 'JUL', 'AUG',
#         'SEP', 'OCT', 'NOV', 'DEC'
#     ]
#
#     values = [
#         967.67, 1190.89, 1079.75, 1349.19,
#         2328.91, 2504.28, 2873.83, 4764.87,
#         4349.29, 6458.30, 9907, 16297
#     ]
#
#     colors = [
#         "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
#         "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
#         "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]
#
#     line_labels=labels
#     line_values=values
#     return render_template('linechart.html', title='Bitcoin Monthly Price in USD', max=17000, labels=line_labels, values=line_values)


@app.route("/preoneweek",methods=['GET', 'POST'])
def preoneweek():
    y0 = []
    y1 = []
    y2 = []
    x = []
    query = "select Coalesce(sum(Pfiles),0) as pfiles, Coalesce(sum(dfiles),0) as dfiles, Coalesce(sum(ffiles),0) as ffiles,cast(date(CreatedDate) as char) as CreatedDate " \
            "from delclusterhistory where Destinationsite = 'UTA_SWT2' " \
            "and date(CreatedDate)>= NOW() + INTERVAL -7 DAY AND date(CreatedDate) <  NOW() + INTERVAL  0 DAY " \
            "group by date(CreatedDate) order by date(Createddate) desc "

    cursor.execute(query)
    oneweek = cursor.fetchall()
    for row in oneweek:
        y0.append(int(row[0]))
        y1.append(int(row[1]))
        y2.append(int(row[2]))
        x.append(row[3])

    chart = {"renderTo": "chart_ID", "type": "line", "height": "350"}
    series = [{"name": 'Planned', "data": y0, "color": 'green'}, {"name": 'Done', "data": y1, "color": 'blue'},
              {"name": 'Failed', "data": y2, "color": 'red'}]
    title = {"text": 'UTA_SWT2(Cluster Health for past one week)'}
    xAxis = {"categories": x, "lineColor": 'Black', "lineWidth": '1'}
    # yAxis = [{"title": {"text": 'No.of Files'},"lineColor":'#FF0000','lineWidth':'1'}]
    yAxis = [{"title": {
        "text": 'Number of Files'
    }, "lineColor": 'Black', "lineWidth": '1'}]
    credits = {"credits": {"enabled": 'false'}}
    print 'f'

    return render_template('timeseries.html', chartID="chart_ID", chart=chart, series=series, title=title, xAxis=xAxis,
                           yAxis=yAxis, credits=credits)
    # count = 500
    # xScale = np.linspace(0, 100, count)
    # y0_scale = np.random.randn(count)
    # y1_scale = np.random.randn(count)
    # y2_scale = np.random.randn(count)
    #
    # # Create traces
    # trace0 = go.Scatter(
    #     x=xScale,
    #     y=y0_scale
    # )
    # trace1 = go.Scatter(
    #     x=xScale,
    #     y=y1_scale
    # )
    # trace2 = go.Scatter(
    #     x=xScale,
    #     y=y2_scale
    # )
    # data = [trace0, trace1, trace2]
    # print 'am'
    # graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    # return render_template('timeseries.html',
    #                        graphJSON=graphJSON)

@app.route("/pretwoweeks",methods=['GET', 'POST'])
def pretwoweeks():
    return render_template('timeseries.html');

@app.route("/preinterval",methods=['GET', 'POST'])
def preinterval():
    return render_template('timeseries.html');

@app.route("/config")
def config():
    cursor.execute("select count(*) from thresholds")
    cntres = cursor.fetchall()
    cntval=''
    for row in cntres:
        cntval=row[0]
    # utadel,utasrc,utades,cpbdel,cpbsrc,cpbdes,oscdel,oscsrc,oscdel=loadconfig()
    # return render_template('config.html',configres='',utadel=utadel,utasrc=utasrc,utades=utades)
    print cntval
    if(cntval==0):
        return render_template('config.html', configres='', utadel='', utasrc='', utades='',cpbdel='',cpbsrc='',cpbdes='',oscdel='',oscsrc='',oscdes='')
    else:

        utadel, utasrc, utades, cpbdel, cpbsrc, cpbdes, oscdel, oscsrc, oscdes = loadconfig()
        return render_template('config.html', configres='', utadel=utadel, utasrc=utasrc, utades=utades,cpbdel=cpbdel,cpbsrc=cpbsrc,cpbdes=cpbdes,oscdel=oscdel,oscsrc=oscsrc,oscdes=oscdes)

@app.route("/saveconfig", methods=['GET', 'POST'])
def saveconfig():
    if request.method == "POST":

        cursor.execute("delete from thresholds")
        con.commit()

        del1=request.form['del1']
        transrc1 = request.form['transrc1']
        trandes1 = request.form['trandes1']
        sitename1='UTA_SWT2'

        cursor.execute("INSERT INTO thresholds (Sitename, Deletionval,Transfersrcval,Transferdesval) VALUES (%s,%s,%s,%s)",(sitename1, del1, transrc1, trandes1))
        con.commit()

        del2 = request.form['del2']
        transrc2 = request.form['transrc2']
        trandes2 = request.form['trandes2']
        sitename2 = 'SWT2_CPB'
        cursor.execute(
            "INSERT INTO thresholds (Sitename, Deletionval,Transfersrcval,Transferdesval) VALUES (%s,%s,%s,%s)",
            (sitename2, del2, transrc2, trandes2))
        con.commit()
        del3 = request.form['del3']
        transrc3 = request.form['transrc3']
        trandes3 = request.form['trandes3']
        sitename3 = 'OU_OSCER_ATLAS'
        cursor.execute(
            "INSERT INTO thresholds (Sitename, Deletionval,Transfersrcval,Transferdesval) VALUES (%s,%s,%s,%s)",
            (sitename3, del3, transrc3, trandes3))
        con.commit()

        utadel, utasrc, utades, cpbdel, cpbsrc, cpbdes, oscdel, oscsrc, oscdes = loadconfig()
        return render_template('config.html', utadel=utadel, utasrc=utasrc, utades=utades, cpbdel=cpbdel,
                               cpbsrc=cpbsrc, cpbdes=cpbdes, oscdel=oscdel, oscsrc=oscsrc, oscdes=oscdes,configres="Config saved successfully")
        # return render_template('config.html',configres="Config saved successfully",utadel='', utasrc='', utades='',cpbdel='',cpbsrc='',cpbdes='',oscdel='',oscsrc='',oscdes='')

def loadconfig():
    cursor.execute('select Sitename,Deletionval,Transfersrcval,Transferdesval from thresholds')
    configval=cursor.fetchall()
    utaalert = str(configval[0]).split(',')
    cpbalert=str(configval[1]).split(',')
    oscalert=str(configval[2]).split(',')
    utav1=utaalert[1].replace("'", "")
    print 'utav1'
    print utav1
    utav2=utaalert[2].replace("'", "")
    utav3=utaalert[3].replace("')", "")
    cpbv1 = cpbalert[1].replace("'", "")
    cpbv2 = cpbalert[2].replace("'", "")
    cpbv3 = cpbalert[3].replace("')", "")
    oscv1 = oscalert[1].replace("'", "")
    oscv2 = oscalert[2].replace("'", "")
    oscv3 = oscalert[3].replace("')", "")
    return utav1,utav2,utav3.replace("'", ""),cpbv1,cpbv2,cpbv3.replace("'", ""),oscv1,oscv2,oscv3.replace("'", "")



@app.route("/viewtimegraph", methods=['GET', 'POST'])
def viewtimegraph():
    if request.method == "POST":
        selval=str(request.form['option'])
        print selval
        plottimeuta = timedelgr1()
        plottimecpb = timedelgr2()
        plottimeoscer = timedelgr3()
        plottimetransrcuta = timetransrcgr1()
        plottimetransrccpb = timetransrcgr2()
        plottimetransrcosc = timetransrcgr3()
        plottimetrandesuta = timetrandesgr1()
        plottimetrandescpb = timetrandesgr2()
        plottimetrandesosc = timetrandesgr3()
        v = 'visible'
        n = 'none'
        if selval=='1':
            return render_template('home.html', plottimeuta=plottimeuta, plottimecpb='',
                                   plottimetransrcuta=plottimetransrcuta, plottimetransrccpb='',
                                   plottimeoscer='', plottimetransrcosc='',
                                   plottimetrandesuta=plottimetrandesuta, plottimetrandescpb='',
                                   plottimetrandesosc='',
                                   allsites=n,utasites=v,cpbsites=n,oscsites=n,ddval='1')
        if selval=='2':
            return render_template('home.html', plottimeuta='', plottimecpb=plottimecpb,
                               plottimetransrcuta='', plottimetransrccpb=plottimetransrccpb,
                               plottimeoscer='', plottimetransrcosc='',
                               plottimetrandesuta='', plottimetrandescpb=plottimetrandescpb,
                               plottimetrandesosc='',
                               allsites=n,utasites=n,cpbsites=v,oscsites=n,ddval='2')
        if selval == '3':
           return render_template('home.html', plottimeuta=plottimeuta, plottimecpb=plottimecpb,
                                   plottimetransrcuta=plottimetransrcuta, plottimetransrccpb=plottimetransrccpb,
                                   plottimeoscer=plottimeoscer, plottimetransrcosc=plottimetransrcosc,
                                   plottimetrandesuta=plottimetrandesuta, plottimetrandescpb=plottimetrandescpb,
                                   plottimetrandesosc=plottimetrandesosc,
                                   allsites=n,utasites=n,cpbsites=n,oscsites=v,ddval='3')
        else:
           return render_template('home.html', plottimeuta=plottimeuta, plottimecpb=plottimecpb,
                                   plottimetransrcuta=plottimetransrcuta, plottimetransrccpb=plottimetransrccpb,
                                   plottimeoscer=plottimeoscer, plottimetransrcosc=plottimetransrcosc,
                                   plottimetrandesuta=plottimetrandesuta, plottimetrandescpb=plottimetrandescpb,
                                   plottimetrandesosc=plottimetrandesosc,
                                   allsites=v,utasites=n,cpbsites=n,oscsites=n,ddval='0')



# if __name__ == '__main__':
#     app.run()
if __name__ == '__main__':
    app.run(debug=True,port=4992)