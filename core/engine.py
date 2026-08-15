import requests
import yaml
import json


context={}
def load_yaml(file_path):
    with open(file_path,"r",encoding="utf8") as f:
        return yaml.safe_load(f)

def run_case(yaml_path):
    case=load_yaml(yaml_path)
    url=case["request"].get("url")
    method=case["request"].get("method","Get").lower()
    json_data=case["request"].get("json")

    if json_data:
        json_str=json.dumps(json_data)
        print(f"替换前：{json_str}")
        for var_name,var_value in context.items():
            print(str(var_value))
            json_str=json_str.replace("{{"+var_name+"}}",str(var_value))
        print(f"替换后：{json_str}")
        json_data=json.loads(json_str)

    resp=requests.request(method,url,json=json_data)
    print(f"状态码：{resp.status_code}")  # 👈 加这行
    print(f"响应体：{resp.text}")

    expect_status_code=case["response"].get("status_code")
    assert resp.status_code==expect_status_code

    expect_response=case["response"].get("json")
    if expect_response:
        result_response=resp.json()
        for key,value in expect_response.items():
            assert result_response.get(key)==value

    if "extract" in case:
        for var_name,extract_rule in case["extract"].items():
            extract_type,path=extract_rule[0],extract_rule[1]
            if extract_type=="json":
                data=resp.json()
                keys=path.split(".")[1:]
                value=data
                for key in keys:
                    value=value.get(key)
                context[var_name]=value
                print(f"提取变量：{var_name}=={value}")

#

