---
navigation:
  parent: turbine/turbine-index.md
  title: 涡轮机能量端口
  icon: turbine_power_port
  position: 36
item_ids:
  - colossal_reactors:turbine_power_port
  - colossal_reactors:turbine_high_cond_power_port
categories:
  - ports
---

# 涡轮机能量端口

<Row gap="16" fullWidth={true}>
  <BlockImage id="turbine_power_port" scale="4" />
  <BlockImage id="turbine_high_cond_power_port" scale="4" />
</Row>

能量端口将涡轮机的 **RF** 送往**外部**的线缆和机器. **没有 GUI**: 连接外侧面, 在你的能量网络中读取功率.

## 涡轮机能量端口

普通的**涡轮机能量端口**足以满足大多数整合包和典型 RF 速率.

## 涡轮机高传导能量端口

**高传导**变体适用于每 tick 产生巨额 RF 的**超大**涡轮机. 它可储存和传输高得多的能量(可在模组设置中调整), 并且更适合支持超大功率传输的模组(例如安装后的 Draconic Evolution 或 Flux Networks).

用**涡轮机能量端口**加高级部件合成, 查看 **JEI**.

## 自动容量缩放

当涡轮机**重新验证**时, 每个**能量端口**会根据估算的涡轮机输出调整其 RF 缓冲大小:

- 目标大小约为**估算 RF/t × 10**, 且绝不低于 **10,000 RF**.
- **涡轮机能量端口**上限为 **2.1B RF**.
- **高传导**变体上限为 **9.22×10¹⁸ RF**(64 位缓冲).

输出升高时容量会立即增长; 只有在储存的能量仍能放入新目标容量时才会缩小.

## 两种变体

- 放置在**外壳面**上, 使内侧朝向涡轮机内部.

- 在**外部**连接能量线缆或机器.

输出取决于蒸汽, 线圈和叶片, 见[蒸汽, RF 与线圈](turbine_generation_and_coils.md).
