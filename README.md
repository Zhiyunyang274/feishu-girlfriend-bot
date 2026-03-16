# 🤖 Feishu Girlfriend Bot

基于飞书机器人 + Kimi AI 的虚拟女友聊天助手，支持长期记忆功能。

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ 功能特性

- 💬 **自然对话**：基于 Kimi AI，回复生动自然
- 🧠 **长期记忆**：能记住之前的聊天内容，像真人一样聊天
- 🔗 **长连接支持**：无需内网穿透，本地运行即可接收消息
- 👥 **多用户隔离**：每个用户有独立的记忆库
- 💾 **持久化存储**（可选）：重启后记忆不丢失

## 🚀 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/你的用户名/feishu-girlfriend-bot.git
cd feishu-girlfriend-bot
2. 安装依赖
bashCopyCopied!
pip install -r requirements.txt
3. 配置环境变量
Windows (PowerShell):

powershellCopyCopied!
$env:FEISHU_APP_ID="cli_xxxxxxxxxxxxx"
$env:FEISHU_APP_SECRET="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
$env:KIMI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
Linux/macOS:

bashCopyCopied!
export FEISHU_APP_ID="cli_xxxxxxxxxxxxx"
export FEISHU_APP_SECRET="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
export export KIMI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
或者使用 .env 文件：

复制 .env.example 为 .env
填入真实的 ID 和 Key
4. 运行程序
bashCopyCopied!
python server.py
看到 🚀 正在连接飞书... 就说明启动成功了！

📋 飞书配置指南
前往 飞书开放平台 创建企业自建应用
开启"机器人"能力
获取 App ID 和 App Secret（凭证与基础信息页面）
开通权限：
im:message:send_as_bot
im:message:receive_v1
配置事件订阅：
方式：长连接
事件：im.message.receive_v1
创建版本并发布
🔑 获取 Kimi API Key
前往 Moonshot AI 控制台
创建 API Key
复制以 sk- 开头的密钥
⚙️ 配置说明
环境变量	说明	获取方式
FEISHU_APP_ID	飞书应用 ID	飞书开放平台 → 凭证与基础信息
FEISHU_APP_SECRET	飞书应用密钥	飞书开放平台 → 凭证与基础信息
KIMI_API_KEY	Kimi AI API Key	Moonshot AI 控制台
🔒 安全提示
切勿将 .env 文件提交到 GitHub！ 已加入 .gitignore
定期轮换 API Key 和 App Secret
建议使用专门的应用，不要用生产环境的主应用
📝 自定义女友人设
修改 server.py 中的 SYSTEM_PROMPT 变量：

pythonCopyCopied!
SYSTEM_PROMPT = """
你是我的女朋友，名字叫"宝宝"。你的性格有点傲娇但很关心我。
请用真人女朋友的语气和我聊天，不要暴露自己是AI。
"""
🤝 贡献
欢迎提交 Issue 和 PR！