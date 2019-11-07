import hashlib


def get_md5(s: str):
    """获取md5加密值

    :param s: 需要加密的字符串
    :return: 加密后的字符串
    """
    if s:
        # 创建md5对象
        m = hashlib.md5()
        if s is str:
            m.update(s.encode("utf8"))
        else:
            m.update(str(s).encode("utf8"))

        return m.hexdigest()  # 返回加密后的值
    raise TypeError("转入参数不能为空")
