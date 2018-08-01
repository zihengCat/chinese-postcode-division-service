# -*- coding:utf-8 -*-
import chinese_postcode_division_service as cpds
if __name__ == '__main__':
    c = cpds.PostCodeDivisionService()
    print(c.parseCode('310053'))
    print(c.parseCode('317100'))

