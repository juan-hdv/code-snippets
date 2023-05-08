from datetime import datetime

def coerce_into_date_in_dict(dic: dict, datetime_fields: list):
    """ Apply coerce_into_date to all the datetime fields in datetime_fields """
    for f in datetime_fields:
        field_list = f.split(".")
        obj = dic
        for key in field_list[0:-1]:
            obj = obj[key]
        key = field_list[-1]
        obj[key] = obj[key].date()
    return dic

d = {
    "start_date":{
        "metadata":{
            "job_start_date":datetime (2022,5,4,8,7,6,5),
        }
    },
    "start_date_x":{
        "job_start_date":datetime (2022,5,4,8,7,6,5),
    }
}

fields =["start_date.metadata.job_start_date", "start_date_x.job_start_date"]
result = coerce_into_date_in_dict (d, fields)
print (result)
