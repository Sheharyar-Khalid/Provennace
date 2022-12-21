from elasticsearch import Elasticsearch
from elasticsearch.client import EqlClient
import json
import threading
from datetime import datetime


def queryelastic(x):
    client = Elasticsearch("http://localhost:9200",timeout =100000000)
    index2 = ['cadets75','cadets76','cadets77','cadets78','cadets79','cadets80','cadets81','cadets82','cadets83','cadets84','cadets85','cadets86','cadets87','cadets88','cadets89','cadets90','cadets91','cadets92','cadets93','cadets94','cadets95','cadets96','cadets97','cadets98','cadets99','cadets100','cadets101','cadets102','cadets103','cadets104','cadets105','cadets106','cadets107','cadets108','cadets109','cadets110','cadets111','cadets112','cadets113','cadets114']
    eql = EqlClient(client)

    start = datetime.now().strftime("%H:%M:%S")
    # resultini = client.search(index=index2,query={"bool": {"must" : [{"query_string": {"query": "*bongalk*"}}]}})
    # resultini = eql.search(index=index2,query=x,expand_wildcards='all')
    print('Thread Started KQL')
    resultini = client.search(index="cadets*",query={"bool": {"must" : [{"query_string": {"query": x}}]}},request_cache=False, expand_wildcards='all')
    end = datetime.now().strftime("%H:%M:%S")
    print(start, ', ', end, ', ', resultini['took'], ', ', resultini)

def queryelasticEQL(x):
    client = Elasticsearch("http://localhost:9200",timeout =100000000)
    index2 = ['cadets75','cadets76','cadets77','cadets78','cadets79','cadets80','cadets81','cadets82','cadets83','cadets84','cadets85','cadets86','cadets87','cadets88','cadets89','cadets90','cadets91','cadets92','cadets93','cadets94','cadets95','cadets96','cadets97','cadets98','cadets99','cadets100','cadets101','cadets102','cadets103','cadets104','cadets105','cadets106','cadets107','cadets108','cadets109','cadets110','cadets111','cadets112','cadets113','cadets114']
    eql = EqlClient(client)

    start = datetime.now().strftime("%H:%M:%S")
    # resultini = client.search(index=index2,query={"bool": {"must" : [{"query_string": {"query": "*bongalk*"}}]}})
    print('Thread Started EQL')
    resultini = eql.search(index=index2,query=x,expand_wildcards='all')
    end = datetime.now().strftime("%H:%M:%S")
    print(start, ', ', end, ', ', resultini['took'], ', ', resultini)


x = """sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*elevate_*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid """

x = [
    "*.12.59","*.xx.59","*.12.*","*dasdn*","python*","*chrome*","sad", "*nda*", "*ab*dj*", "192*", "*dasd*","hell*", "*ngin*","*elevate*","*macho*", "*ola*", "*malware*", "cadets*", "*collg*","*heasj*", "dasd*","*12.H*","*1*2*hello","*bas*","*hog*","*ha*", "*//nginx", "*elvaj_*", "*rand*","sadad*","*hasjd*", "*7&*8aa*","*lolol*", "*.12.*.a*", "*jsad*", "*non*","pta*","*approv*ed","*phon*ne","*0800*17ab*","*record*noaho*","net*chup*","120.*ba*","remo*add*naop*","*help*nhi","kalo*","*tho*718*","*pl*se*h*","*alm*st*g","*fifty*sn*","*.50.s","*.yy.77*","*.21un*","*asd*","chaios*","*choas*","*happ", "*asnd*", "*d*as*", "78t78*", "*asd*","fassd*", "*sda*","*sad*","*ad*", "*asda*", "*theao*", "cadetsdsd*", "*e//ect*","*//etc*", "c12*","*12.dsf*","*1*2*etc","*sdetc*","*passwd*","*asd*", "*//not", "*vsdds*", "*vdf64*","dg3*","*vxcv*", "*7&*8axza*","*xzc*", "*.12.*.a*", "*fsf*", "*fnds*","*dms*","*asd*1","*asd*12","*12sc*sad*","cord*12as*","mxa*ad*","asd.*12e*","xc*msa*asd*","*nott*ss","as*","*cs*ss*","*ss*asd*h*","*fas*f*g","*fas*sn*"]
y = [
    """sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*elevate_*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*elevate_*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*elevate_*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*ansdk*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*notda*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*kasd*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*chrome*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*asd*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*nginx*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*pythonn*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*py*on.*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*sad*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*dasf*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*1223*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*2123(*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*asd,kk*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*jasd1*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*sds1*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*asdc*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid ""","""sequence [any where message.datum.com.bbn.tc.schema.avro.cdm20.Event.properties.map.cmdLine : "*cx*"] by message.datum.com.bbn.tc.schema.avro.cdm20.Event.subject.com.bbn.tc.schema.avro.cdm20.UUID [any where message.type == "RECORD_SUBJECT"] by message.datum.com.bbn.tc.schema.avro.cdm20.Subject.uuid """]

threads = []
for i in range(0,100):
    try:
        threads.append(threading.Thread(target=queryelastic, args=(x[i],)))
        threads[i].start()
    except:
        print('error in ',x[i])

for i in range(0,20):
    k =i+100
    try:
        threads.append(threading.Thread(target=queryelasticEQL, args=(y[i],)))
        threads[k].start()
    except:
        print('error in ',y[i])

# print(threads)
for i in range(0,120):
    try:
        threads[i].join
    except:
        print(i)

# print(threads)
# t2.join()


print("Done!")
