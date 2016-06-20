from datetime import datetime


def import_file(pathstr,splitterstr,condition_value=str(), condition_index=int(), operator="in", length=100000000,
                columns=[]):
    start = datetime.now()

    path=str(pathstr)
    splitter=str(splitterstr)



    # index #=int(condition_index)
    # value=condition_value


    print path.split("/")[-1], " beginning processing at ", start

    f = open(path, 'U')

    data = []
    rows=[]
    for row in f:
        if row not in rows:
            rows.append(row)
            if len(data) <= length:
                if condition_value in str(row):

                    value = row.split(splitter)
                    value[-1]=value[-1][0:-1]
                    #print value
                    if type(condition_index)==int:
                        if operator == "==":
                            if value[condition_index] == condition_value:
                                info=[]
                                if columns !=[]:
                                    for i in columns:
                                        info.append(value[i])
                                    data.append(info)
                                else: data.append(value)
                        if operator == "!=":
                            if value[condition_index] != condition_value:
                                info=[]
                                if columns !=[]:
                                    for i in columns:
                                        info.append(value[i])
                                    data.append(info)
                                else:data.append(info)
                        if operator == "in":
                            if condition_value in value[condition_index]:
                                info=[]
                                if columns !=[]:
                                    for i in columns:
                                        info.append(value[i])
                                    data.append(info)
                                else:data.append(info)
                    else: data.append(value)
    print len(data)
    f.close()
    titles=data[0]
    data=data[1:]
    end=datetime.now()
    duration = end - start
    rows=[]
    print data[:5]
    print path.split("/")[-1], ' data parsed and assigned as of', end,'. Time taken: ', duration
    return titles, data
