# -*- coding:utf-8 -*-
import chinese_postcode_division_service as cpds
if __name__ == '__main__':
    c = cpds.PostCodeDivisionService()
    # 正确用例 =>
    print(len(c.parseCode('310053')))
    print(c.parseCode('317100')[0])
    # 错误用例 =>
    print(c.parseCode('hello'))
