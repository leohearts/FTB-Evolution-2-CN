---
item_ids:
  - colossal_reactors:radiation_scrubber
  - colossal_reactors:radiation_cure
categories:
  - processing
---

# 辐射管理

当配置中启用**辐射管理**且你的实例包含集成内容(通常是 **Mekanism**)时出现. 使用 **JEI** 确认你的存档中存在对应配方与方块.

## 辐射净化器

<BlockImage id="radiation_scrubber" scale="4" />

**辐射净化器**消耗能量与可选的**催化剂**物品, 将空气中的辐射相关物质处理为储罐中显示的**化学品/气体缓冲**.

### 控件

- 两个**物品槽**, 用于配置催化剂(有效催化剂见 JEI 与你的数据包).

- **气体/化学品储罐**: 悬停可查看内容物与填充量.

- 侧面的**能量条**: 悬停可查看已储存能量.

当存在 **Mekanism** 时, 自动化设备可通过该方块暴露的 Mek 化学品 API 与其交互; 否则可在支持的情况下通过界面与连接的管道手动交互.

## 辐射治疗剂

<ItemImage id="radiation_cure" scale="2" />

**辐射治疗剂**是用于该辐射流程的消耗品. 配置后可通过物品提示中的 GuideME **打开指南**快捷键打开.
