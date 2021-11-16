from src.ABI import read_csv

title = {
    "3": "Mr",
    "4": "MRS",
    "5": "Ms",
    "002": "Miss",
    "3_dr": "Dr -Male",
    "5_dr_female": "Dr- Female"
}
marital_status = {
    "D": "Divorced",
    "M": "Married",
    "C": "Common Law",
    "A": "Seperated",
    "B": "Civil Partnered",
    "S": "Single",
    "W": "Widowed"

}

type_of_licence = {
    "F_uk_manual": "Full UK - Manual",
    "F_uk_auto": "Full UK - Auto",
    "F_uk_iam": "Full UK - IAM",
    "F_uk_pass_plus": "Full UK - Pass Plus",
    "F_full_eu": "Full EU",
    "H_full_non_eu": "Full European (non EU)",
    "N_full_international": "Full International",
    "P_provisional_uk": "Provisional UK",
    "O_provisional_eu": "Provisional EU",
    "U_provisional_noneu": "Provisional European (non EU)",
    "0_provisional_inter": "Provisional International"

}

registered_keeper = {
    "1": "Proposer",
    "1_leased_private": "Leased - private",
    "2": "Spouse",
    "3": "Company",
    "4": "Leased - company",
    "6": "Parent",
    "7": "Common Law Partner",
    "8": "Son/Daughter",
    "9_society_club": "Society / Club",
    "9": "Other",
    "E": "Civil Partner",
    "H_sibling": "Brother / Sister",
    "H": "Other Family Member"
}
other_vehicle = {
    "no": "No",
    "own_another_car": "Yes - own another car",
    "named_driver_nonhd": "Yes - as named driver on another car",
    "own_motorcycle": "Yes - own/have use of a motorcycle",
    "own_van": "Yes - own/have use of a Van",
    "business_car": "Yes - on company car for business use only",
    "social_car": "Yes - on company car with social use"
}
kept_overnight = {
    "4": "Drive",
    "7": "Locked Compound",
    "1": "Locked Garage",
    "2": "Private Property",
    "F": "Public Car Park",
    "H": "Street away from home",
    "3": "Street outside home",
    "B": "Unlocked compound",
    "I": "Unlocked Garage",
    "E": "Work Car Park"
}

immobiliser = {
    "92": "Factory fitted Alarm + Immobiliser",
    "93": "Factory Fitted immobiliser",
    "N": "No security device",
    "91": "Non-Factory fitted Alarm + Immobiliser",
    "94": "Non-Factory Fitted immobiliser",
    "99": "Thatcham Approved Cat 1",
    "100": "Thatcham Approved Cat 2"
}

class_of_use = {
    "S": "Social only",
    "C": "Social inc. Comm",
    "1": "Business Use (PH)",
    "4": "Business use (PH + Spouse / Civil Partner)",
    "N": "Business use (spouse / Civil Parnter)",
    "2": "Business use by all drivers",
    "3": "Commercial travelling"
}

relationship_proposer = {
    "S": "Spouse",
    "J": "Civil Partner",
    "W": "Common law Partner",
    "M": "Parent",
    "O": "Son/Daughter",
    "A": "Brother / Sister",
    "F": "Other family member",
    "C": "Business partner",
    "E": "Employee",
    "B": "Employer",
    "U": "Other / No Relation"
}

import_type = {
    "no": "No",
    "yes_uk_import": "Yes - UK spec European import",
    "yes_euro_import": "Yes - Other European import",
    "yes_japanese_import": "Yes - Japanese import",
    "yes_us_import": "Yes - US import"
}

tracker = {

}

owner = {
    "1": "Proposer",
    "1_leased_private": "Leased - private",
    "2": "Spouse",
    "3": "Company",
    "4": "Leased - company",
    "6": "Parent",
    "7": "Common Law Partner",
    "8": "Son/Daughter",
    "9_society_club": "Society / Club",
    "9": "Other",
    "E": "Civil Partner",
    "H_sibling": "Brother / Sister"
}

cover_type = {
    "1": "Comprehensive",
    "2": "Third Party, Fire And Theft",
    "3": "Third Party Only"
}

voluntary_excess = {
    "0": "0",
    "50": "50",
    "100": "100",
    "150": "150",
    "200": "200",
    "250": "250",
    "300": "300",
    "350": "350,",
    "400": "400",
    "450": "450",
    "500": "500",
    "550": "550",
    "600": "600",
    "650": "650",
    "700": "700",
    "750": "750",
    "800": "800",
    "850": "850",
    "900": "900",
    "950": "950",
    "1000": "1000"
}

how_ncd = {
    "21": "Company Car - Business Only",
    "2": "Commercial Vehicle",
    "22": "Company Car - Including Social",
    "8": "Motor Cycle",
    "23": "Other",
    "11": "Private Car Bonus",
    "12": "Private Hire",
    "13": "Public Hire",
    "18": "Policyholders Civil Partner",
    "14": "Spouse Of Policyholder"
}

employment_status = {
    "V": "Voluntary Work",
    "E": "Employed",
    "F": "In Full Or Part Time Education",
    "H": "Household Duties",
    "S": "Self Employed",
    "R": "Retired",
    "U": "Unemployed",
    "I": "Independent Means",
    "N": "Not employed due to disability"
}
business_dict = read_csv("../res/ABI_business_codes.csv")
occupation_dict = read_csv("../res/ABI_occupation_codes.csv")
type_of_address = {}
primary_phoneno = {}
fuel_type = {}
