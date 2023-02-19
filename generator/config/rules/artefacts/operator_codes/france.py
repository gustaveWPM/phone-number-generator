# coding: utf-8

import internal_lib.list as MyListLib

OPERATORS_CODES: dict = {
    "MOBILE": MyListLib.uniq([
        "699", "698", "695", "68", "67", "6699", "6698", "669", "668", "666", "667", "665", "663",
        "664", "660", "661", "662", "659", "658", "6567", "6568", "6449", "6448", "6447", "6440",
        "6419", "6418", "6415", "6414", "6413", "6412", "6411", "6410", "65666", "65667", "65668",
        "65669", "655", "652", "651", "650", "64999", "64995", "64998", "64992", "64993", "64990", "64991",
        "6496", "6497", "6498", "64951", "64952", "64953", "64954", "64955", "64956", "64957", "64958",
        "64959", "6490", "6491", "6492", "6493", "6494", "648", "647", "646", "645",
        "6444", "6445", "6446", "6441", "6442", "6443", "643", "642",
        "6417", "64166", "64167", "64168", "64169", "64164", "64160", "64161",
        "6401", "6402", "6403", "6404", "6405", "6406", "6407", "6408", "6409",
        "64005", "64006", "64007", "64008", "64009", "6381", "6382", "6383", "6384", "6385", "6386",
        "6387", "6388", "6389", "63801", "63802", "63803", "63804", "63805", "637", "6365", "6366",
        "6367", "6368", "6369", "6360", "6361", "6362", "6363", "6364", "635", "634", "633", "632",
        "631", "630", "62", "61",
        "789", "788", "787", "786", "785", "7840", "7841", "7842", "7843", "7844", "7845", "783",
        "782", "781", "7801", "7802", "7803", "7804", "7805", "7806", "7800", "779", "778", "777",
        "7757", "7710", "7711", "7712", "7705", "7706", "7707", "7708", "7709", "7700", "7701", "7702",
        "7703", "7704", "768", "769", "767", "7669", "7660", "7661", "7662", "7663", "7664", "7665",
        "7666", "7667", "7668", "763", "764", "762", "761", "7601", "7602", "7603", "7604", "7605",
        "7606", "7607", "7608", "7609", "76001", "76002", "76003", "76004", "76005", "76006", "76007",
        "76008", "76009", "76000", "759", "758", "75787", "75777", "75778", "75767", "75768", "75769",
        "75760", "75761", "75762", "75763", "75764", "75765", "75766", "75759", "75757", "75758",
        "75750", "75751", "75752", "75753", "75754", "75755", "75756", "75707", "75717", "75567",
        "75568", "75569", "75566", "75558", "75559", "75556", "75557", "75555", "75550", "75551",
        "75552", "75553", "75554", "75432", "753", "7521", "7522", "7523", "7524", "7525", "75202",
        "75203", "75204", "75205", "75206", "75200", "75201", "7516", "7513", "7514", "7515",
        "751", "7508", "7509", "75071", "75072", "75070", "75061", "75062", "75063", "75064", "75065",
        "75066", "75067", "75068", "75069", "75060", "75052", "75053", "75054", "75055", "75056", "75057",
        "75058", "75059", "75050", "75051", "7502", "7503", "7504", "7501", "75008", "75009", "75007",
        "75001", "75002", "75003", "75004", "75005", "75006", "75000", "749", "740", "741", "742"
    ]),

    "DESK": MyListLib.uniq(
        ["1", "2", "3", "4", "5"]
    )
}

FINE_TUNING: dict = {
    # * ... Number of digits in the complete phone suffix, operator code included
    "NDIGITS": 9,
    # * ... Maximum same digit amount in the generated block
    "SAME_DIGIT_THRESHOLD": 5,
    # * ... Maximum consecutive same digit amount anywhere in the generated block
    "CONSECUTIVE_SAME_DIGIT_THRESHOLD": 4,
    # * ... Maximum consecutive 0 amount in the beginning of the generated block
    "HEAD_MAX_ZEROS": 1
}
