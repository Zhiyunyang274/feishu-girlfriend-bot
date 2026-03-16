# 🤖 Feishu Girlfriend Bot

> 让你的飞书机器人变成一个会聊天、有记忆、会撒娇的 AI 女友。

一个基于 **飞书机器人 + Kimi AI** 的虚拟女友聊天助手，支持长期记忆、多用户聊天和个性化人设。

---

## ✨ 功能特性

| 功能 | 描述 |
|------|------|
| 💬 自然对话 | 基于 Kimi AI（Moonshot），回复自然流畅 |
| 🧠 长期记忆 | 记住用户历史聊天，支持连续对话 |
| 👥 多用户隔离 | 每个用户独立记忆，不会串聊天记录 |
| 🔗 长连接模式 | 无需公网服务器，无需内网穿透 |
| 💾 持久化存储 | 重启后记忆仍然存在（可选） |

---

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/Zhiyunyang274/feishu-girlfriend-bot.git
cd feishu-girlfriend-bot
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

**方式一：直接设置（临时生效）**

Windows（PowerShell）：
```powershell
$env:FEISHU_APP_ID="cli_xxxxxxxxx"
$env:FEISHU_APP_SECRET="xxxxxxxxxxxxxxxx"
$env:KIMI_API_KEY="sk-xxxxxxxxxxxxxxxx"
```

Linux / macOS：
```bash
export FEISHU_APP_ID="cli_xxxxxxxxx"
export FEISHU_APP_SECRET="xxxxxxxxxxxxxxxx"
export KIMI_API_KEY="sk-xxxxxxxxxxxxxxxx"
```

**方式二：使用 `.env` 文件（推荐）**

复制示例文件：
```bash
cp .env.example .env
```

编辑 `.env` 并填写：
```env
FEISHU_APP_ID=cli_xxxxx
FEISHU_APP_SECRET=xxxx
KIMI_API_KEY=sk-xxxx
```

### 4. 启动机器人

```bash
python server.py
```

看到以下输出说明启动成功：

```
🚀 正在连接飞书...
```

---

## 📋 飞书配置指南

### 第一步：创建应用

前往 [飞书开放平台](https://open.feishu.cn/)，创建一个**企业自建应用**。

### 第二步：开启机器人能力

在应用的「应用能力」中，开启 **机器人** 能力。

### 第三步：获取凭证

在「凭证与基础信息」页面获取：
- `App ID`
- `App Secret`

### 第四步：配置权限

在「权限管理」中开启以下权限：

```
im:message:send_as_bot
im:message:receive_v1
```

### 第五步：配置事件订阅

- 连接方式：选择**长连接模式**
- 订阅事件：`im.message.receive_v1`

### 第六步：发布应用

创建版本并发布，等待审核（企业自建应用一般立即生效）。

---

## 🔑 获取 Kimi API Key

1. 前往 [Moonshot AI 平台](https://platform.moonshot.cn/)
2. 登录账号
3. 进入「API Key 管理」，创建新的 Key
4. 复制以 `sk-` 开头的密钥

---

## ⚙️ 环境变量说明

| 变量名 | 说明 | 获取方式 |
|--------|------|----------|
| `FEISHU_APP_ID` | 飞书应用 ID | 飞书开放平台 → 凭证与基础信息 |
| `FEISHU_APP_SECRET` | 飞书应用密钥 | 飞书开放平台 → 凭证与基础信息 |
| `KIMI_API_KEY` | Moonshot API Key | [platform.moonshot.cn](https://platform.moonshot.cn/) |

---

## 📝 自定义女友人设

修改 `server.py` 中的 `SYSTEM_PROMPT`：

```python
SYSTEM_PROMPT = """
你是我的女朋友，名字叫若楠。
你的性格有点傲娇但很关心我。
请用真人女朋友的语气聊天。
不要暴露自己是AI。
"""
```

你可以自由定制：
- 🎭 性格与语气
- 📖 人设与背景故事
- 💌 说话风格
- 🌟 特定记忆或共同经历

---

## 🧠 项目结构

```
feishu-girlfriend-bot/
│
├── server.py          # 主程序（机器人核心逻辑）
├── requirements.txt   # Python 依赖
├── .env.example       # 环境变量示例
└── README.md          # 项目文档
```

---

## 🔒 安全提示

> ⚠️ **请不要将 `.env` 文件上传到 GitHub！**

建议在 `.gitignore` 中添加：
```
.env
```

其他安全建议：
- 定期更换 API Key
- 使用测试应用进行开发，不要使用生产账号
- 不要在公共场所或日志中打印完整的 Key

---

## 🤝 贡献指南

欢迎任何形式的贡献！

- 🐛 [提交 Issue](https://github.com/Zhiyunyang274/feishu-girlfriend-bot/issues) 反馈问题
- 🔧 提交 Pull Request 改进功能
- 💡 分享你的人设配置和使用体验

---

## 📜 License

本项目基于 [MIT License](LICENSE) 开源。
