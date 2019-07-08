#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
#---------------ATV---------------------
CREATE TABLE [tbl_ATVDefaultPrograms] (
  [u8CityIndex] INTEGER  NULL,          #根据Factory code中给的参数确定
  [u8AtvProgramIndex] INTEGER  NULL,    #从0-15，共有16个索引
  [u8AtvProgramCount] INTEGER  NULL,    #log中共有几组台的数据，则为 几 个台
  [u32FrequencyKHz] INTEGER  NULL,      #频点，log中FACTORY:<< 55250 KHz中的 55250
  [AudioStandard] INTEGER  NULL,        #AudioStandard，log中AudioStandard=10中的 10
  [VideoStandard] INTEGER  NULL,        #VideoStandard，log中VideoStandard=1中的 1
  PRIMARY KEY ([u8CityIndex],[u8AtvProgramIndex])       #主键为：[u8CityIndex, u8AtvProgramIndex]
 );

atv insert:
INSERT INTO "tbl_ATVDefaultPrograms" VALUES(2,13,2,0,0,0);

#-------------DTV----------------------
CREATE TABLE [tbl_DTVDefaultPrograms] (
 [u8CityIndex] INTEGER  NULL,           #根据Factory code中给的参数确定
 [u8DtvRouteMode] INTEGER  NULL,        #都是DTMB格式，都为 0
 [u8DtvProgramCount] INTEGER  NULL,     #log中共有几组台的数据，则为 几 个台，可直接从log中看出，也可以由log中的数据组计算得到
 [u8DtvProgramIndex] INTEGER  NOT NULL, #从0-15，共有16个索引
 [u8RfChNumber] INTEGER  NULL,          #区间为[0,台的个数)，左闭右开；如有3个台，前三个的u8RfChNumber为0，1，2，其余全部为0
 [u8QAMMode] INTEGER  NULL,             #log中无对应字段，都为 0
 [u32Frequency] INTEGER  NULL,          #频点，u32Frequency=586000中的 586000
 [u32SymbolRate] INTEGER  NULL,         #固定，填 6875
 [u16TSID] INTEGER  NULL,               #u16TSID=1,u16ONID=1,u16NID=0
 [u16ONID] INTEGER  NULL,               #u16TSID=1,u16ONID=1,u16NID=0
 [u16NID] INTEGER  NULL,                #u16TSID=1,u16ONID=1,u16NID=0
 [u16PCRPID] INTEGER  NULL,             #PCR Pid: 0x0065中的  0x0065 转化为十进制的 101
 [u16LCN] INTEGER  NULL,                #LCN 65535中的 65535 或者 simuLCN 65535中的 65535
 [u16PmtPID] INTEGER  NULL,             #PMT Pid: 0x0020 中的 0x0020 转化为十进制的 32
 [u16ServiceID] INTEGER  NULL,          #Service ID: 0x000b中的 0x000b 转化为十进制的 12
 [u16SourceId] INTEGER  NULL,           #log中无对应字段，都为 0
 [u16VideoPID] INTEGER  NULL,           #Vid Pid: 0x0065 中的 0x0065 转为十进制的 101
 [u16AudioPID] INTEGER  NULL,           #aud[0] type[0],FACTORY:ISO[CHI]  Pid[0x3e9] 中的Pid后边的0x3e9 转为十进制的 1001
 [u8VideoType] INTEGER  NULL,           #video type: 2中的 2
 [u8AudioType] INTEGER  NULL,           #aud[0] type[0],FACTORY:ISO[CHI]  Pid[0x3e9] 中的 type[0]中的 0
 [u8NITVersion] INTEGER  NULL,          #u8NITVersion=255,u8PatVer=0,u8PMTVersion=0,u8SDTVersion=0
 [u8PATVersion] INTEGER  NULL,          #u8NITVersion=255,u8PatVer=0,u8PMTVersion=0,u8SDTVersion=0
 [u8PMTVersion] INTEGER  NULL,          #u8NITVersion=255,u8PatVer=0,u8PMTVersion=0,u8SDTVersion=0
 [u8SDTVersion] INTEGER  NULL,          #u8NITVersion=255,u8PatVer=0,u8PMTVersion=0,u8SDTVersion=0
 [u8VctVersion] INTEGER  NULL,          #都填 0
 [u8RrtVersion] INTEGER  NULL,          #都填 0
 PRIMARY KEY ([u8CityIndex],[u8DtvProgramIndex])    #主键为：[u8CityIndex, u8AtvProgramIndex]
 );

dtv insert:
INSERT INTO "tbl_DTVDefaultPrograms" VALUES(6,0,12,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);
"""
#  -----------------------------ATV--------------------------------------
atv_dict = {'u8CityIndex': 6, 'u8AtvProgramIndex': 0, 'u8AtvProgramCount': 3,
            'u32FrequencyKHz': 0, 'AudioStandard': 0, 'VideoStandard': 0}

fa = open('atv_log.txt', 'r')
fa1 = open("atv_dict.txt", "w")
fa2 = open("insert_atv.txt", "w")
i = 0
resa = 'INSERT INTO "tbl_ATVDefaultPrograms" VALUES'
for line in fa:
    line = line.strip()
    if len(line) < 10:
        continue
    #if i & 1:
    if line.find('VideoStandard') > 0:
        #print i,line
        a = line.split(' ')[-1].split('=')[1]
        atv_dict['VideoStandard'] = a
        print >> fa1, atv_dict
        insert_atv = resa + '(' + str(atv_dict['u8CityIndex']) + ',' + str(atv_dict['u8AtvProgramIndex']) + ',' + str(atv_dict['u8AtvProgramCount']) \
                  + ',' + str(atv_dict['u32FrequencyKHz']) + ',' + str(atv_dict['AudioStandard']) + ',' + str(atv_dict['VideoStandard']) + ');'
        print >> fa2, insert_atv
        atv_dict['u8AtvProgramIndex'] += 1
    #elif not i & 1:
    elif line.find('FACTORY:<< ') > 0 and line.find('u32FrequencyKHz') > 0:
        path = 'FACTORY:<< '
        a = line[line.find(path):].split(' ')
        atv_dict['u32FrequencyKHz'] = a[1]
        a = a[4].split(':')[1].split('=')[1]
        print a
        atv_dict['AudioStandard'] = a

    #print line
    i += 1

atv_dict = {'u8CityIndex': 6, 'u8AtvProgramIndex': 0, 'u8AtvProgramCount': 3,
            'u32FrequencyKHz': 0, 'AudioStandard': 0, 'VideoStandard': 0}
atv_dict['u8AtvProgramIndex'] = atv_dict['u8AtvProgramCount']
for i in range(atv_dict['u8AtvProgramIndex'], 16, 1):
    insert_atv = resa + '(' + str(atv_dict['u8CityIndex']) + ',' + str(atv_dict['u8AtvProgramIndex']) + ',' + \
                 str(atv_dict['u8AtvProgramCount']) + ',' + str(atv_dict['u32FrequencyKHz']) + ',' + \
                 str(atv_dict['AudioStandard']) + ',' + str(atv_dict['VideoStandard']) + ');'
    atv_dict['u8AtvProgramIndex'] += 1
    print >> fa2, insert_atv
fa.close()
fa1.close()
fa2.close()
print 'done_atv'

#  -----------------------------------DTV--------------------------------------------
dtv_dict = {'u8CityIndex': 6, 'u8DtvRouteMode': 0, 'u8DtvProgramCount': 12, 'u8DtvProgramIndex': 0, 'u8RfChNumber': 0,
            'u8QAMMode': 0, 'u32Frequency': 0, 'u32SymbolRate': 0, 'u16TSID': 0, 'u16ONID': 0,'u16NID': 0,
            'u16PCRPID': 0, 'u16LCN': 0, 'u16PmtPID': 0, 'u16ServiceID': 0,'u16SourceId': 0, 'u16VideoPID': 0,
            'u16AudioPID': 0, 'u8VideoType': 0, 'u8AudioType': 0,'u8NITVersion': 0, 'u8PATVersion': 0,
            'u8PMTVersion': 0, 'u8SDTVersion': 0, 'u8VctVersion': 0, 'u8RrtVersion': 0}

fd = open("dtv_log.txt", "r")
fd1 = open("dtv_dict.txt", "w")
fd2 = open("insert_dtv.txt", "w")
cnt = 0
resd = 'INSERT INTO "tbl_DTVDefaultPrograms" VALUES'
for i in fd:
    cnt += 1
    s = i.strip()
    if len(i) < 10:
        cnt = 0
        continue
    if s.find('simuLCN') > 0:
        dtv_dict['u16LCN'] = s.split(' ')[-1]
    elif s.find('Vid Pid') > 0:
        dtv_dict['u16VideoPID'] = int(s.split(' ')[-1][2:], 16)
    elif s.find('video type') > 0:
        dtv_dict['u8VideoType'] = s.split(' ')[-1]
    elif s.find('PMT Pid') > 0:
        dtv_dict['u16PmtPID'] = int(s.split(' ')[-1][2:], 16)
    elif s.find('PCR Pid') > 0:
        dtv_dict['u16PCRPID'] = int(s.split(' ')[-1][2:], 16)
    elif s.find('Service ID:') > 0:
        dtv_dict['u16ServiceID'] = int(s.split(' ')[-1][2:], 16)
    elif s.find('aud') > 0 and s.find('Pid') > 0:
        dtv_dict['u8AudioType'] = s.split(' ')[13].split(',')[0].split(']')[0].split('[')[1]
        dtv_dict['u16AudioPID'] = int(s.split(' ')[-1].split(']')[0].split('[')[1][2:], 16)
    elif s.find('u16TSID') > 0 and s.find('u16ONID') > 0 and s.find('u16NID') > 0:
        dtv_dict['u16TSID'] = s.split(' ')[-1].split(',')[0].split('=')[-1]
        dtv_dict['u16ONID'] = s.split(' ')[-1].split(',')[1].split('=')[-1]
        dtv_dict['u16NID'] = s.split(' ')[-1].split(',')[2].split('=')[-1]
    elif s.find('u32Frequency') > 0:
        dtv_dict['u32Frequency'] = s.split(' ')[-1].split('=')[-1]
    elif s.find('u8NITVersion') > 0 and s.find('u8PatVer') > 0 and s.find('u8PMTVersion') > 0 and s.find('u8SDTVersion') > 0:
        dtv_dict['u8NITVersion'] = s.split(' ')[-1].split(',')[0].split('=')[-1]
        dtv_dict['u8PatVer'] = s.split(' ')[-1].split(',')[1].split('=')[-1]
        dtv_dict['u8PMTVersion'] = s.split(' ')[-1].split(',')[2].split('=')[-1]
        dtv_dict['u8SDTVersion'] = s.split(' ')[-1].split(',')[3].split('=')[-1]
        dtv_dict['u8DtvRouteMode'] = 0
        dtv_dict['u8QAMMode'] = 0
        dtv_dict['u32SymbolRate'] = 6875
        dtv_dict['u16SourceId'] = 0
        dtv_dict['u8VctVersion'] = 0
        dtv_dict['u8RrtVersion'] = 0
        print >> fd1, dtv_dict
        insert_dtv = resd + '(' + str(dtv_dict['u8CityIndex']) + ',' + str(dtv_dict['u8DtvRouteMode']) + ',' + \
                     str(dtv_dict['u8DtvProgramCount']) + ',' + str(dtv_dict['u8DtvProgramIndex']) + ',' + \
                     str(dtv_dict['u8RfChNumber']) + ',' + str(dtv_dict['u8QAMMode']) + ',' + \
                     str(dtv_dict['u32Frequency']) + ',' + str(dtv_dict['u32SymbolRate']) + ',' + \
                     str(dtv_dict['u16TSID']) + ',' + str(dtv_dict['u16ONID']) + ',' + str(dtv_dict['u16NID']) + ',' + \
                     str(dtv_dict['u16PCRPID']) + ',' + str(dtv_dict['u16LCN']) + ',' + \
                     str(dtv_dict['u16PmtPID']) + ',' + str(dtv_dict['u16ServiceID']) + ',' \
                     + str(dtv_dict['u16SourceId']) + ',' + str(dtv_dict['u16VideoPID']) + ',' + \
                     str(dtv_dict['u16AudioPID']) + ',' + str(dtv_dict['u8VideoType']) + ',' + \
                     str(dtv_dict['u8AudioType']) + ',' + str(dtv_dict['u8NITVersion']) + ',' + \
                     str(dtv_dict['u8PATVersion']) + ',' + str(dtv_dict['u8PMTVersion']) + ',' + \
                     str(dtv_dict['u8SDTVersion']) + ',' + str(dtv_dict['u8VctVersion']) + ',' + \
                     str(dtv_dict['u8RrtVersion']) + ');'
        print >> fd2, insert_dtv
        dtv_dict['u8DtvProgramIndex'] += 1
        dtv_dict['u8RfChNumber'] += 1

dtv_dict = {'u8CityIndex': 6, 'u8DtvRouteMode': 0, 'u8DtvProgramCount': 12, 'u8DtvProgramIndex': 0, 'u8RfChNumber': 0,
            'u8QAMMode': 0, 'u32Frequency': 0, 'u32SymbolRate': 0, 'u16TSID': 0, 'u16ONID': 0,'u16NID': 0,
            'u16PCRPID': 0, 'u16LCN': 0, 'u16PmtPID': 0, 'u16ServiceID': 0,'u16SourceId': 0, 'u16VideoPID': 0,
            'u16AudioPID': 0, 'u8VideoType': 0, 'u8AudioType': 0,'u8NITVersion': 0, 'u8PATVersion': 0,
            'u8PMTVersion': 0, 'u8SDTVersion': 0, 'u8VctVersion': 0, 'u8RrtVersion': 0}
dtv_dict['u8DtvProgramIndex'] = dtv_dict['u8DtvProgramCount']

for i in range(dtv_dict['u8DtvProgramCount'], 16, 1):
    insert_dtv = resd + '(' + str(dtv_dict['u8CityIndex']) + ',' + str(dtv_dict['u8DtvRouteMode']) + ',' + \
                 str(dtv_dict['u8DtvProgramCount']) + ',' + str(dtv_dict['u8DtvProgramIndex']) + ',' + \
                 str(dtv_dict['u8RfChNumber']) + ',' + str(dtv_dict['u8QAMMode']) + ',' + \
                 str(dtv_dict['u32Frequency']) + ',' + str(dtv_dict['u32SymbolRate']) + ',' + \
                 str(dtv_dict['u16TSID']) + ',' + str(dtv_dict['u16ONID']) + ',' + str(dtv_dict['u16NID']) + ',' + \
                 str(dtv_dict['u16PCRPID']) + ',' + str(dtv_dict['u16LCN']) + ',' + \
                 str(dtv_dict['u16PmtPID']) + ',' + str(dtv_dict['u16ServiceID']) + ',' \
                 + str(dtv_dict['u16SourceId']) + ',' + str(dtv_dict['u16VideoPID']) + ',' + \
                 str(dtv_dict['u16AudioPID']) + ',' + str(dtv_dict['u8VideoType']) + ',' + \
                 str(dtv_dict['u8AudioType']) + ',' + str(dtv_dict['u8NITVersion']) + ',' + \
                 str(dtv_dict['u8PATVersion']) + ',' + str(dtv_dict['u8PMTVersion']) + ',' + \
                 str(dtv_dict['u8SDTVersion']) + ',' + str(dtv_dict['u8VctVersion']) + ',' + \
                 str(dtv_dict['u8RrtVersion']) + ');'
    print >> fd2, insert_dtv
    dtv_dict['u8DtvProgramIndex'] += 1
fd.close()
fd1.close()
fd2.close()
print 'done_dtv'
