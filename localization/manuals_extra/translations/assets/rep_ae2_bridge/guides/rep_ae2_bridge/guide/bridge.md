---
navigation:
    parent: index.md
    title: AE2-复制桥接器
    icon: rep_ae2_bridge:rep_ae2_bridge
    position: 10
categories:
- rep_bridge_components
item_ids:
- rep_ae2_bridge:rep_ae2_bridge
---

# AE2-复制桥接器

<Row gap="20">
<BlockImage id="rep_ae2_bridge:rep_ae2_bridge" scale="8"></BlockImage>
</Row>

桥接器用于连接你的**ME网络**与**Replication物质网络**. 请将其放在两者都能接入的位置: 一侧接ME线缆, 另一侧接物质管道.

## 功能

- 在AE2终端中显示Replication物质(作为独立的物质类型)
- 允许AE2自动合成通过Replication请求物品
- 启用后可用多余的AE能量为物质网络供能(遵循AE2的FE转换比例; ME网络能量不足时停止)
- 接收来自复制器和物质装配机的成品, 并在有空间时存入ME系统

## 使用界面

右击桥接器打开其界面.

- **为物质网络供能** - 开关, 将多余的AE能量以FE形式送入物质网络(动态调整; 使用AE2的FE比例)
- **优先级** - 与其他AE2机器相同的优先级选项卡; 网络分配任务时优先选择数值更高者

若ME系统暂时已满, 成品会暂存在桥接器的缓存中, 待有空间后再移入存储.

## 自动合成物质

当AE2发起Replication合成时, 物质仍保留在你的元件/储罐/存储总线中(CPU仅持有虚拟预留). 在样板实际运行并消耗物质之前, Replication仍能看到这些库存. 取消合成不会导致物质复制.

## 提示

- 每个物质网络通常只需一个桥接器
- 确保桥接器同时在ME网络和物质管道上保持在线
- 在同一ME网络上搭配物质装配机, 可加快Replication任务
