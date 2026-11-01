---
navigation:
  title: 海洋发电机
  icon: nautec:tidal_rotor
  position: 16
  parent: getting_started/getting_started-index.md
item_ids:
  - nautec:tidal_rotor
  - nautec:thermal_vent_tap
---

# <Color id="light_purple">海洋发电机</Color>

<Column alignItems="center" fullWidth={true}>
  <Row>
    <ItemImage id="tidal_rotor" scale="2"/>
    <ItemImage id="thermal_vent_tap" scale="2"/>
  </Row>
  将海洋转化为 Forge 能量(FE), 供其他模组的机器使用的发电机.
</Column>

海蓝科技 有四种 FE 发电机. 潮汐转子依靠海洋本身运行, 热泉汲取器利用海床的热量煮沸盐水, [内燃发电机](nautec:getting_started/combustion_dynamo.md)燃烧由细菌培育的原油, [聚变电站](nautec:deep_engineering/fusion_plant.md)则是后期反应堆. 每台发电机都会将其 FE 推入接触它的任何线缆或机器.

***

<Row>
  <ItemImage id="tidal_rotor"/>
  ### <Color id="aqua">潮汐转子</Color>
</Row>

早期游戏的铸铁涡轮机, 无需燃料, 提供 40 到 80 FE/t.

将其放置在海洋生物群系的水下. 在能起作用的最狭窄位置, 它产出 40 FE/t, 水域越开阔, 越深, 产出越多, 在每一侧都有水且上方有 24 格水时达到 80 FE/t. 埋入海床或紧贴其他转子的转子产出更少, 因此请将它们分散布置在海床上, 而不是堆叠在一起.

***

<Row>
  <ItemImage id="thermal_vent_tap"/>
  ### <Color id="aqua">热泉汲取器</Color>
</Row>

中期发电机, 在岩浆块或熔岩上方煮沸盐水, 提供 350 到 1,250 FE/t.

* **热量.** 汲取器会检查其正下方的九个方块是否有岩浆块或熔岩. 一个热方块提供 350 FE/t, 九个全有则提供 1,250 FE/t. 来自热泉区的<ItemLink id="hydrothermal_vent"/>本身算作三个热方块. 在海底热泉生物群系中, 只要至少有一个热方块, 海床会再增加三个.
* **燃料.** 将盐水用管道输入任意一面. 运行时汲取器每 tick 煮沸 10 mB, 因此一个[深海排水口](nautec:laser_chemistry/drain.md)可供两台汲取器运行, 还略有富余.
* **盐.** 每煮沸 1,000 mB 会留下一个<ItemLink id="salt"/>. 汲取器会将其推入接触它的任何箱子或其他容器, 你也可以用管道或漏斗从任意一面抽出. 槽位满了只会阻止盐的输出, 不会影响发电.

Jade 会显示每台发电机的输出及其缺少的东西.

<RecipeFor id="tidal_rotor"/>

<RecipeFor id="thermal_vent_tap"/>
