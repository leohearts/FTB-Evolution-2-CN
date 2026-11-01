---
navigation:
  title: 能量转换器
  icon: nautec:energy_converter
  position: 1
  parent: laser_chemistry/laser_chemistry-index.md
item_ids:
  - nautec:energy_converter
  - nautec:creative_power_source
  - nautec:creative_energy_source
  - nautec:energy_conversion_upgrade
  - nautec:advanced_energy_conversion_upgrade
  - nautec:ultimate_energy_conversion_upgrade
---

# <Color id="light_purple">能量转换器</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="energy_converter" scale="2"/>
  将其他模组的 Forge 能量(FE)转化为激光束.
</Column>

转换是单向的: 输入 FE, 输出 AP.

***

## <Color id="gold">使用</Color>

用其他模组的线缆或发电机向任意一面输入 FE. 它最多储存 4,000,000 FE(`config/nautec-common.toml` 中的 `energyConverterFeCapacity`).

每 10 FE 转化为 1 AP(`energyConverterFePerAp`). 转换器会向所有在直线上且距离不超过 16 格的激光接收方所在的面发射光束. AP 会在已连接的接收方之间平均分配, 向下取整, 因此 150 AP 分给两个接收方时各得 75 AP, 分给四个时各得 37. 只有在至少连接一个接收方时才会消耗 FE, 因此没有可供电目标的转换器会保留其缓冲区.

右键点击可设置传输速率: 每 tick 发送的 AP. 按钮每次步进 1 或 10, 按住 Shift 时步进 10 或 100, 按住 Ctrl 时步进 100 或 1,000. 界面会显示该速率每 tick 消耗的 FE, 因此请调低到与发电机供应相匹配, 这样光束就能保持稳定, 而不会在缓冲区耗尽时中断. 速率为 0 时会关闭.

***

## <Color id="gold">升级</Color>

未安装升级的转换器每 tick 最多发送 150 AP. 其界面有三个升级槽位, 每个等级一个, 每个槽位最多可放 8 个同等级升级:

| 升级 | 每个升级增加 | 8 个增加 |
|---|---|---|
| <ItemLink id="energy_conversion_upgrade"/> | 150 AP/t | 1,200 AP/t |
| <ItemLink id="advanced_energy_conversion_upgrade"/> | 500 AP/t | 4,000 AP/t |
| <ItemLink id="ultimate_energy_conversion_upgrade"/> | 1,500 AP/t | 12,000 AP/t |

三个槽位全部装满时每 tick 提供 17,350 AP, 每 tick 消耗 173,500 FE. 取出升级后速率会降低到新的上限.

<Recipe id="nautec:energy_conversion_upgrade"/>
<Recipe id="nautec:advanced_energy_conversion_upgrade"/>
<Recipe id="nautec:ultimate_energy_conversion_upgrade"/>

***

## <Color id="gold">纯度</Color>

它的光束纯度为 0. 这可以驱动[搅拌机](mixer.md), [深海排水口](drain.md), [充能器](charger.md)以及任何不需要纯度的物品转化. 聚焦透镜无法提高它, 因为透镜只会为已有纯度的光束增加纯度.

要从 FE 获得纯净能量, 可将转换器光束与纯净源头合并到同一个方块中, 例如[激光转接器](laser_manipulation.md). 合并后的光束纯度接近最纯的那一束: 3.0 的海棱水晶光束与转换器光束合并后, 输出约为 2.6, 并具有两者的功率. 关于纯净源头, 参见[光束光学](nautec:deep_engineering/beam_optics.md).

<Recipe id="nautec:energy_converter"/>

***

<Row>
  <ItemImage id="creative_power_source"/>
  ### <Color id="aqua">创造能量源</Color>
</Row>

仅创造模式可用的激光源头, 用于测试装置. 它不需要燃料, 每 tick 发送 100 AP, 纯度为 0, 并在所有直线上有接收方的面之间平均分配. 它位于 海蓝科技 创造模式标签页中.

***

<Row>
  <ItemImage id="creative_energy_source"/>
  ### <Color id="aqua">创造能量源</Color>
</Row>

用于测试能量转换器的无限 FE 供应. 它不会主动输出能量, 因此要用能从它抽取的线缆连接. 它位于 海蓝科技 创造模式标签页中.
