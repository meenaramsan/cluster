from flask import Flask,render_template,request
import urllib, json
import pymysql
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches
import numpy
import base64
import StringIO
import os
import cv2

import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline


con = pymysql.connect(host = 'localhost',user = 'root',passwd = '',db = 'jsondet')
cursor = con.cursor()
#
# def datatest:
#     query = "select sum(Pfiles) as pfiles, sum(dfiles) as dfiles, sum(ffiles) as ffiles, BatchId from delclusterhistory " \
#             "where Destinationsite = 'UTA_SWT2' and " \
#             "batchId = (select max(BatchId) from delclusterhistory)"


def timedelgr1():
    y0 = []
    y1 = []
    y2 = []
    x = []
    query = "select Coalesce(sum(Pfiles),0) as pfiles, Coalesce(sum(dfiles),0) as dfiles, Coalesce(sum(ffiles),0) as ffiles, BatchId from delclusterhistory " \
            "where Destinationsite = 'UTA_SWT2' and " \
            "batchId = (select max(BatchId) from delclusterhistory)"
    x.append(1)
    for h in range(1, 24):
        query += " union all select Coalesce(sum(Pfiles),0) as pfiles,Coalesce(sum(dfiles),0) as dfiles,Coalesce(sum(ffiles),0) as ffiles,BatchId from delclusterhistory where Destinationsite='UTA_SWT2'" \
                 " and BatchId = (select max(BatchId) -" + str(h) + " from delclusterhistory)"
        x.append(h + 1)


    # query="SELECT Coalesce(sum(Pfiles),0) as pfiles, Coalesce(sum(dfiles),0) as dfiles,"\
    #       "Coalesce(sum(ffiles),0) as ffiles,BatchId FROM delclusterhistory "\
    #         "WHERE date(createddate) >= now() - INTERVAL 1 DAY and destinationsite='UTA_SWT2' "\
    #         "group by BatchId order by BatchId desc;"

    cursor.execute(query)
    datatimegr = cursor.fetchall()
    count=0
    # count = cursor.rowcount
    # for i in range(count):
    #     x.append(i + 1)
    for row in datatimegr:
        # count = count+1
        # x.append(int(count))

        # if (str(row[0]) == 'None'):
        #     y0.append(0)
        # else:
            y0.append(int(row[0]))
        # if (str(row[1]) == 'None'):
        #     y1.append(0)
        # else:
            y1.append(int(row[1]))
        # if (str(row[2]) == 'None'):
        #     y2.append(0)
        # else:
            y2.append(int(row[2]))
    img = StringIO.StringIO()
    plt.ylabel('No.of Files')
    plt.title('UTA_SWT2 - Deletion')

    plt.xlabel("Time in hours (Last 24 hrs)")
    plt.ylabel("No.of files")
    # plt.xticks(x)
    plt.xticks(numpy.arange(0, 24, step=2))
    plt.plot(x, y0, marker='o', color='blue', label='Planned')
    plt.plot(x, y1, marker='^', color='green', label='Done')
    plt.plot(x, y2, marker='*', color='red', label='Failed')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.17), shadow=True, ncol=3)
    # plt.savefig(img, format='png')
    currentFile = __file__

    realPath = os.path.realpath(currentFile)
    dirPath = os.path.dirname(realPath)
    print dirPath
    plt.savefig(dirPath + '\static\images\del_uta.png')
    # plt.savefig(my_path + '/Sub Directory/graph.png')
    # script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    # rel_path = "images\cig1.jpg"
    # abs_file_path = os.path.join(script_dir, rel_path)
    # print abs_file_path
    #plt.savefig('../images/cig1.jpg')

    # img.seek(0)
    # plot_url = base64.b64encode(img.getvalue()).decode()
    # plt.gcf().clear()
    # print 'f1'
    # return plot_url


def timedelgr2():
    y0 = []
    y1 = []
    y2 = []
    x = []
    # query = "SELECT Coalesce(sum(Pfiles),0) as pfiles, Coalesce(sum(dfiles),0) as dfiles," \
    #         "Coalesce(sum(ffiles),0) as ffiles,BatchId FROM delclusterhistory " \
    #         "WHERE date(createddate) >= now() - INTERVAL 1 DAY and destinationsite='SWT2_CPB' " \
    #         "group by BatchId order by BatchId desc;"
    query = "select Coalesce(sum(Pfiles),0) as pfiles, Coalesce(sum(dfiles),0) as dfiles, Coalesce(sum(ffiles),0) as ffiles, BatchId from delclusterhistory " \
            "where Destinationsite = 'SWT2_CPB' and " \
            "batchId = (select max(BatchId) from delclusterhistory)"
    x.append(1)
    for h in range(1, 24):
        query += " union all select Coalesce(sum(Pfiles),0) as pfiles,Coalesce(sum(dfiles),0) as dfiles,Coalesce(sum(ffiles),0) as ffiles,BatchId from delclusterhistory where Destinationsite='SWT2_CPB'" \
                 " and BatchId = (select max(BatchId) -" + str(h) + " from delclusterhistory)"
        x.append(h + 1)

    cursor.execute(query)
    datatimegr = cursor.fetchall()
    # count=0
    # count = cursor.rowcount
    # for i in range(count):
    #     x.append(i + 1)
    for row in datatimegr:
        # count = count+1
        # x.append(int(count))

        # if (str(row[0]) == 'None'):
        #     y0.append(0)
        # else:
            y0.append(int(row[0]))
        # if (str(row[1]) == 'None'):
        #     y1.append(0)
        # else:
            y1.append(int(row[1]))
        # if (str(row[2]) == 'None'):
        #     y2.append(0)
        # else:
            y2.append(int(row[2]))

    img = StringIO.StringIO()

    plt.ylabel('No.of Files')
    plt.title('SWT2_CPB - Deletion')

    plt.xlabel("Time in hours (Last 24 hrs)")
    plt.ylabel("No.of files")
    # plt.xticks(x)
    plt.xticks(numpy.arange(0, 24, step=2))
    plt.plot(x, y0, marker='o', color='blue', label='Planned')
    plt.plot(x, y1, marker='^', color='green', label='Done')
    plt.plot(x, y2, marker='*', color='red', label='Failed')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.17), shadow=True, ncol=3)
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.gcf().clear()
    print 'f2'
    return plot_url


def timedelgr3():
    y0 = []
    y1 = []
    y2 = []
    x = []
    query = "select Coalesce(sum(Pfiles),0) as pfiles, Coalesce(sum(dfiles),0) as dfiles, Coalesce(sum(ffiles),0) as ffiles, BatchId from delclusterhistory " \
            "where Destinationsite = 'OU_OSCER_ATLAS' and " \
            "batchId = (select max(BatchId) from delclusterhistory)"
    x.append(1)
    for h in range(1, 24):
        query += " union all select Coalesce(sum(Pfiles),0) as pfiles,Coalesce(sum(dfiles),0) as dfiles,Coalesce(sum(ffiles),0) as ffiles,BatchId from delclusterhistory where Destinationsite='OU_OSCER_ATLAS'" \
                 " and BatchId = (select max(BatchId) -" + str(h) + " from delclusterhistory)"
        x.append(h + 1)


    cursor.execute(query)
    datatimegr = cursor.fetchall()
    # count=0
    # count = cursor.rowcount
    # for i in range(count):
    #     x.append(i + 1)
    for row in datatimegr:
        # count = count+1
        # x.append(int(count))

        # if (str(row[0]) == 'None'):
        #     y0.append(0)
        # else:
            y0.append(int(row[0]))
        # if (str(row[1]) == 'None'):
        #     y1.append(0)
        # else:
            y1.append(int(row[1]))
        # if (str(row[2]) == 'None'):
        #     y2.append(0)
        # else:
            y2.append(int(row[2]))

    img = StringIO.StringIO()

    plt.ylabel('No.of Files')
    plt.title('OU_OSCER_ATLAS - Deletion')

    plt.xlabel("Time in hours (Last 24 hrs)")
    plt.ylabel("No.of files")
    # plt.xticks(x)
    plt.xticks(numpy.arange(0, 24, step=2))
    plt.plot(x, y0, marker='o', color='blue', label='Planned')
    plt.plot(x, y1, marker='^', color='green', label='Done')
    plt.plot(x, y2, marker='*', color='red', label='Failed')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.17), shadow=True, ncol=3)
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.gcf().clear()
    print 'f3'
    return plot_url

def timetransrcgr1():
    # y0 = []
    # y1 = []

    x = []
    # query = "select Coalesce(sum(tfiles),0) as tfiles, Coalesce(sum(ffiles),0) as ffiles, BatchId from transclusterhistory " \
    #         " where sourcesite = 'UTA_SWT2' and " \
    #         " batchId = (select max(BatchId) from transclusterhistory)"
    # x.append(1)
    # for h in range(1, 24):
    #     query += " union all select Coalesce(sum(tfiles),0) as tfiles,Coalesce(sum(ffiles),0) as ffiles,BatchId from transclusterhistory where sourcesite='UTA_SWT2'" \
    #              " and BatchId = (select max(BatchId) -" + str(h) + " from transclusterhistory)"
    #     x.append(h + 1)
    # print query
    # print x
    qmax="select max(BatchId) from transclusterhistory"
    cursor.execute(qmax)
    mbatchidsel=cursor.fetchone()
    mbatchid=0
    for row in mbatchidsel:
        mbatchid=row

    mlbatchid=mbatchid-24


    # query="select sum(tfiles) as tfiles, sum(ffiles)as ffiles, batchid from transclusterhistory where sourcesite = 'UTA_SWT2' " \
    #       "and BatchId between(select max(BatchId) - 23 from transclusterhistory) and (select max(BatchId) from transclusterhistory) "\
    #       "group by BatchId order by BatchId desc"
    query = "SELECT Coalesce(sum(tfiles),0),Coalesce(sum(ffiles),0),BatchId FROM transclusterhistory " \
            "WHERE date(createddate) >= now() - INTERVAL 1 DAY " \
            "and sourcesite='UTA_SWT2' group by BatchId order by BatchId desc"
    print query
    cursor.execute(query)
    datatimegr = cursor.fetchall()
    # count=cursor.rowcount
    # for i in range(count):
    #     x.append(i+1)

    # count=1
    #
    # for row in datatimegr:
    #         if(int(row[2]) == int(mbatchid)):
    #             y0.append(int(row[0]))
    #             y1.append(int(row[1]))
    #
    #         else:
    #             y0.append(0)
    #             y1.append(0)
    #         x.append(count)
    #         count=count+1
    #         mbatchid=mbatchid-1
    y0=[]
    y1=[]
    src1={}
    src2={}
    ind=0

    for i in range(mbatchid,mlbatchid,-1):
        print i
        ind = ind+1
        x.append(ind)
        for row in datatimegr:
                if(i==int(row[2])):
                    # y0.append(int(row[0]))
                    # y1.append(int(row[1]))
                     src1[ind]=int(row[0])
                     src2[ind] = int(row[1])
                else:
                    if(ind not in src1):
                        src1[ind]=0
                    if (ind not in src2):
                        src2[ind] = 0

    print src1
    print src2
    # for h in range(0, 24):
    #     x.append(h + 1)
        # if(h not in src1):
        #     src1[h]=0
        # if (h not in src2):
        #     src2[h] = 0

    y0=list(src1.values())
    y1 = list(src2.values())
    print src1[1]
    print src2[1]
    print y0
    print y1
    print x
    img = StringIO.StringIO()


    plt.ylabel('No.of Files')
    plt.title('UTA_SWT2 - Transfer (Source site)')

    plt.xlabel("Time in hours (Last 24 hrs)")
    plt.ylabel("No.of files")
    plt.xticks(numpy.arange(0, 24, step=2))
    plt.plot(x,y0,marker='^',color='green',label='Transferred')
    plt.plot(x, y1,marker='*',color='red',label='Failed')
        #plt.legend(['Transferred', 'Failed'], loc='upper left')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.17), shadow=True, ncol=2)
        #  plt.legend(bbox_to_anchor=(1.05, 1), loc=3, borderaxespad=0.)
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.gcf().clear()
    print 'f4'
    return plot_url

def timetransrcgr2():
    y0 = []
    y1 = []
    y2 = []
    x = []

    query = "SELECT Coalesce(sum(tfiles),0),Coalesce(sum(ffiles),0),BatchId FROM transclusterhistory " \
            "WHERE date(createddate) >= now() - INTERVAL 1 DAY " \
            "and sourcesite='SWT2_CPB' group by BatchId order by BatchId desc"
    print query

    cursor.execute(query)
    datatimegr = cursor.fetchall()
    # count=0

    print cursor.rowcount
    if(cursor.rowcount==0):
        for h in range(0, 24):
            x.append(h+1)
            y0.append(0)
            y1.append(0)
    else:
        for i in range(cursor.rowcount):
            x.append(i + 1)
        for row in datatimegr:
            # count = count+1
            # x.append(int(count))

            # if (str(row[0]) == 'None'):
            #     y0.append(0)
            # else:
                y0.append(int(row[0]))
            # if (str(row[1]) == 'None'):
            #     y1.append(0)
            # else:
                y1.append(int(row[1]))

    img = StringIO.StringIO()

    plt.ylabel('No.of Files')
    plt.title('SWT2_CPB - Transfer (Source site)')

    plt.xlabel("Time in hours (Last 24 hrs)")
    plt.ylabel("No.of files")
    plt.xticks(numpy.arange(0, 24, step=2))
    plt.plot(x,y0,marker='^',color='green',label='Transferred')
    plt.plot(x, y1,marker='*',color='red',label='Failed')
        #plt.legend(['Transferred', 'Failed'], loc='upper left')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.17), shadow=True, ncol=2)
        #  plt.legend(bbox_to_anchor=(1.05, 1), loc=3, borderaxespad=0.)
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.gcf().clear()
    print 'f5'
    return plot_url

def timetransrcgr3():
    y0 = []
    y1 = []
    y2 = []
    x = []
    query = "SELECT Coalesce(sum(tfiles),0),Coalesce(sum(ffiles),0),BatchId FROM transclusterhistory " \
            "WHERE date(createddate) >= now() - INTERVAL 1 DAY " \
            "and sourcesite='OU_OSCER_ATLAS' group by BatchId order by BatchId desc"

    cursor.execute(query)
    datatimegr = cursor.fetchall()
    # count=0
    count = cursor.rowcount
    for i in range(count):
        x.append(i + 1)
    # count=0
    for row in datatimegr:
        # count = count+1
        # x.append(int(count))

        # if (str(row[0]) == 'None'):
        #     y0.append(0)
        # else:
            y0.append(int(row[0]))
        # if (str(row[1]) == 'None'):
        #     y1.append(0)
        # else:
            y1.append(int(row[1]))


    img = StringIO.StringIO()

    plt.ylabel('No.of Files')
    plt.title('OU_OSCER_ATLAS - Transfer (Source site)')

    plt.xlabel("Time in hours (Last 24 hrs)")
    plt.ylabel("No.of files")
    plt.xticks(numpy.arange(0, 24, step=2))
    plt.plot(x, y0, marker='^', color='green', label='Transferred')
    plt.plot(x, y1, marker='*', color='red', label='Failed')
        #plt.legend(['Transferred', 'Failed'], loc='upper left')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.17), shadow=True, ncol=2)
        #  plt.legend(bbox_to_anchor=(1.05, 1), loc=3, borderaxespad=0.)
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.gcf().clear()
    print 'f6'
    return plot_url

def timetrandesgr1():
    y0 = []
    y1 = []
    y2 = []
    x = []
    query = "SELECT Coalesce(sum(tfiles),0),Coalesce(sum(ffiles),0),BatchId FROM transclusterhistory " \
            "WHERE date(createddate) >= now() - INTERVAL 1 DAY " \
            "and destinationsite='UTA_SWT2' group by BatchId order by BatchId desc"

    cursor.execute(query)
    datatimegr = cursor.fetchall()
    # count=0
    count = cursor.rowcount
    for i in range(count):
        x.append(i + 1)
    # count=0
    for row in datatimegr:
        # count = count+1
        # x.append(int(count))

        # if (str(row[0]) == 'None'):
        #     y0.append(0)
        # else:
            y0.append(int(row[0]))
        # if (str(row[1]) == 'None'):
        #     y1.append(0)
        # else:
            y1.append(int(row[1]))

    img = StringIO.StringIO()

    plt.ylabel('No.of Files')
    plt.title('UTA_SWT2 - Transfer (Destination site)')

    plt.xlabel("Time in hours (Last 24 hrs)")
    plt.ylabel("No.of files")
    plt.xticks(numpy.arange(0, 24, step=2))
    plt.plot(x, y0, marker='^', color='green', label='Transferred')
    plt.plot(x, y1, marker='*', color='red', label='Failed')
        #plt.legend(['Transferred', 'Failed'], loc='upper left')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.17), shadow=True, ncol=2)
        #  plt.legend(bbox_to_anchor=(1.05, 1), loc=3, borderaxespad=0.)
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.gcf().clear()
    print 'f7'
    return plot_url

def timetrandesgr2():
    y0 = []
    y1 = []
    y2 = []
    x = []
    query = "SELECT Coalesce(sum(tfiles),0),Coalesce(sum(ffiles),0),BatchId FROM transclusterhistory " \
            "WHERE date(createddate) >= now() - INTERVAL 1 DAY " \
            "and destinationsite='SWT2_CPB' group by BatchId order by BatchId desc"

    cursor.execute(query)
    datatimegr = cursor.fetchall()
    # count=0
    count = cursor.rowcount
    for i in range(count):
        x.append(i + 1)
    # count=0
    for row in datatimegr:
        # count = count+1
        # x.append(int(count))

        # if (str(row[0]) == 'None'):
        #     y0.append(0)
        # else:
            y0.append(int(row[0]))
        # if (str(row[1]) == 'None'):
        #     y1.append(0)
        # else:
            y1.append(int(row[1]))

    img = StringIO.StringIO()

    plt.ylabel('No.of Files')
    plt.title('SWT2_CPB - Transfer (Destination site)')

    plt.xlabel("Time in hours (Last 24 hrs)")
    plt.ylabel("No.of files")
    plt.xticks(numpy.arange(0, 24, step=2))
    plt.plot(x, y0, marker='^', color='green', label='Transferred')
    plt.plot(x, y1, marker='*', color='red', label='Failed')
        #plt.legend(['Transferred', 'Failed'], loc='upper left')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.17), shadow=True, ncol=2)
        #  plt.legend(bbox_to_anchor=(1.05, 1), loc=3, borderaxespad=0.)
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.gcf().clear()
    print 'f8'
    return plot_url


def timetrandesgr3():
    y0 = []
    y1 = []
    y2 = []
    x = []
    query = "SELECT Coalesce(sum(tfiles),0),Coalesce(sum(ffiles),0),BatchId FROM transclusterhistory " \
            "WHERE date(createddate) >= now() - INTERVAL 1 DAY " \
            "and destinationsite='OU_OSCER_ATLAS' group by BatchId order by BatchId desc"

    cursor.execute(query)
    datatimegr = cursor.fetchall()
    # count=0
    count = cursor.rowcount
    for i in range(count):
        x.append(i + 1)
    # count=0
    for row in datatimegr:
        # count = count+1
        # x.append(int(count))
        #
        # if (str(row[0]) == 'None'):
        #     y0.append(0)
        # else:
            y0.append(int(row[0]))
        # if (str(row[1]) == 'None'):
        #     y1.append(0)
        # else:
            y1.append(int(row[1]))

    img = StringIO.StringIO()

    plt.ylabel('No.of Files')
    plt.title('OU_OSCER_ATLAS - Transfer (Destination site)')

    plt.xlabel("Time in hours (Last 24 hrs)")
    plt.ylabel("No.of files")
    plt.xticks(numpy.arange(0, 24, step=2))
    plt.plot(x, y0, marker='^', color='green', label='Transferred')
    plt.plot(x, y1, marker='*', color='red', label='Failed')

        #plt.legend(['Transferred', 'Failed'], loc='upper left')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.17), shadow=True, ncol=2)
        #  plt.legend(bbox_to_anchor=(1.05, 1), loc=3, borderaxespad=0.)
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.gcf().clear()
    print 'f9'
    return plot_url




