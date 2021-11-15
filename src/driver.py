import xml.etree.ElementTree as et
# import request
from util import run_sql
import xml.dom.minidom as MD
import snowflake.connector

relationship = "DRIVER_RELATIONSHIPTOPROPOSER"
dateOfBirth = "DRIVER_DATEOFBIRTH"
maritalStatus = "DRIVER_MARITALSTATUS"
type = "DRIVER_LICENCETYPE"
DRIVER_LICENCEDATE = "DRIVER_LICENCEDATE"
ukResident = "DRIVER_UKRESIDENCYDATE"
useOtherVehicle = "DRIVER_OTHERVEHICLEOWNEDIND"
driverId = "DRIVER_PRN"
lastName = "DRIVER_SURNAME"
firstName = "DRIVER_FORENAMEINITIAL1"
title = "DRIVER_TITLE"
medicalConditions = "DRIVER_MEDICALCONDITIONIND"
employmentOccupationDesc = "OCCUPATION_DESCRIPTION"
employmentBusinessDesc = "OCCUPATION_BUSINESSDESC"
addressLine1 = "PROPOSERPOLICYHOLDER_ADDRESSLINE1"
postCode = "PROPOSERPOLICYHOLDER_POSTCODEFULL"
employmentStatusCode = "OCCUPATION_EMPLOYMENTTYPE"
employmentOccupationCode = "OCCUPATION_CODE"
employmentBusinessCode = "OCCUPATION_EMPLOYERSBUSINESS"
employmentBusinessDesc = "OCCUPATION_DESCRIPTION"
lengthHeld = "DRIVER_LICENCEDATE"
number = "DRIVER_LICENCENUMBER"
primaryEmail = "PROPOSERPOLICYHOLDER_EMAIL"
homeOwner = "DRIVER_HOMEOWNERIND"
ukResident = "DRIVER_NOOFYEARSUKRESIDENCY"
titleDesc = "titleDesc"


def change_name(xml):
    # xml must be an ET tree object
    attribute_order = f"{title}, {titleDesc}, {firstName}, {firstName}"
    sql = f"select {attribute_order} from PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ_VEHICLE where QUOTE_REFERENCE ='10358790597'"
    tag_values = run_sql(sql)
    attri = xml.find('fullName')
    for i in range(0, len(tag_values[0])):
        attri[i].text = tag_values[i]


def fill_driver(xml):
    r = xml.find("policyholder")
    for name_attributes in r:
        print(name_attributes.tag)


def check_for_layer(tree_tag):
    if len(tree_tag) == 1:
        return True


if __name__ == '__main__':
    tree = et.parse("../res/sample.xml")
    for string in tree.iter('car'):
        for driver_attributes in string:
                print(driver_attributes.tag)
    for string in tree.iter('policyholder'):
        for driver_attributes in string:
            if driver_attributes.tag == 'name':
                change_name(driver_attributes)
            else:
                print(driver_attributes.tag)
