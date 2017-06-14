## In this guided script, we'll continue working with the same dataset, compiled by FiveThirtyEight
## "US_births_1994-2003_CDC_NCHS.csv"


## Introduction To The Dataset

US_birth = open("US_births_1994-2003_CDC_NCHS.csv", "r").read()
US_birth1 = US_birth.split("\n")
US_birth1[0:10]


## Converting Data Into A List Of Lists

# A customize function for reading the dataset, converting into the list and convert every element to integer
def read_csv(filename):
    string_list = open(filename).read()
    string_list = string_list.split("\n")
    g = len(string_list)
    string_list = string_list[1:g-1]
    final_list = []
    for i in string_list:
        int_fields = []
        string_fields = i.split(",")
        for p in string_fields:
            gint = int(p)
            int_fields.append(gint)
        final_list.append(int_fields)
    return(final_list)


cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
cdc_list[0:10]


## Calculating Number Of Births Each Month

def month_births(list):
    births_per_month = {}
    for i in list:
        month_ext = i[1]
        birth_ext = int(i[4])
        if month_ext in births_per_month:
            births_per_month[month_ext] = births_per_month[month_ext] + birth_ext
        else:
            births_per_month[month_ext] = birth_ext
            
    return(births_per_month)

cdc_month_births = month_births(cdc_list)

cdc_month_births


## Calculating Number Of Births Each Day Of Week

def dow_births(list_name):
    birth_day = {}
    for i in list_name:
        day_ext = i[3]
        birth_ext = i[4]
        if day_ext in birth_day:
            birth_day[day_ext] = birth_day[day_ext] + i[4]
        else:
            birth_day[day_ext] = i[4]
    return(birth_day)

cdc_day_births = dow_births(cdc_list)


## Creating A More General Function

def calc_counts(data, column):
    births = {}
    if (column=="year"):
        for i in data:
            year_birth = i[0]
            if year_birth in births:
                births[year_birth] = births[year_birth] + i[4]
            else:
                births[year_birth] = i[4]
                    
    if (column=="month"):
        for i in data:
            month_birth = i[1]
            if month_birth in births:
                births[month_birth] = births[month_birth] + i[4]
            else:
                births[month_birth] = i[4]
        
    if (column=="date_of_month"):
        for i in data:
            date_birth = i[2]
            if date_birth in births:
                births[date_birth] = births[date_birth] + i[4]
            else:
                births[date_birth] = i[4]
                    
    if (column=="day_of_week"):
        for i in data:
            day_birth = i[3]
            if day_birth in births:
                births[day_birth] = births[day_birth] + i[4]
            else:
                births[day_birth] = i[4]
    
    return(births)
                


cdc_year_births = calc_counts(cdc_list, column = "year")
cdc_month_births = calc_counts(cdc_list, column = "month")
cdc_dom_births = calc_counts(cdc_list, column = "date_of_month")
cdc_dow_births = calc_counts(cdc_list, column = "day_of_week")


## END
