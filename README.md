# DIAN Racing Test Ride Log

同济大学 DIAN Racing 电车队 — 赛车测试日志 Web 应用

**在线地址**: [https://testridelog.pages.dev](https://testridelog.pages.dev)

---

## 项目结构

```
TestRide/
├── Test Ride Log.html    # 主应用（单页 HTML，所有功能在此）
├── index.html            # 重定向 → Test Ride Log.html
├── generate-qr.py        # 生成 QR 码脚本
├── start-tunnel.py       # 本地隧道脚本（备用，一般不需要）
├── qr-code.png           # 永久 QR 码
└── README.md
```

## 部署架构

```
GitHub (源码仓库)
   ↓ git push
   ↓ 自动同步
Cloudflare Pages (托管 + CDN)
   ↓
https://testridelog.pages.dev ← QR 码指向此地址
```

- **GitHub**: [github.com/Vahallaaaaa/TestRideLog](https://github.com/Vahallaaaaa/TestRideLog)
- **Gitee 镜像**: [gitee.com/vahalla/test-ride-log](https://gitee.com/vahalla/test-ride-log)
- **Cloudflare Pages**: 国内可直连，无需 VPN

---

## 更新网页

修改 `Test Ride Log.html` 后：

```bash
cd d:/ai/TestRide

git add "Test Ride Log.html"
git commit -m "描述你的改动"
git push origin master
```

推送后 Cloudflare Pages **自动部署**，1 分钟内生效。QR 码永远不变。

如需同步到 Gitee：

```bash
git push gitee master
```

---

## 重新生成 QR 码

只有 URL 变了才需要重新生成（一般不需要）：

```bash
# 1. 编辑 generate-qr.py，修改 URL 变量
# 2. 运行
python generate-qr.py

# 3. 推送
git add generate-qr.py qr-code.png
git commit -m "Update QR code"
git push origin master
```

---

## 本地测试

无需任何工具，直接浏览器打开 `Test Ride Log.html` 即可。

如需局域网内其他设备访问：

```bash
python -m http.server 8000
# 然后访问 http://你的电脑IP:8000
```

---

## 技术栈

纯前端，无框架，无后端，无构建步骤。

- HTML5 / CSS3 / Vanilla JS
- Canvas 2D（轮胎胎压/温度可视化）
- localStorage（数据持久化）
- 响应式设计（桌面 + 平板 + 手机）

---

## URL 变更记录

| 日期 | 平台 | URL |
|------|------|-----|
| 2026-08-04 | Cloudflare Pages | `https://testridelog.pages.dev` |
| 2026-08-04 | GitHub Pages | `https://vahallaaaaa.github.io/TestRideLog/` |
