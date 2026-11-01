---
navigation:
  title: 超维能量存储器
  icon: nautec:extradimensional_energy_storage
  position: 14
  parent: deep_engineering/deep_engineering-index.md
item_ids:
  - nautec:extradimensional_energy_storage
  - nautec:rift_containment_frame
  - nautec:void_containment_frame
  - nautec:abyssal_containment_frame
  - nautec:event_horizon_containment_frame
---

# <Color id="light_purple">超维能量存储器</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="extradimensional_energy_storage" scale="2"/>
  束缚在约束轭中的奇点, 在其背后的空间中储存 FE. 它会从单个方块成长为 9x9 的平台.
</Column>

它只储存 FE. 放置存储方块后, 它会立即作为 1 级存储运作. 你围绕它建造的每一圈框架都会提高其等级, 容量和 FE 传输速度, 其上方的奇点也会相应成长.

***

## <Color id="gold">等级</Color>

| 等级 | 尺寸 | 需添加的环 | 储量 | 每个端口每 tick |
|---|---|---|---|---|
| 1 | 1x1 | 无 | 10,000,000 FE | 50,000 FE |
| 2 | 3x3 | 8 个<ItemLink id="rift_containment_frame"/> | 1,000,000,000 FE | 500,000 FE |
| 3 | 5x5 | 16 个<ItemLink id="void_containment_frame"/> | 100,000,000,000 FE | 5,000,000 FE |
| 4 | 7x7 | 24 个<ItemLink id="abyssal_containment_frame"/> | 10,000,000,000,000 FE | 50,000,000 FE |
| 5 | 9x9 | 32 个<ItemLink id="event_horizon_containment_frame"/> | 1,000,000,000,000,000 FE | 2,147,483,647 FE |

每一圈都紧贴上一圈, 并与存储方块处于同一层: 裂隙框架紧贴它, 然后是围绕裂隙框架的虚空框架, 依此类推. 只有完整且由正确框架构成的环才算数. 最后一格框架放下后的一秒内, 平台会自行成型, 其每个方块都会改变外观, 表明它属于同一台机器. 破坏任意框架会使存储回落到最后一个完整的等级; 其中储存的能量不会丢失, 但当储量超过新容量时, 它不会接收任何输入.

右键点击存储方块或任意已成型的框架可打开其界面.

***

## <Color id="gold">端口</Color>

存储器的每一侧都有一个端口. 对于单独的存储方块, 方块的四个侧面就是端口. 一旦有了环, 每个端口就是平台该边缘的中央方块, FE 通过其外侧面进出.

界面顶部的四个按钮可将每个端口设为**输入**, **输出**或**关闭**. 输入端口从线缆和机器接收 FE. 输出端口会将 FE 推入其面接触的任何东西, 并允许线缆从中抽取. 端口初始为输入.

***

## <Color id="gold">共鸣网络</Color>

在其界面中选择或创建网络, 方式与[共鸣节点](resonance_node.md)相同. 存储器随后会充当网络的电池, 无需设置模式:

* 网络输入节点向上发送, 但没有输出节点需要的 FE 会进入存储器, 而不是填满上行链路.
* 当输出节点或共鸣护符的需求超过输入节点的供给时, 存储器会补足差额.

它每 tick 都会以各方向最多等于其端口速率的流量与网络交换. 通常的 10% 网络损耗作用于它送出的能量, 而不作用于它储存的能量. 网络需要任意维度中有一台已发射卫星的<ItemLink id="uplink_array"/>; 在此之前, 存储器会显示**无核心**. **加载**会保持其区块加载.

***

## <Color id="gold">移动</Color>

破坏存储方块会将其 FE 保留在物品中, 再次放置即可恢复, 因此满储量的存储器可以搬运到新基地. 框架会以自身形式掉落. 它需要钻石镐或更好的工具.

<ItemLink id="configuration_card"/>会复制其网络, 端口设置和区块加载设置.

***

## <Color id="gold">配方</Color>

<RecipeFor id="extradimensional_energy_storage"/>
<RecipeFor id="rift_containment_frame"/>
<RecipeFor id="void_containment_frame"/>
<RecipeFor id="abyssal_containment_frame"/>
<RecipeFor id="event_horizon_containment_frame"/>
