import requests
import hashlib
import random

YOUDAO_URL = 'https://openapi.youdao.com/api'
APP_KEY = '789def3aa7334755'
APP_SECRET = 'SbuSmhF9BQaYE3sAtIr4Q2u018mytYgS'

def create_sign(q, app_key, app_secret, salt):
    """生成签名"""
    sign = app_key + q + salt + app_secret
    return hashlib.md5(sign.encode('utf-8')).hexdigest()
def translate(q, from_lang='auto', to_lang='zh-CHS'):
    """
    调用有道 API 进行翻译
    :param q: 待翻译文本
    :param from_lang: 源语言
    :param to_lang: 目标语言
    :return: 翻译结果字符串
    """
    if not q.strip():
        return "错误：输入文本不能为空。"

    salt = str(random.randint(32768, 65536))
    sign = create_sign(q, APP_KEY, APP_SECRET, salt)

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'q': q,
        'from': from_lang,
        'to': to_lang,
        'appKey': APP_KEY,
        'salt': salt,
        'sign': sign,
    }

    try:
        response = requests.post(YOUDAO_URL, headers=headers, data=data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            if 'translation' in result:
                return result['translation'][0]
            else:
                return f"翻译失败：{result.get('errorCode', 'Unknown error')}"
        else:
            return f"HTTP 请求失败，状态码：{response.status_code}"
    except Exception as e:
        return f"请求出错：{str(e)}"
# 示例用法
if __name__ == "__main__":
    # 可以手动修改这里测试
    text_to_translate = input("请输入要翻译的文本: ")
    translation = translate(text_to_translate)
    print(f"翻译结果: {translation}")