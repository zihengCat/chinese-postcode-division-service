# -*- coding:utf-8 -*-
import os
import json
# Chinese PostCode Division Service Class
class PostCodeDivisionService(object):
    # Core Data Structure =>
    # ----------------------
    # {
    #     'post_number': [{obj_1}, {obj_2}, ... {obj_n}],
    #     ...
    # }
    def __init__(self):
        # Core Data Structure => dict()
        self._postcode_dict = self.__do_init_process()
        print("Get records: %s" % len(self._postcode_dict))
    #/*
    # - API:    parseCode()
    # - Input:  post_code (`str`)
    # - Output: info_data (`list`)
    # - Error:  `None`
    # */
    def parseCode(self, post_code_str):
        # Algorithm Complexity => O(1)
        return self._postcode_dict.get(post_code_str)
    # Hidden Initialize Process =>
    def __do_init_process(self):
        postcode_dict = dict()
        for i in range(0, 6 + 1, 1):
            # File Blocks => [x00 -> x06]
            f_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                     'db/x0%d' % i)
            #        'db/postcode.txt')
            with open(f_path, 'rt') as f:
                for line in f:
                    c_line = line[0: line.rfind(',')]
                    c_line = json.loads(c_line)
                    # get 'PostNumber' as primary key
                    postcode_key = c_line.get('PostNumber')
                    if(postcode_dict.get(postcode_key) == None):
                        # First appear
                        postcode_dict[postcode_key] = [c_line]
                    else:
                        # Already exist
                        postcode_dict[postcode_key].append(c_line)
        return postcode_dict
