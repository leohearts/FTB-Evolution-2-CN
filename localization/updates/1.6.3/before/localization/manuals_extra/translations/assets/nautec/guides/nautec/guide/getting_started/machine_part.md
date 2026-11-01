---
navigation:
  title: 远古机器部件
  icon: nautec:ancient_valve
  position: 5
  parent: getting_started/getting_started-index.md
item_ids:
  - nautec:burnt_coil
  - nautec:rusty_gear
  - nautec:gear
  - nautec:ancient_valve
  - nautec:valve
  - nautec:damaged_aquatic_chip
  - nautec:aquatic_chip
---

# <Color id="light_purple">远古机器部件</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="ancient_valve" scale="2"/>
  来自海底的破损零件, 需要修复后才能用于配方.
</Column>

齿轮, 阀门, 线圈, 芯片和搅拌器从海底找到时已经损坏, 每种都有各自的修复方式. [打捞物](salvage.md)列出了它们的出现地点. 到达水晶晶洞后, 你也可以自行制作其中每一种, 因此不必等待好运: 参见本页底部的自行制作.

| 找到 | 修复为 | 方法 |
|---|---|---|
| <ItemLink id="rusty_gear"/> | <ItemLink id="gear"/> | [蚀刻](etching.md) |
| <ItemLink id="ancient_valve"/> | <ItemLink id="valve"/> | [蚀刻](etching.md) |
| <ItemLink id="burnt_coil"/> | 激光引导线圈 | [物品转化](item_transformation.md), 纯度 1.5 |
| <ItemLink id="damaged_aquatic_chip"/> | <ItemLink id="aquatic_chip"/> | 合成 |
| 破损的搅拌器 | 搅拌器 | 合成 |

***

<Row>
  <ItemImage id="gear"/>
  ### <Color id="aqua">齿轮</Color>
</Row>

将生锈的齿轮丢入蚀刻酸. 齿轮用于海蓝钢镐, 斧和锹, 搅拌机, 钓鱼站, 深海排水口以及两种强化.

***

<Row>
  <ItemImage id="valve"/>
  ### <Color id="aqua">阀门</Color>
</Row>

将远古阀门丢入蚀刻酸. 阀门用于海蓝钢胸甲和护腿, 深海排水口, 热泉汲取器, 氧气扩散器, 压力舱门, 货舱模块和聚变端口.

***

<Row>
  <ItemImage id="burnt_coil"/>
  ### <Color id="aqua">激光引导线圈</Color>
</Row>

将烧坏的线圈置于纯度 1.5 的光束中 10 秒. 如[物品转化](item_transformation.md)所述, 可用海棱水晶, 细菌燃料电池或聚焦透镜达到该纯度. 线圈用于海蓝钢工具, 充能器, 海晶电池和许多机器.

***

<Row>
  <ItemImage id="aquatic_chip"/>
  ### <Color id="aqua">海蓝芯片</Color>
</Row>

用海晶碎片合成损坏的海蓝芯片. 海蓝芯片用于培养机, 生物反应机和细菌燃料电池, 深海压力锻炉, 共鸣室, 大多数海洋侦察艇模块以及大多数合成强化. 荧光海林的幸运区域宝藏有时会直接给出一枚成品.

<Recipe id="nautec:aquatic_chip"/>

***

## <Color id="gold">搅拌器</Color>

用铸铁粒合成破损的搅拌器. [搅拌机](nautec:laser_chemistry/mixer.md)需要搅拌器. 破损的搅拌器来自溺尸, 海底废墟的箱子和幸运区域宝藏.

<Recipe id="nautec:whisk"/>

***

## <Color id="gold">自行制作</Color>

每种部件都有一条随进度解锁的稳定途径. 每一条都通向下一步:

1. **齿轮**: 将铸铁块置于纯度 2.5 或更高的光束中 8 秒, 它会变成四个齿轮. 只有<ItemLink id="prismarine_crystal"/>或<ItemLink id="bacterial_fuel_cell"/>能达到 2.5; 参见[物品转化](item_transformation.md).
2. **阀门和搅拌器**: 用铸铁, 一个齿轮或海蓝钢, 以及一个海棱水晶碎片合成.
3. 有了阀门和搅拌器, 你就可以建造[深海排水口](nautec:laser_chemistry/drain.md)和[搅拌机](nautec:laser_chemistry/mixer.md).
4. **烧坏的线圈**: 在搅拌机中, 4 个铜锭, 2 个红石, 一个海蓝钢锭和一个海棱水晶碎片, 加上 1,000 mB 盐水, 可制成一个烧坏的线圈. 按上文在纯度 1.5 的光束中修复它.
5. **海蓝芯片**: 在搅拌机中, 2 个金锭, 4 个红石, 2 个海棱水晶碎片和一个激光引导线圈, 加上 1,000 mB 盐水, 可制成两个成品海蓝芯片.

JEI 会显示搅拌机和光束配方.

<Recipe id="nautec:valve_from_cast_iron"/>

<Recipe id="nautec:whisk_from_cast_iron"/>
