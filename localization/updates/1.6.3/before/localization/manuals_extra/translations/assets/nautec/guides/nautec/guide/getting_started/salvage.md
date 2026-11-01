---
navigation:
  title: 打捞物
  icon: nautec:atlantic_gold_nugget
  position: 4
  parent: getting_started/getting_started-index.md
item_ids:
  - nautec:atlantic_gold_nugget
  - nautec:atlantic_gold_ingot
  - nautec:prismarine_lens
---

# <Color id="light_purple">打捞物</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="atlantic_gold_nugget" scale="2"/>
  海蓝科技 的拾取材料和机器部件的出现地点.
</Column>

许多 海蓝科技 配方需要的部件要靠寻找和修复获得, 而不是合成. 本页列出它们的来源. [远古机器部件](machine_part.md)介绍如何修复它们.

***

## <Color id="gold">结构</Color>

| 地点 | 找到的东西 |
|---|---|
| 海底废墟(海蓝科技) | 一个海蓝催化器, 一个生锈的板条箱, 可疑的沙砾 |
| 水晶晶洞 | 装满部件和材料的木桶, 板条箱和生锈的板条箱 |
| 沉船宝藏箱 | 三次中有两次是一个板条箱 |
| 原版海底废墟箱子 | 三次中有两次是一个板条箱, 四次中有一次是一些散落的打捞物: 海棱水晶碎片, 海洋金粒, 生锈的齿轮, 烧坏的线圈, 远古阀门, 损坏的海蓝芯片, 破损的搅拌器, 深海海带, 偶尔还有一个海晶透镜. 大型废墟还有机会出现海蓝钢锭, 共鸣碎片或潜水头盔 |
| 温暖海洋废墟的可疑沙子 | 偶尔有一个板条箱 |
| 埋藏的宝藏 | 略低于一半的概率出现损坏的海蓝芯片 |

原版箱子中的板条箱装有烧坏的线圈, <ItemLink id="brown_polymer"/>, 铸铁锭, 海蓝钢混合物, 海洋金粒, 海晶石, 铁和金. 海蓝科技 的结构参见[结构](structures.md), 打开方式参见[板条箱与蚀刻](etching.md).

***

## <Color id="gold">生物掉落</Color>

| 生物 | 额外掉落 |
|---|---|
| 守卫者 | 五次中有一次: 远古阀门, 烧坏的线圈或守卫者之眼 |
| 远古守卫者 | 必定掉落, 从远古阀门, 生锈的齿轮, 烧坏的线圈和邪能之心中选三样 |
| 溺尸 | 五次中有一次: 破损的搅拌器或溺尸之肺 |
| 海豚 | 五次中有一次: 海豚鳍 |

这些器官(守卫者之眼, 邪能之心, 溺尸之肺, 海豚鳍)是强化部件: 参见[生物强化](nautec:laser_augmentation/mob_augments.md). 深海生物会掉落它们自己的器官, 见[深海生命](deep_life.md).

***

## <Color id="gold">钓鱼</Color>

幸运钓鱼区域和海晶钓鱼竿会额外抽取战利品, 包括生锈的齿轮, 远古阀门, 破损的搅拌器, 海晶透镜和海洋金粒, 以及取决于生物群系的更稀有发现. 参见[钓鱼](fishing.md).

***

<Row>
  <ItemImage id="atlantic_gold_nugget"/>
  ### <Color id="aqua">海洋金</Color>
</Row>

<ItemLink id="atlantic_gold_nugget"/>会出现在任何海洋的板条箱, 生锈的板条箱和幸运区域宝藏中. 九个金粒可合成一个<ItemLink id="atlantic_gold_ingot"/>, 一个锭也可合成回九个金粒. 之后你可以稳定地生产它: 位于 Y -20 或更低的[深海压力锻炉](nautec:deep_engineering/pressure_forge.md)可在纯度 2.0 的光束中, 用 15 秒将金块压制成两个海洋金锭.

<Recipe id="nautec:atlantic_gold_ingot_from_nuggets"/>

<Recipe id="nautec:atlantic_gold_nuggets_from_ingot"/>

该锭用于海洋侦察艇, 太阳能模块和声呐模块, 辅助心室强化和共鸣护符, 之后还用于聚变电站部件, 晶体培育座, 棱镜卫星和共鸣网络方块.

***

<Row>
  <ItemImage id="prismarine_lens"/>
  ### <Color id="aqua">海晶透镜</Color>
</Row>

一种透镜, 用于细菌分析机, 移植站, 激光注入器, 海晶发射器, 脉冲激光模块, 太阳能模块和声呐模块以及若干后期机器. 你可以用海蓝钢合成它, 它也会作为幸运区域宝藏出现.

<RecipeFor id="prismarine_lens"/>
