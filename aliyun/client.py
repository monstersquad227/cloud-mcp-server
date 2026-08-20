import os
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_bssopenapi20171214.client import Client as BssOpenApi20171214Client
from alibabacloud_bssopenapi20171214 import models as bss_models
from dotenv import load_dotenv
load_dotenv()

class AliyunClient:
    def __init__(self):
        config = open_api_models.Config(
            access_key_id=os.getenv("ALIYUN_ACCESS_KEY_ID"),
            access_key_secret=os.getenv("ALIYUN_ACCESS_KEY_SECRET"),
            region_id=os.getenv("ALIYUN_REGION_ID"),
        )
        self.client = BssOpenApi20171214Client(config)

    def get_account_balance(self):
        response = self.client.query_account_balance()
        return response.body.data.to_map()

    def get_daily_cost(self, date: str, page_size: int = 20, page_num: int = 1):
        request = bss_models.QueryAccountBillRequest(
            billing_cycle=date[:7],
            is_group_by_product=True,
            billing_date=date,
            granularity="DAILY",
            page_size=page_size,
            page_num=page_num,
        )
        resp = self.client.query_account_bill(request)
        return resp.body.data.to_map()

    def get_monthly_cost(self, date: str, page_size: int = 20, page_num: int = 1):
        request = bss_models.QueryAccountBillRequest(
            billing_cycle=date,
            is_group_by_product=True,
            granularity="MONTHLY",
            page_size=page_size,
            page_num=page_num,
        )
        resp = self.client.query_account_bill(request)
        return resp.body.data.to_map()