import os
from core.engine import run_case

def test_get_article():
    yaml_path=os.path.join(os.path.dirname(__file__),"..","data","get_data.yaml")
    run_case(yaml_path)

def test_post_article():
    yaml_path = os.path.join(os.path.dirname(__file__), "..", "data", "post_data.yaml")
    run_case(yaml_path)