---
navigation:
  title: 共鸣节点
  icon: nautec:resonance_node
  position: 11
  parent: deep_engineering/deep_engineering-index.md
item_ids:
  - nautec:resonance_node
---

# <Color id="aqua">共鸣节点</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="resonance_node" scale="2"/>
  将任意激光线路或 FE 线缆接入卫星网络, 无需天线, 也无需开阔天空.
</Column>

共鸣节点会加入[共鸣网络](resonance_network.md), 与[上行链路阵列](prism_satellite.md)相同. 每台已发射卫星的上行链路都会为整个网络汇集能量. 节点可从你放置它的任何位置向该能量池输入能量, 或从中取出能量.

***

## <Color id="gold">设置</Color>

1. 将节点放置在任意方块的面上. 其水晶会背离你点击的面.
2. 空手右键点击它, 选择或创建一个网络. 输入名称并按**创建**以新建网络, 或使用箭头选择已有网络.
3. 用其界面中的按钮将其设为**输入**或**输出**.

网络需要任意维度中至少有一台已发射卫星且天空无遮挡的<ItemLink id="uplink_array"/>. 在此之前, 节点会显示**无核心**, 并且不传输任何东西.

***

## <Color id="gold">输入与输出</Color>

* **输入:** 接收射入任意侧面的激光束以及来自线缆的 FE, 并将两者发送到网络的上行链路. 它会优先发送到自身维度中的上行链路. 发送到其他维度上行链路的 AP 会损失 5% 的纯度.
* **输出:** 从网络获取 AP 和 FE. 它会将 AP 作为光束从其水晶尖端射出, 并将 FE 推入接触它的任何东西.

输出节点会与共鸣护符按优先级顺序共享网络的能量. 途中会损失 10%, 而位于没有自身上行链路的维度中的节点获得的 AP 纯度会降低 5%.

***

## <Color id="gold">缓冲, 优先级与上限</Color>

节点最多可储存 200,000 AP 和 1,000,000 FE(`resonanceNodeApBuffer` 和 `resonanceNodeFeBuffer`). 输入节点会暂存其接收的能量, 直到上行链路有空间. 输出节点会暂存从网络获取的能量, 并以其上限允许的速度向外输出.

界面顶部的控件可设置其优先级(-100 到 100)及其上限: 每 tick 传输的最大 AP, 以及单独的 FE 上限. 优先级更高的会先被填充. 点击任一数字可将其重置.

***

## <Color id="gold">升级</Color>

单独一个节点每 tick 最多传输 100,000 AP 和 100,000 FE(`satelliteTransferLimit`). 导管升级会提高该值, 其缓冲也会相应增长:

| 升级 | 每 tick 传输量 | FE 缓冲 | AP 缓冲 |
|---|---|---|---|
| 无 | 100,000 | 1,000,000 | 200,000 |
| <ItemLink id="eddy_upgrade"/> | 500,000 | 5,000,000 | 1,000,000 |
| <ItemLink id="surge_upgrade"/> | 2,500,000 | 25,000,000 | 5,000,000 |
| <ItemLink id="riptide_upgrade"/> | 10,000,000 | 100,000,000 | 20,000,000 |
| <ItemLink id="maelstrom_upgrade"/> | 无限制 | 1,000,000,000 | 1,000,000,000 |

手持升级右键点击节点即可安装; 更换时已安装的升级会返还给你. 空手潜行右键点击可将其取出. 界面会在模式按钮下方显示已安装的升级. `resonanceNodeUpgradeLimits` 设置每 tick 上限.

每台<ItemLink id="uplink_array"/>可储存 5,000,000 FE, 因此每 tick 传输超过该值的网络需要不止一台上行链路.

开启**加载**可保持节点自身区块加载, 使其在无人附近时也能工作.

<ItemLink id="configuration_card"/>会将节点的网络, 模式, 优先级, 上限, 区块加载和升级复制到另一个节点.

***

## <Color id="gold">配方</Color>

<RecipeFor id="resonance_node"/>
