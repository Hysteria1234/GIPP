""" This call is created to set a tone on how to populate database """
from util import *


dict_check = {
    "abiCode": "48510205",
    "registration": "YK57VFE",
    # "make": "",
    "bodyType": "02",
    "yearOfRegistration": "2007",
    "transmission": "002",
    "engineSize": "1490",
    "model": "SWIFT GLX VVTS",
    "noOfSeats": "4",
    "fuelType": "002",
    "carValue": "1500",
    "purchaseDate": "12/03/2014",
    "importType": "N",
    "rightHandDrive": "R",
    "immobiliser": "92",
    "tracker": "N",
    "overnightPostCode": "NR27 9LB",
    "parkedDaytimeData": "NULL",
    "parkedOvernight": "4",
    "owner": "1",
    "registeredKeeper": "1",
    "coverType": "01",
    "classOfUse": "04",
    "voluntaryExcess": "500",
    "mainUser": "1",
    "totalMileage": "7000",
    "ncdGrantedYears": "2",  # ?
    "insurancePaymentType": "debit",  # ?
    "ncdProtect": "NCD_GRANTEDPROTECTEDIND",#?
    "howNcdEarn": "11",#?
    "ncdEarnedUk": "GB"#?
}


def check_for_layer(tree_tag):
    """This method is used for finding the extra indented layer in tree tags
    input - tree tag
    output - True/False depending on indent"""
    if len(tree_tag) == 1:
        return True


def sql_stmt_car_row(tags):
    """This function creates an sql statement that is then run on snowflake and give the result as a list
    input - the function takes tags that are needed from the database"""
    sql_cols = create_select_stmt(tags, column_tag_mappings)
    # building select statement VEHICLE_MODEL, VEHICLE_REGNO, ...
    final_statement = f"SELECT {sql_cols}" \
                      f"FROM PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ_VEHICLE V" \
                      f"INNER JOIN PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ R" \
                      f"ON V.QUOTE_REFERENCE= R.QUOTE_REFERENCE" \
                      f"where V.DATE_CREATED >= DATEADD(day,-5, GETDATE()) and V.TRANNAME = 'Renewal' and " \
                      f"V.PRODUCT_CODE = 'PrivateCar_Ext' "
    extracted_values = [
        ["33800601", 'EJ55XOV', '8', '2005', '2', '1598', 'COOPER', 'CONVERTIBLE', '4', '1', '2000', 'no',
         'N', 'R', 'N', 'BH15 '
            , "3", 'QH', '4', '1']]  # preferably one (string them)
    return extracted_values[0]


def sql_stmt_ncd_row(lc):
    """This function creates an sql statement that is then run on snowflake and give the result as a list
       input - the function takes tags that are needed from the database"""
    sql_cols = create_select_stmt(lc, ncd_tag_mappings)
    # building select statement VEHICLE_MODEL, VEHICLE_REGNO, ...
    final_statement = f"SELECT {sql_cols}" \
                      f"FROM PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ_VEHICLE V" \
                      f"INNER JOIN PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ R" \
                      f"ON V.QUOTE_REFERENCE= R.QUOTE_REFERENCE" \
                      f"where V.DATE_CREATED >= DATEADD(day,-5, GETDATE()) and V.TRANNAME = 'Renewal' and " \
                      f"V.PRODUCT_CODE = 'PrivateCar_Ext' "
    extracted_values = [['1', '2', '6000']]  # preferably one (string them)
    return extracted_values[0]


def main_car(tree):
    item = get_tree_tags(tree, "car")
    # Add the descriptions
    desc = ['importTypeDesc', 'immobiliserDesc', 'trackerDesc', 'parkedOvernightDesc', 'ownerDesc']
    one_for_all1(item, desc, column_tag_mappings, dict_check)

    # cover stuff
    cover = get_tree_tags(item, "cover")
    desc = ["coverLevelDesc", "classOfUseDesc", "voluntaryExcessDesc"]
    one_for_all(item, desc, cover_tag_mappings)

    ncd_greater = get_tree_tags(item, "ncdGreaterZero")
    desc = ["howNcdEarnDesc"]
    one_for_all(item, desc, ncd_tag_mappings)


def main_car1(tree):
    item = get_tree_tags(tree, "car")
    # Add the descriptions
    desc = ['importTypeDesc', 'immobiliserDesc', 'trackerDesc', 'parkedOvernightDesc', 'ownerDesc']
    one_for_all1(item, desc, dict_check)

    # cover stuff
    cover = get_tree_tags(item, "cover")
    desc = ["coverLevelDesc", "classOfUseDesc", "voluntaryExcessDesc"]
    one_for_all1(cover, desc, dict_check)

    ncd_greater = get_tree_tags(item, "ncdGreaterZero")
    desc = ["howNcdEarnDesc"]
    one_for_all1(ncd_greater, desc, dict_check)


if __name__ == '__main__':
    f = et.parse("../res/sample.xml")
    main_car(f)
    # fix 1 step
