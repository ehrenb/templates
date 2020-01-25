import base64
import hashlib
import json

import magic

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body with file data base64 encoded and serialized in json:
        {"data": "<b64data>"}
    Return:
        {"mime": <data mimetype>, "detailed_type": <detailed type>}
    """
    data = json.loads(req)
    fdata = base64.b64decode(data['data'])

    fpath = hashlib.md5(fdata).hexdigest()
    with open(fpath, 'wb') as f:
        f.write(fdata)

    detailed_type = magic.from_file(fpath)
    mime = magic.from_file(fpath, mime=True)

    ret = {
        'detailed_type': detailed_type,
        'mime': mime
    }

    return json.dumps(ret)
