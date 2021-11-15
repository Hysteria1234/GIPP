""" This call is created to set a tone on how to populate database """

import xml.etree.ElementTree as et
# import request
from column_mappings import column_tag_mappings
from column_mappings import cover_tag_mappings
from column_mappings import ncd_tag_mappings
from column_mappings import code_desc
import xml.dom.minidom as MD
import snowflake.connector


def check_for_layer(tree_tag):
    """This method is used for finding the extra indented layer in tree tags
    input - tree tag
    output - True/False depending on indent"""
    if len(tree_tag) == 1:
        return True


def get_tree_tags(tree_item):
    """This method is used to get all the tags with with the parameter name eg- car would return abicode, regno
    input - a tag whose inner tags are needed
    output - a tag that contains all the inner tags needed"""
    for tag in tree.iter(tree_item):
        return tag


def deal_with_case(tag_name):
    """This method deals with descriptor tag names that donot match with their parent tag name with the code
    input - takes the tag name to check if it is one of those special case tags"""
    special_cases = {
        "coverLevelDesc": "coverType",
        "parkedOvernightDesc": "parkedOvernight",
    }
    if tag_name in special_cases:
        return special_cases[tag_name]
    else:
        return tag_name


def add_desc_map(final_map, description_list):
    """This method takes care of the description tags in the sub-tree as these can only be detected after the sql
    is run.
    input - a dict with the final mappings that needed to be added to the xml.
    the method does not return anything but adds to the map that was passed as a parameter"""
    for i in description_list:
        tag = deal_with_case(i)
        if tag.find("Desc") != -1:
            tag = tag[:-4]
        map_needed = code_desc[tag]
        if final_map[tag] in map_needed:
            final_map[i] = map_needed[final_map[tag]]


def create_select_stmt(tag_list, used_dict):
    """This method creates a select statement foe the sql statement that needs to be run
    input - Takes the list of tags that need a column name """
    ordered_columns = []
    b = ","
    for i in range(0, len(tag_list)):
        column_name = tag_list[i]
        if column_name in used_dict:
            ordered_columns.append(used_dict[column_name])

    sql_cols_names = b.join(ordered_columns)
    return sql_cols_names


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


def sql_stmt_cover_row(lc):
    """This function creates an sql statement that is then run on snowflake and give the result as a list
       input - the function takes tags that are needed from the database"""
    sql_cols = create_select_stmt(lc, cover_tag_mappings)
    # building select statement VEHICLE_MODEL, VEHICLE_REGNO, ...
    final_statement = f"SELECT {sql_cols}" \
                      f"FROM PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ_VEHICLE V" \
                      f"INNER JOIN PRD_RAW_DB.QUOTES_PUBLIC.VW_POLARIS_VEH_REQ R" \
                      f"ON V.QUOTE_REFERENCE= R.QUOTE_REFERENCE" \
                      f"where V.DATE_CREATED >= DATEADD(day,-5, GETDATE()) and V.TRANNAME = 'Renewal' and " \
                      f"V.PRODUCT_CODE = 'PrivateCar_Ext' "
    extracted_values = [['1', "", "", '2', '6000', "", ""]]  # preferably one (string them)
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


def add_to_xml(tree_sub, final_mapping):
    """This class takes in the tree subitems and adds the appropriate text to the tags
    input - takes a tree subitem and a dictionary
    result should be adding text to the tree subitem"""
    for driver_tags in tree_sub:
        if driver_tags.tag in final_mapping:
            if len(driver_tags) == 1:
                print("Layer")
            elif len(driver_tags) == 0:
                driver_tags.text = final_mapping[driver_tags.tag]
            else:
                print("handle/should never happen in car subitem")


def add_database_values_to_dict(extracted_values, dict_type, desc_list):
    """This methods add all the car values to the dict to then add to the respective tags in the xml
    input - takes the extracted values from the snowflake database"""
    final_mapping = {}
    for h in range(0, len(extracted_values)):
        final_mapping[list(dict_type.keys())[h]] = extracted_values[h]
    if len(desc_list) > 0:
        add_desc_map(final_mapping, desc_list)
    return final_mapping


if __name__ == '__main__':
    tree = et.parse("../res/sample.xml")
    item = get_tree_tags("car")
    list_of_tags = []
    for car_tags in item:
        list_of_tags.append(car_tags.tag)

    values = sql_stmt_car_row(list_of_tags)
    # Add the descriptions
    desc = ['importTypeDesc', 'immobiliserDesc', 'trackerDesc', 'parkedOvernightDesc', 'ownerDesc']
    populated_dict = add_database_values_to_dict(values, column_tag_mappings, desc)
    add_to_xml(item, populated_dict)

    # cover stuff
    cover = get_tree_tags("cover")
    list_of_tags = []
    for cover_tags in cover:
        if cover_tags.tag != 'ncdGreaterZero':
            list_of_tags.append(cover_tags.tag)

    values = sql_stmt_cover_row(list_of_tags)
    desc = ["coverLevelDesc", "classOfUseDesc", "voluntaryExcessDesc"]
    populated_dict = add_database_values_to_dict(values, cover_tag_mappings, desc)
    add_to_xml(item, populated_dict)

    ncd_greater = get_tree_tags("ncdGreaterZero")
    list_of_tags = []
    for ncd_tags in ncd_greater:
        list_of_tags.append(ncd_tags.tag)

    values = sql_stmt_ncd_row(list_of_tags)
    desc = ["howNcdEarnDesc"]
    populated_dict = add_database_values_to_dict(values, ncd_tag_mappings, desc)
    add_to_xml(item, populated_dict)

    # fix 1 step
