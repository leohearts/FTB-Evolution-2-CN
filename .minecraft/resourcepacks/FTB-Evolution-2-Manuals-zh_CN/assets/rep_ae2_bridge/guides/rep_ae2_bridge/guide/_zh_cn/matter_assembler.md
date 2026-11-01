---
navigation:
    parent: index.md
    title: 物质装配机
    icon: rep_ae2_bridge:matter_assembler
    position: 20
categories:
- rep_bridge_components
item_ids:
- rep_ae2_bridge:matter_assembler
---

# 物质装配机

<Row gap="20">
<BlockImage id="rep_ae2_bridge:matter_assembler" scale="8"></BlockImage>
</Row>

物质装配机是你**ME网络**中的快速合成工作单元. 与桥接器配合使用时, 它可以接取 Replication 任务, 完成速度远超普通复制器.

## 工作原理

- 将其连接到与桥接器相同的ME网络
- 它会接取来自 Replication 的任务(例如来自 Replication 终端), 以及经由桥接器发出的AE2合成请求
- 由 Replication 发起的任务, 成品会送回 Replication
- 由AE2发起的任务, 成品会送入ME系统

## 升级与优先级

打开物质装配机可插入**加速卡**以提升速度. 若你有多台装配机并希望部分优先接取任务, 可使用**优先级**标签页.

## 提示

- 需要在同一ME网络中有桥接器(芯片样板和 Replication 任务均来自桥接器)
- 若目标位置没有空间, 装配机会等待, 直到可以交付
