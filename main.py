from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost

from mirai import Image
import random

"""
在收到GPT接口回复时，检测“:xxx:”格式的表情包表达式，将其替换为Image"
"""

# 注册插件
@register(name="Emoticon-Girl", description="表情包表达式转换", version="0.1", author="cillow")
class HelloPlugin(Plugin):
    
    # 当收到GPT回复时触发
    @on(NormalMessageResponded)
    def normal_message_responded(self, event: EventContext, **kwargs):
        response_text:str = kwargs['response_text']

        emotion = {
    "love_forever":[
        'https://img1.ali213.net/glpic/2022/01/25/584_20220125101547775.png'
    ],
    "sad":[
        'https://img1.ali213.net/glpic/2022/01/25/584_20220125101504258.jpg'
    ],
    "i_don't_care":[
        'https://img1.ali213.net/glpic/2022/01/25/584_2022012510150485.png'
    ],
    "i_am_die":[
        'https://img1.ali213.net/glpic/2022/01/25/584_20220125101504878.png'
    ],
    "sorry":[
        'https://img1.ali213.net/glpic/2022/01/25/584_20220125101504618.png'
    ],
    "ok":[
        'https://img1.ali213.net/glpic/2022/01/25/584_20220125101504835.png'
    ],
    "this":[
        'https://img1.ali213.net/glpic/2022/01/25/584_2022012510150417.png'
    ],
    "resist":[
        'pic/resist.jpg']
}


        import re
        # 后续改一下正则
        ma = re.search('\:[a-z]+\:', response_text)
        if ma:
            emotion = ma.group()[1:-1]
            logging.info(emotion)

            emotion_dict: dict = emotion
            if emotion in emotion_dict.keys():
                e_list = emotion_dict[emotion]
                url = e_list[random.randint(0, len(e_list)-1)]
                logging.debug('choose emotion: {}'.format(url))
                img = [response_text.replace(ma.group(), '')]
                if url.startswith('http'):
                    img = [Image(url=url), response_text.replace(ma.group(), '')]
                else:
                    pass
                    # 未成功
                    # import os
                    # img = [Image(path=os.path.join('plugins/emotion', url)), response_text.replace(ma.group(), '')]

                event.add_return("reply", img)
                event.prevent_default()

    # 插件卸载时触发
    def __del__(self):
        pass
