---
navigation:
  title: 海晶单片镜
  icon: nautec:prism_monocle
  position: 9
  parent: getting_started/getting_started-index.md
item_ids:
  - nautec:prism_monocle
---

# <Color id="light_purple">海晶单片镜</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="prism_monocle" scale="2"/>
  显示你正在注视的 海蓝科技 方块的读数.
</Column>

将单片镜戴在头盔槽位或它专用的单片镜饰品槽位中. 戴上后, 注视 海蓝科技 机器或激光方块时, 屏幕中央会显示其读数. 它还会清除水下迷雾, 效果与潜水头盔相同.

<Recipe id="nautec:prism_monocle"/>

***

## <Color id="gold">读数</Color>

| 方块 | 显示内容 |
|---|---|
| 任何机器, 中继器, 光学设备或其他激光方块 | 到达的功率(AP/t)和纯度 |
| <ItemLink id="aquatic_catalyst"/> | 持续时间: 当前燃料物品已燃烧的刻数 |
| <ItemLink id="bacterial_fuel_cell"/> | 输出(AP/t), 纯度和燃料, 或无菌落 |
| <ItemLink id="pressure_forge"/> | 是否安装了合成器, 然后是压力充足, 蚀刻酸(mb)和纯度, 或仍需要的深度和水 |
| <ItemLink id="resonance_chamber"/> | 充能, 上限和纯度, 或已破裂, 冷却中 |
| <ItemLink id="gateway"/>及其环 | 其地址; 是否已开启, 就绪, 空闲, 无能量, 被红石保持关闭或受阻; 是否为野生传送门环; 以及其储存的能量 |
| <ItemLink id="submarine_dock"/> | 是否停靠着海洋侦察艇 |
| 深海排水口壁 | 功率和流体存量 |
| <ItemLink id="bubble_anchor"/> | 其状态, 力场大小, 以及剩余燃料或最终产物 |
| <ItemLink id="oxygen_diffuser"/> | 运行时的范围, 或所需的 AP |
| <ItemLink id="energy_converter"/> | 发送的 AP, 有多少光束共享它及其消耗的 FE/t, 或空闲的原因 |
| <ItemLink id="grafting_station"/>和<ItemLink id="advanced_bacterial_analyzer"/> | 状态, 能量和纯度 |
| <ItemLink id="colony_replicator"/> | 状态, 复制或剪接模式, 以及生物质 |
| <ItemLink id="uplink_array"/> | 其状态 |

在归咎于配方之前, 用它检查光束是否到达且纯度足够. 当较弱的光束与纯净光束供给同一个方块时, 纯度会略微下降.

戴在护符槽位中的<ItemLink id="resonance_charm"/>也能起到相同作用, 因此不需要同时佩戴两者. 参见[共鸣网络](nautec:deep_engineering/resonance_network.md).

***

## <Color id="gold">配合 Jade</Color>

如果安装了 Jade, 它会为部分方块添加自己的提示: 海蓝催化器的状态, 排队中的燃料, 剩余刻数, 每 tick 的 AP 及其光束到达的位置, 此外还有搅拌机, 激光转接器, 深海排水口, 约束刷怪笼, 晶体培育座, 海棱水晶, 聚变电站控制器, 潮汐转子, 热泉汲取器和能量转换器.
