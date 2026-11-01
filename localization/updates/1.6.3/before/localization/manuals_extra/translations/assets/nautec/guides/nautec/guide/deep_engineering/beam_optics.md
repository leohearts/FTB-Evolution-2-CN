---
navigation:
  title: 光束光学
  icon: nautec:focusing_lens
  position: 0
  parent: deep_engineering/deep_engineering-index.md
item_ids:
  - nautec:focusing_lens
---

# <Color id="light_purple">光束光学</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="focusing_lens" scale="2"/>
  纯度, 以及提高纯度的透镜.
</Column>

<ItemLink id="prismarine_laser_relay"/>沿直线传递光束, <ItemLink id="laser_junction"/>则让光束转向, 合并和分流, 两者都不会改变纯度(见[传输激光能量](nautec:laser_chemistry/laser_manipulation.md)). 配方在运行前会检查纯度, 因此请根据末端机器所需的纯度来规划光源.

***

## <Color id="gold">纯度</Color>

纯度由光源决定. 合并光束会略微降低纯度, 聚焦透镜则会提高纯度.

| 光源 | 纯度 |
|---|---|
| <ItemLink id="aquatic_catalyst"/>燃烧海晶碎片 | 0.4 |
| 海蓝催化器燃烧海晶水晶 | 0.8 |
| 海蓝催化器燃烧海棱水晶碎片 | 1.2 |
| <ItemLink id="bacterial_fuel_cell"/> | 最高 2.5 |
| 从侧面击中的<ItemLink id="prismarine_crystal"/> | 3.0 |

每个接触海蓝催化器的海晶母岩方块为其光束增加 0.1 纯度, 最高 2.0. 见[激光能量](nautec:getting_started/laser_power.md).

本节的机器需要以下纯度:

| 产出 | 机器 | 纯度 |
|---|---|---|
| 无瑕海棱水晶 | [深海压力锻炉](pressure_forge.md) | 2.0 |
| 海洋金锭 | 深海压力锻炉 | 2.0 |
| 深海钢镀板 | 深海压力锻炉 | 2.5 |
| 共鸣碎片 | [共鸣室](resonance_chamber.md) | 3.0 |
| 海晶晶种 | 共鸣室 | 3.0 |

当两束或更多光束供给同一方块时, 它们的功率相加, 纯度则接近最纯的光束. 结果是最高纯度减去它与所有光束平均值之间差距的四分之一(`beamMergePurityDrop`), 因此 3.0 光束与 0 光束合并后约为 2.6.

***

<Row>
  <ItemImage id="focusing_lens"/>
  ### <Color id="aqua">聚焦透镜</Color>
</Row>

使直穿而过的光束纯度提高 0.5(`lensPurityBonus`), 上限为 2.0. 放置时请朝向光束传播的方向: 朝向你的面接收光束, 远端的面将其继续发出, 最远 16 格(`laserDistance`). 功率原样通过, 且可放置在水下.

透镜只会为已经带有纯度的光束增加纯度, 因此请把它放在可工作的光源之后. 1.8 的光束会变为 2.0, 而已经达到 2.0 或更高的光束会原样通过, 所以一排透镜的上限是 2.0. 串联两个透镜可将海棱水晶碎片催化器(1.2)提升到压力锻炉制造无瑕海棱水晶所需的 2.0. 若要 2.5 和 3.0, 请使用细菌燃料电池或海棱水晶作为光源.

<Recipe id="nautec:focusing_lens"/>
