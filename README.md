# Chinese PostCode Division Service

[![Build Status](https://travis-ci.com/zihengCat/chinese-postcode-division-service.svg?branch=master)](https://travis-ci.com/zihengCat/chinese-postcode-division-service)

中华人民共和国邮政编码数据服务模块「Python Module」。

An Chinese PostCode Division Service Module for `Python`.

# Usage（使用说明）

此模块**同时兼容`Python2`与`Python3`，且无「第三方」依赖项**。

1. 解压缩`db/postcode.zip`
2. 导入模块
3. 初始化类实例
4. 调用解析方法

| API                        | 说明           |
| -------------------------- | -------------- |
| `parseCode(post_code_str)` | 接受参数：邮政编码（6位字符串），正确返回：省市区街结构，错误返回：`None` |

> 表：模块`API`接口表

```python
# 1. 导入模块「可以使用`as`简化书写」
import chinese_postcode_division_service as cpds

# 2. 创建类实例
c = cpds.PostCodeDivisionService()

# 3. 调用解析方法
i = c.parseCode('310053')
print(i)
```
> 代码清单：示例代码「详见`main.py`」

# Data Source（数据来源）

详情参看：`db/postcode.zip`

# License（许可协议）

[MIT](./LICENSE)

