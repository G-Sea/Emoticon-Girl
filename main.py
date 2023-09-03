from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost

from mirai import Image
import re
"""
在收到GPT接口回复时，检测“:xxx:”格式的表情包表达式，将其替换为Image"
"""


# 注册插件
@register(name="Emoticon-Girl", description="表情包表达式转换", version="0.1", author="cillow")
class HelloPlugin(Plugin):
    # 插件加载时触发
    # plugin_host (pkg.plugin.host.PluginHost) 提供了与主程序交互的一些方法，详细请查看其源码
    def __init__(self, plugin_host: PluginHost):
        pass
    @on(NormalMessageResponded)
    # 当收到GPT回复时触发
    def Emoticon(self, event: EventContext, **kwargs):
        response_text: str = kwargs['response_text']

        emotions = {
            "love": [
                'https://img1.ali213.net/glpic/2022/01/25/584_20220125101547775.png'
            ],
            "sad": [
                'https://img1.ali213.net/glpic/2022/01/25/584_20220125101504258.jpg'
            ],
            "idc": [
                'https://img1.ali213.net/glpic/2022/01/25/584_2022012510150485.png'
            ],
            "die": [
                'https://img1.ali213.net/glpic/2022/01/25/584_20220125101504878.png'
            ],
            "sorry": [
                'https://img1.ali213.net/glpic/2022/01/25/584_20220125101504618.png'
            ],
            "ok": [
                'https://img1.ali213.net/glpic/2022/01/25/584_20220125101504835.png'
            ],
            "this": [
                'https://img1.ali213.net/glpic/2022/01/25/584_2022012510150417.png'
            ],
            "resist": [
                'pic/resist.jpg']
        }


        # 后续改一下正则
        ma = re.search('\:[a-z]+\:', response_text)
                
        if ma:
            emotion = ma.group()[1:-1]
            logging.info(emotion)
            print(emotion)

            emotion_dict: dict = emotions

            if emotion in emotion_dict.keys():
                e_list = emotion_dict[emotion]
                url = e_list
                logging.debug('choose emotion: {}'.format(url))
                
                host: pkg.plugin.host.PluginHost = kwargs['host']
                host.send_person_message(kwargs['launcher_id'], Image(url=url), response_text.replace(ma.group(), '')) if kwargs['launcher_type'] == 'person' else host.send_group_message(
                kwargs['launcher_id'], Image(url=url), response_text.replace(ma.group(), ''))
	


    # 插件卸载时触发
    def __del__(self):
        pass
