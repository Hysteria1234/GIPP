import xml.etree.ElementTree as et
# import request
from util import *
import xml.dom.minidom as MD
import snowflake.connector

# relationship = "DRIVER_RELATIONSHIPTOPROPOSER"
# dateOfBirth = "DRIVER_DATEOFBIRTH"
# maritalStatus = "DRIVER_MARITALSTATUS"
# type = "DRIVER_LICENCETYPE"
# DRIVER_LICENCEDATE = "DRIVER_LICENCEDATE"
# ukResident = "DRIVER_UKRESIDENCYDATE"
# useOtherVehicle = "DRIVER_OTHERVEHICLEOWNEDIND"
# driverId = "DRIVER_PRN"
# lastName = "DRIVER_SURNAME"
# firstName = "DRIVER_FORENAMEINITIAL1"
# title = "DRIVER_TITLE"
# medicalConditions = "DRIVER_MEDICALCONDITIONIND"
# employmentOccupationDesc = "OCCUPATION_DESCRIPTION"
# employmentBusinessDesc = "OCCUPATION_BUSINESSDESC"
# addressLine1 = "PROPOSERPOLICYHOLDER_ADDRESSLINE1"
# postCode = "PROPOSERPOLICYHOLDER_POSTCODEFULL"
# employmentStatusCode = "OCCUPATION_EMPLOYMENTTYPE"
# employmentOccupationCode = "OCCUPATION_CODE"
# employmentBusinessCode = "OCCUPATION_EMPLOYERSBUSINESS"
# employmentBusinessDesc = "OCCUPATION_DESCRIPTION"
# lengthHeld = "DRIVER_LICENCEDATE"
# number = "DRIVER_LICENCENUMBER"
# primaryEmail = "PROPOSERPOLICYHOLDER_EMAIL"
# homeOwner = "DRIVER_HOMEOWNERIND"
# ukResident = "DRIVER_NOOFYEARSUKRESIDENCY"
# titleDesc = "titleDesc"


# def change_name(xml):
#     # xml must be an ET tree object
#     attribute_order = f"{title}, {titleDesc}, {firstName}, {firstName}"
#     sql = f"select {attribute_order} from PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ_VEHICLE where QUOTE_REFERENCE ='10358790597'"
#     tag_values = run_sql(sql)
#     attri = xml.find('fullName')
#     for i in range(0, len(tag_values[0])):
#         attri[i].text = tag_values[i]
#
#
# def fill_driver(xml):
#     r = xml.find("policyholder")
#     for name_attributes in r:
#         print(name_attributes.tag)
#
#
# def check_for_layer(tree_tag):
#     if len(tree_tag) == 1:
#         return True


if __name__ == '__main__':
    # driver
    # name
    # address
    # marketing preferences
    # employment
    # licence
    tree = et.parse("../res/sample.xml")
    item = get_tree_tags(tree, "drivers")
    driver_items = get_tree_tags(tree, "policyholder")
    policy_proposer_tree = driver_items
    list_of_tags = []
    for driver_tags in driver_items:
        list_of_tags.append(driver_tags.tag)

    # values = sql_stmt_cover_row(list_of_tags) add a list on values returned
    values = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    desc = ["maritalStatusDesc", "relationshipDesc"]
    populated_dict = add_database_values_to_dict(values, driver_tag_mappings, desc)
    add_to_xml(item, populated_dict)
    one_for_all(driver_items, desc, driver_tag_mappings)

    driver_items = get_tree_tags(policy_proposer_tree, "employment")
    list_of_tags = []
    for driver_tags in driver_items:
        list_of_tags.append(driver_tags.tag)

    values = ["1", "2", "3"]
    desc = ["employmentStatusDesc", "employmentOccupationDesc", "employmentBusinessDesc"]
    populated_dict = add_database_values_to_dict(values, employment_mapping, desc)
    add_to_xml(item, populated_dict)

    driver_items = get_tree_tags(policy_proposer_tree, "address")
    list_of_tags = []
    for driver_tags in driver_items:
        list_of_tags.append(driver_tags.tag)

    # values = sql_stmt_cover_row(list_of_tags) add a list on values returned
    values = ["1", "2"]
    desc = []
    populated_dict = add_database_values_to_dict(values, address_mapping, desc)
    add_to_xml(item, populated_dict)

    driver_items = get_tree_tags(policy_proposer_tree, "licence")
    list_of_tags = []
    for driver_tags in driver_items:
        list_of_tags.append(driver_tags.tag)

    # values = sql_stmt_cover_row(list_of_tags) add a list on values returned
    values = ["1", "2"]
    desc = ["typeDesc"]
    populated_dict = add_database_values_to_dict(values, licence_mapping, desc)
    add_to_xml(item, populated_dict)

    driver_items = get_tree_tags(tree, "marketingPreference")
    list_of_tags = []
    for driver_tags in driver_items:
        list_of_tags.append(driver_tags.tag)

    # values = sql_stmt_cover_row(list_of_tags) add a list on values returned
    values = ["1"]
    desc = []
    populated_dict = add_database_values_to_dict(values, cover_tag_mappings, desc)
    add_to_xml(item, populated_dict)

    # for string in tree.iter('car'):
    #     for driver_attributes in string:
    #         print(driver_attributes.tag)
    # for string in tree.iter('policyholder'):
    #     for driver_attributes in string:
    #         if driver_attributes.tag == 'name':
    #             change_name(driver_attributes)
    #         else:
    #             print(driver_attributes.tag)
