""" This call is created to set a tone on how to populate database """

import xml.etree.ElementTree as et
# import request
from column_mappings import column_tag_mappings
from column_mappings import cover_tag_mappings
from column_mappings import ncd_tag_mappings
from column_mappings import code_desc
from util import *
import snowflake.connector


def check_for_layer(tree_tag):
    """This method is used for finding the extra indented layer in tree tags
    input - tree tag
    output - True/False depending on indent"""
    if len(tree_tag) == 1:
        return True


# def get_tree_tags(tree_item):
#     """This method is used to get all the tags with with the parameter name eg- car would return abicode, regno
#     input - a tag whose inner tags are needed
#     output - a tag that contains all the inner tags needed"""
#     for tag in tree.iter(tree_item):
#         return tag


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


if __name__ == '__main__':
    tree = et.parse("../res/sample.xml")
    item = get_tree_tags(tree, "car")
    list_of_tags = []
    for car_tags in item:
        list_of_tags.append(car_tags.tag)

    values = sql_stmt_car_row(list_of_tags)
    # Add the descriptions
    desc = ['importTypeDesc', 'immobiliserDesc', 'trackerDesc', 'parkedOvernightDesc', 'ownerDesc']
    populated_dict = add_database_values_to_dict(values, column_tag_mappings, desc)
    add_to_xml(item, populated_dict)

    # cover stuff
    cover = get_tree_tags(tree, "cover")
    list_of_tags = []
    for cover_tags in cover:
        if cover_tags.tag != 'ncdGreaterZero':
            list_of_tags.append(cover_tags.tag)

    values = sql_stmt_cover_row(list_of_tags)
    desc = ["coverLevelDesc", "classOfUseDesc", "voluntaryExcessDesc"]
    populated_dict = add_database_values_to_dict(values, cover_tag_mappings, desc)
    add_to_xml(item, populated_dict)

    ncd_greater = get_tree_tags(tree, "ncdGreaterZero")
    list_of_tags = []
    for ncd_tags in ncd_greater:
        list_of_tags.append(ncd_tags.tag)

    values = sql_stmt_ncd_row(list_of_tags)
    desc = ["howNcdEarnDesc"]
    populated_dict = add_database_values_to_dict(values, ncd_tag_mappings, desc)
    add_to_xml(item, populated_dict)

    tree.write("../hello.xml")

    # fix 1 step
