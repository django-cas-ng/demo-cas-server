groups = [
    "harvard:ref:courses:ext:1900:ongoing:406122-staff",
    "harvard:ref:courses:ext:2013:fall:328457-enrollees",
    "harvard:ref:courses:ext:2013:fall:328995-enrollees",
    "harvard:ref:courses:ext:2013:spring:328479-enrollees",
    "harvard:ref:courses:ext:2013:spring:328484-enrollees",
    "harvard:ref:courses:ext:2013:winter:329878-enrollees",
    "harvard:ref:courses:ext:2014:fall:349239-enrollees",
    "harvard:ref:courses:ext:2014:fall:349892-enrollees",
    "harvard:ref:courses:ext:2014:spring:349217-enrollees",
    "harvard:ref:courses:ext:2015:fall:358334-enrollees",
    "harvard:ref:courses:ext:2015:fall:358998-enrollees",
    "harvard:ref:courses:ext:2015:spring:358339-enrollees",
    "harvard:ref:courses:ext:2016:fall:397249-enrollees",
    "harvard:ref:courses:ext:2016:fall:397316-enrollees",
]


# Create your views here.
def custom_attributes(user, service):

    return {"memberOf": "harvard:ref:courses:ext:1900:ongoing:406122-staff"}
