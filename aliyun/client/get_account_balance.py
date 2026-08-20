from .base import AliyunBaseClient


class AliyunClient(AliyunBaseClient):
    def get_account_balance(self):
        response = self.client.query_account_balance()
        return response.body.data.to_map()
