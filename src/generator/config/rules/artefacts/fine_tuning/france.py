# coding: utf-8


FINE_TUNING = {
    # * ... Number of digits in the complete phone suffix, operator code included
    "NDIGITS": 9,
    # * ... Maximum same digit amount in the generated pseudo-randomly block
    "SAME_DIGIT_THRESHOLD": 5,
    # * ... Maximum consecutive same digit amount anywhere in the pseudo-randomly generated block
    "CONSECUTIVE_SAME_DIGIT_THRESHOLD": 4,
    # * ... Maximum consecutive 0 amount at the beginning of the pseudo-randomly generated block
    "LAST_BLOCK_HEAD_MAX_ZEROS": 2,
    # * ... All phone numbers starting with those codes will be rejected. Set it to `{""}` to disable this feature.
    "BANNED_OPERATOR_CODES": {
        "600", "669",

        "74", "75", "76", "77", "78", "751",
        "700", "710", "711", "712", "713", "714", "715", "716", "717", "718",
        "719", "720", "721", "722", "723", "724", "725", "726", "727", "728",
        "729", "730", "731", "732", "733", "734", "735", "736", "737", "738",
        "739", "740", "741", "742", "746", "747",

        "100", "200", "300", "400", "500"
    }
}
