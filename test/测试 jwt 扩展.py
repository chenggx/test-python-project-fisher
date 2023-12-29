import jwt
from datetime import datetime, timedelta, timezone

dic = {
    'exp': datetime.now(timezone.utc) + timedelta(seconds=3600),
    'iat': datetime.now(timezone.utc),  # 发行时间
    'iss': 'yushu',  # token签发者
    'data': {  # 内容，一般存放该用户id和开始时间
        'user_id': 1
    }
}
str = jwt.encode(payload=dic, key='ccc')  # 加密生成字符串

tk_decoder = jwt.decode(str, key='ccc', algorithms='HS256')

print(tk_decoder)
