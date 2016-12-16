
def parse_form_to_dict(payload):
    kvpstrs = payload.split('&')
    kvpsplit = map(lambda each: each.split('='), kvpstrs)
    kvps = {
        kvp[0] : kvp[1]
        for kvp in kvpsplit
    }

    return kvps
    