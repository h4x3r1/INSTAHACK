# Encoded By : HAX4 ¿
# Encryption : Py3 Marshal+Zlib+B64
# Github: https://github.com/h4x3r1
#----------------------------------------------

import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))
