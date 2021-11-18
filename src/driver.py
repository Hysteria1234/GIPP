import xml.etree.ElementTree as et
# import request
from util import *
import xml.dom.minidom as MD


if __name__ == '__main__':
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
    add_to_xml(driver_items, populated_dict)

    driver_items = get_tree_tags(policy_proposer_tree, "employment")
    list_of_tags = []
    for driver_tags in driver_items:
        list_of_tags.append(driver_tags.tag)

    values = ["false", "V", "001", "190"]
    desc = ["employmentStatusDesc", "employmentOccupationDesc", "employmentBusinessDesc"]
    populated_dict = add_database_values_to_dict(values, employment_mapping, desc)
    add_to_xml(driver_items, populated_dict)

    driver_items = get_tree_tags(policy_proposer_tree, "address")
    list_of_tags = []
    for driver_tags in driver_items:
        list_of_tags.append(driver_tags.tag)

    # values = sql_stmt_cover_row(list_of_tags) add a list on values returned
    values = ["1", "2"]
    desc = []
    populated_dict = add_database_values_to_dict(values, address_mapping, desc)
    add_to_xml(driver_items, populated_dict)

    driver_items = get_tree_tags(policy_proposer_tree, "licence")
    list_of_tags = []
    for driver_tags in driver_items:
        list_of_tags.append(driver_tags.tag)

    # values = sql_stmt_cover_row(list_of_tags) add a list on values returned
    values = ["F_FM", "2"]
    desc = ["typeDesc"]
    populated_dict = add_database_values_to_dict(values, licence_mapping, desc)
    add_to_xml(driver_items, populated_dict)

    driver_items = get_tree_tags(tree, "marketingPreference")
    list_of_tags = []
    for driver_tags in driver_items:
        list_of_tags.append(driver_tags.tag)

    # values = sql_stmt_cover_row(list_of_tags) add a list on values returned
    values = ["1"]
    desc = []
    populated_dict = add_database_values_to_dict(values, cover_tag_mappings, desc)
    add_to_xml(driver_items, populated_dict)

    tree.write("../hello1.xml")

    # for string in tree.iter('car'):
    #     for driver_attributes in string:
    #         print(driver_attributes.tag)
    # for string in tree.iter('policyholder'):
    #     for driver_attributes in string:
    #         if driver_attributes.tag == 'name':
    #             change_name(driver_attributes)
    #         else:
    #             print(driver_attributes.tag)
