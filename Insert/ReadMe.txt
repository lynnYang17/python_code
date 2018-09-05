#-----------------------------------作用说明-----------------------------------------
针对mstar台表，需要从搜台log中对应每个信息字段到customer.sql文件中，需要人工操作的费时费力问题，
现生成sql_opt.py脚本，可以直接生成atv和dtv表的insert语句，copy到sql文件中对应位置。



#-----------------------------------使用说明-----------------------------------------
脚本中的处理分为两部分，上半部分是对ATV log的处理，下半部分是对DTV log的处理
1. 修改atv/dtv的log文件名为：atv_log.txt/dtv_log.txt

2. 删除atv_log.txt/dtv_log.txt中的多余部分，将每个台的一组信息规整到一个段落中，详见atv_log.txt

3. 将atv_log.txt/dtv_log.txt和sql_opt.py放到同一路径下，运行“python sql_opt.py”执行脚本，执行成功后会打印出‘atv_done’'dtv_done'的信息，
   并且生成insert_atv.txt/insert_dtv.txt 和 atv_dict.txt/dtv_dict.txt，其中insert_xtv.txt中的insert语句是需要copy到customer.sql文件中的。


   必须要注意的是: log中的字段并不能完全涵盖sql文件中的所有字段，所以一些字段需要手动在脚本中自己修改：

   atv固定字段:
   #需要手动设置的固定字段：
   ['u8CityIndex']: 根据工厂代码中的所以值确定，比如BOE的所以值为7，那么它的u8CityIndex字段就为7；
   ['u8AtvProgramCount']: 台的个数，从log中可以看出。BOE有4个ATV台，那么u8AtvProgramCount字段为4。(脚本不能自动计算出有几个台)
   #脚本中已经默认设置的固定字段：
   ['u8AtvProgramIndex']: 该字段在log中没有，但是脚本可以自动累加。是从0-15，sql中为每个工厂预留了16个台的位置。


   dtv固定字段：
   #需要手动设置的固定字段：
   ['u8CityIndex']: 根据工厂代码中的所以值确定，比如BOE的所以值为7，那么它的u8CityIndex字段就为7；
   ['u8DtvProgramCount']: 台的个数，从log中可以看出。BOE有4个ATV台，那么u8AtvProgramCount字段为4。(脚本不能自动计算出有几个台)
   #脚本中已经默认设置的固定字段：
   ['u8QAMMode']: 都是DTMB格式，都为0
   ['u32SymbolRate']: 6875
   ['u16SourceId']: 0
   ['u8VctVersion']: 0
   ['u8RrtVersion']: 0

