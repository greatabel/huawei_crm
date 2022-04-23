import json

class SourceDataDemo:

    def __init__(self):
        self.title = '商品购买大数据可视化展板'
        self.counter = {'name': 'action_type table', 'value': 54925330}
        self.counter2 = {'name': 'activity_log table', 'value': 7027943}
        self.echart1_data = {
            'title': '男女性别分布',
            'data': [
                {"name": "男", "value": 1643382},
                {"name": "女", "value": 258644},
                {"name": "未知", "value": 5062667},


            ]
        }
        self.echart2_data = {
            'title': '单人重复购买最多次数排名',
            'data': [
                {"name": "u265990", "value": 25},
                {"name": "u246371", "value": 13},
                {"name": "u216131", "value": 12},
                {"name": "u262623", "value": 11},
                {"name": "u50682", "value": 11},
       
            ]
        }
        self.echarts3_1_data = {
            'title': '年龄分布',
            'data': [
                {"name": "<18", "value": 1345565},
                {"name": "[18,24]", "value": 260},
                {"name": " [25,29]", "value": 733323},
                {"name": " [30,34]", "value": 1916611},
                {"name": "[35,39]", "value": 1460542},
            ]
        }
        self.echarts3_2_data = {
            'title': 'label复购',
            'data': [
                {"name": "重复买家", "value": 261477},
                {"name": "非重复买家", "value":  6766466},
        
            ]
        }
        self.echarts3_3_data = {
            'title': '性别是否可区分分布',
            'data': [
                {"name": "可区分", "value": 643382+258644},
                {"name": "不可区分", "value": 63250},
         
            ]
        }
        self.echart4_data = {
            'title': '平均log时间趋势',
            'data': [
                {"name": "男", "value": [3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 4]},
                {"name": "女", "value": [5, 3, 5, 6, 1, 5, 3, 5, 6, 4, 6, 4, 8, 3, 5, 6, 1, 5, 3, 7, 2, 5, 8]},
            ],
            'xAxis': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '11', '12', '13', '14', '15', '16', '17',
                      '18', '19', '20', '21', '22', '23', '24'],
        }
        self.echart5_data = {
            'title': '品牌购买数量统计分布',
            'data': [

                {"name": "no1", "value": 763345},
                {"name": "no2", "value": 737545},
                {"name": "no3", "value": 729555},
                {"name": "no4", "value": 541075},
                {"name": "no5", "value": 528003},
            ]
        }
        self.echart6_data = {
            'title': '行为分布：0点击，1加入购物车，2购买，3收藏',
            'data': [
                {"name": "点击", "value": 48550713, "value2": 36, "color": "01", "radius": ['59%', '70%']},
                {"name": "购物车", "value": 3292144, "value2": 214, "color": "02", "radius": ['49%', '60%']},
                {"name": "购买", "value": 3005723, "value2": 20, "color": "03", "radius": ['39%', '50%']},
                {"name": "收藏", "value": 76750, "value2": 18, "color": "04", "radius": ['29%', '40%']},
               
            ]
        }
        self.map_1_data = {
            'symbolSize': 100,
            'data': [
                {'name': '武汉', 'value': 239},
                {'name': '北京', 'value': 121},
                {'name': '其他', 'value': 203},
            ]
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        echart = {
            'symbolSize': data.get('symbolSize'),
            'data': data.get('data'),
        }
        return echart


class SourceData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        self.title = '商品购买大数据可视化展板'

