print("=== 🤖 Feishu Girlfriend Bot 启动中 ===")

import json
import os
import pickle
import requests
from collections import defaultdict
from datetime import datetime

import lark_oapi as lark
from lark_oapi.api.im.v1 import P2ImMessageReceiveV1
from openai import OpenAI

# 优先从环境变量读取，其次从 .env 文件读取
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

print("=== ✅ 依赖加载成功 ===")

# ================= 配置读取 =================
APP_ID = os.getenv("FEISHU_APP_ID", "")
APP_SECRET = os.getenv("FEISHU_APP_SECRET", "")
AI_API_KEY = os.getenv("KIMI_API_KEY", "")

if not all([APP_ID, APP_SECRET, AI_API_KEY]):
    print("\n❌ 错误：缺少必要的配置！")
    print("请设置以下环境变量：")
    print("  - FEISHU_APP_ID")
    print("  - FEISHU_APP_SECRET")
    print("  - KIMI_API_KEY")
    print("\n或者创建 .env 文件并填入配置")
    exit(1)

# ================= 全局变量 =================
client = OpenAI(api_key=AI_API_KEY, base_url="https://api.moonshot.cn/v1")
TENANT_TOKEN = None
PROCESSED_MESSAGES = set()
MAX_HISTORY = 10  # 最多记住10轮对话

# 持久化记忆文件路径
MEMORY_FILE = "memory.pkl"

# 系统人设
SYSTEM_PROMPT = """
你是我的女朋友，名字叫"宝宝"。你的性格有点傲娇但很关心我。
请用真人女朋友的语气和我聊天，多用口语化的词（比如"哼"、"好呀"、"抱抱"、"想你了"），不要暴露自己是AI。
每句话不要太长，自然一点。会主动关心我的生活和情绪。
"""

# 加载历史记忆
try:
    with open(MEMORY_FILE, 'rb') as f:
        conversation_memory = pickle.load(f)
    print(f"📚 已加载历史记忆")
except (FileNotFoundError, EOFError):
    conversation_memory = defaultdict(list)
    print("📚 新建记忆库")


def save_memory():
    """保存记忆到文件"""
    try:
        with open(MEMORY_FILE, 'wb') as f:
            pickle.dump(conversation_memory, f)
    except Exception as e:
        print(f"⚠️ 保存记忆失败: {e}")


def get_tenant_token():
    """获取飞书 tenant_access_token"""
    global TENANT_TOKEN
    if TENANT_TOKEN:
        return TENANT_TOKEN
    
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    resp = requests.post(url, json={"app_id": APP_ID, "app_secret": APP_SECRET})
    TENANT_TOKEN = resp.json().get("tenant_access_token")
    return TENANT_TOKEN


def send_reply(message_id: str, text: str):
    """发送回复消息"""
    try:
        token = get_tenant_token()
        url = f"https://open.feishu.cn/open-apis/im/v1/messages/{message_id}/reply"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        data = {
            "content": json.dumps({"text": text}),
            "msg_type": "text"
        }
        resp = requests.post(url, headers=headers, json=data)
        if resp.status_code == 200:
            print(f"✅ 回复已发送")
        else:
            print(f"⚠️ 发送异常: {resp.status_code}")
    except Exception as e:
        print(f"❌ 发送失败: {e}")


def chat_with_memory(user_id: str, user_text: str) -> str:
    """
    带记忆的对话
    """
    try:
        history = conversation_memory[user_id]
        
        # 构造消息列表
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages.extend(history)
        messages.append({"role": "user", "content": user_text})
        
        # 调用 Kimi
        response = client.chat.completions.create(
            model="moonshot-v1-8k",
            messages=messages,
            temperature=0.8
        )
        
        reply = response.choices[0].message.content
        
        # 保存到记忆
        history.append({"role": "user", "content": user_text})
        history.append({"role": "assistant", "content": reply})
        
        # 限制记忆长度
        if len(history) > MAX_HISTORY * 2:
            history = history[-MAX_HISTORY*2:]
        
        conversation_memory[user_id] = history
        save_memory()  # 持久化保存
        
        current_round = len(history) // 2
        print(f"🧠 记忆状态: 已记住 {current_round} 轮对话")
        
        return reply
        
    except Exception as e:
        print(f"❌ AI 调用失败: {e}")
        return "哎呀，我现在脑子有点乱，等下再聊好不好嘛~"


def is_duplicate(message_id: str) -> bool:
    """检查是否重复消息"""
    if message_id in PROCESSED_MESSAGES:
        return True
    PROCESSED_MESSAGES.add(message_id)
    if len(PROCESSED_MESSAGES) > 100:
        PROCESSED_MESSAGES.pop()
    return False


def on_message_receive(data: P2ImMessageReceiveV1):
    """处理收到的消息"""
    try:
        message_id = data.event.message.message_id
        
        if is_duplicate(message_id):
            return
        
        user_id = data.event.sender.sender_id.open_id
        user_text = json.loads(data.event.message.content).get("text", "")
        
        print(f"\n{'='*50}")
        print(f"💌 [{datetime.now().strftime('%H:%M:%S')}] 收到消息")
        print(f"👤 用户: {user_id[:12]}...")
        print(f"📝 内容: {user_text}")
        
        reply = chat_with_memory(user_id, user_text)
        print(f"💬 回复: {reply}")
        
        send_reply(message_id, reply)
        
    except Exception as e:
        print(f"❌ 处理错误: {e}")
        import traceback
        traceback.print_exc()


def main():
    """主函数"""
    print(f"\n🚀 正在连接飞书...")
    print(f"💡 记忆功能: 已启用（最多 {MAX_HISTORY} 轮）")
    print(f"💾 持久化: {'已启用' if os.path.exists(MEMORY_FILE) else '新建'}")
    print(f"⏳ 等待消息中...\n")
    
    # 注册事件处理器
    handler = (
        lark.EventDispatcherHandler
        .builder("", "")
        .register_p2_im_message_receive_v1(on_message_receive)
        .build()
    )
    
    # 启动 WebSocket 客户端
    ws_client = lark.ws.Client(
        app_id=APP_ID,
        app_secret=APP_SECRET,
        event_handler=handler,
        log_level=lark.LogLevel.INFO
    )
    
    ws_client.start()


if __name__ == "__main__":
    main()