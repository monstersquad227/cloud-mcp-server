from alibabacloud_bssopenapi20171214 import models as bss_models

from .base import AliyunBaseClient


class AliyunClient(AliyunBaseClient):
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
