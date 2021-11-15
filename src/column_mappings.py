from mappings import *

column_tag_mappings = {
    "abiCode": "VEHICLE_MODEL",
    "registration": "VEHICLE_REGNO",
    # "make": "",
    "bodyType": "VEHICLE_BODYTYPE",
    "yearOfRegistration": "VEHICLE_FIRSTREGDYEAR",
    "transmission": "VEHICLE_TRANSMISSIONTYPE",
    "engineSize": "VEHICLE_CUBICCAPACITY",
    "model": "VEHICLE_MODELNAME",
    # "noOfDoors": "",
    "noOfSeats": "VEHICLE_NOOFSEATS",
    "fuelType": "VEHICLE_TYPEOFFUEL",
    "carValue": "VEHICLE_VALUE",
    "purchaseDate": "VEHICLE_PURCHASEDATE",
    "importType": "VEHICLE_PERSONALIMPORTIND",
    # "importTypeDesc": "",
    "rightHandDrive": "VEHICLE_LEFTORRIGHTHANDDRIVE",
    "immobiliser": "SECURITY_MAKEMODEL",
    # "immobiliserDesc": "",
    "tracker": "VEHICLE_TRACKERDEVICEFITTEDIND",
    # "trackerDesc": "",
    "overnightPostCode": "VEHICLE_POSTCODEFULL",
    "parkedDaytimeData": "VEHICLE_VEHICLEKEPTDAYTIME",
    "parkedOvernight": "VEHICLE_LOCATIONKEPTOVERNIGHT",
    # "parkedOvernightDesc": "",
    "owner": "VEHICLE_OWNERSHIP",
    # "ownerDesc": "",
    "registeredKeeper": "VEHICLE_KEEPER",
    # "registeredKeeperDesc": "",
    # "cover": ""
}

cover_tag_mappings = {
    "coverType": "COVER_CODE",
    "classOfUse": "Uses_AbiCode",
    "voluntaryExcess": "Cover_VolXsAmt",
    "mainUser": "COVER_VEHPRN",
    "totalMileage": "VEHICLE_ANNUALMILEAGE",
    "ncdGrantedYears":	"Ncd_ClaimedYears",#?
    "insurancePaymentType": ""#?
}
ncd_tag_mappings = {
    "ncdProtect": "NCD_GRANTEDPROTECTEDIND",#?
    "howNcdEarn": "Ncd_ClaimedEntitlementReason",#?
    "ncdEarnedUk": "Ncd_ClaimedCountryEarned",#?
}
code_desc = {
        "title": title,
        "maritalStatus": marital_status,
        "type": type_of_licence,
        "registeredKeeper": registered_keeper,
        "useOtherVehicle": other_vehicle,
        "parkedOvernight": kept_overnight,
        "immobiliser": immobiliser,
        "classOfUse": class_of_use,
        "relationship": relationship_proposer,
        "parkedDaytimeData": kept_overnight,
        "importType": import_type,
        "tracker": tracker,
        "owner": owner,
        "coverType": cover_type,
        "voluntaryExcess": voluntary_excess,
        "howNcdEarn": how_ncd
}
