# 接口自动化测试框架
基于 Python + Pytest + Requests + YAML 的数据驱动接口自动化测试框架。
写这个框架是因为：我每次换项目都要重新写一套接口测试脚本，维护成本太高。所以我把请求、断言、数据提取这些重复逻辑封装成一个引擎，测试数据用 YAML 管理，这样改接口只需要改 YAML，不用动代码。

## 怎么跑的

1. YAML 里写好接口地址、请求体、期望结果
2. `engine.py` 读 YAML → 发请求 → 断言状态码和字段
3. 如果接口之间有依赖（比如先登录拿 token，再用 token 下单），用 `extract` 提取变量，后面用 `{{变量名}}` 自动替换

## 技术栈
- Python 3.10+
- Pytest
- Requests
- PyYAML

## 目录

```
api-test-framework/
├── core/                    # 核心执行引擎
│   └── engine.py            # 读取 YAML、发请求、断言、提取变量
├── data/                    # 测试数据（YAML 用例）
│   ├── get_data.yaml        # GET 请求用例
│   └── post_data.yaml       # POST 请求用例
├── tests/                   # 测试入口
│   └── test_article.py      # pytest 测试用例
├── requirements.txt         # 项目依赖
├── .gitignore               # 忽略文件配置
└── README.md                # 项目说明
```


## 跑起来

```bash
pip install -r requirements.txt
pytest tests/test_article.py -v -s
```


## 真实经历
我刚开始写接口测试时，每次新增用例都要在代码里改一堆东西，很麻烦。后来我把请求数据抽到 YAML 文件里，用 engine.py 统一执行，这样不懂代码的人也能维护测试数据。通过 extract 和 {{变量名}} 解决了 token 依赖的问题——登录接口返回 token 后，后续接口自动引用，不用每次手动填。

## GitHub Actions 已配好

每次 `git push` 会自动跑测试，跑完结果会在 Actions 里显示。

[![Actions Status](https://github.com/siyi-dev/api-test-framework/actions/workflows/python-app.yml/badge.svg)](https://github.com/siyi-dev/api-test-framework/actions)