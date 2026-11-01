---
item_ids:
  - auroral:aurora_bloom
  - auroral:aurora_bloom_decorative
  - auroral:frozen_petals
navigation:
  title: 极光花
  icon: auroral:frozen_petals
  parent: index.md
  position: 30
---

# <Color id="gold">极光花</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="aurora_bloom" scale="2" />

  在极光期间于雪地上自发出现的魔法花朵.它是 <ItemLink id="frozen_petals" /> 的来源, 也是通往模组大部分内容的入口.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">寻找极光花</Color>
</Column>

极光期间, 极光花会自然生成在寒冷生物群系的表面.它们会经历 **四个阶段** 才完全成熟.极光结束时留下的任何花朵都会在日出时枯萎.

可生成与存活的表面:

* 雪层 (前提是下方方块本身也是有效的雪面, 这样雪融化时花朵不会滞留在泥土或石头上)
* 雪块
* 细雪 (见下文)
* 冰, 浮冰与蓝冰 (冻洋表面也可)
* <ItemLink id="shimmering_ice" />

<Row>
  <ItemImage id="aurora_bloom" />
  ### <Color id="aqua">积雪封存的花朵</Color>
</Row>

当花朵被放置在 **雪层** 上或出现在 **细雪** 中时, 雪的类型会被记录.破坏或枯萎时, 花朵会在原处恢复原本的雪 - 雪层恢复为雪层, 细雪恢复为细雪.被掩埋的花朵会在上方发出微弱的雪花粒子流, 因此即使上面又堆积了更多雪, 也仍能找到它们.

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">采集</Color>
</Column>

破坏完全成熟 (第 3 阶段) 的极光花会掉落:

* <ItemLink id="frozen_petals" /> (受时运影响为 1-4 个)
* **活的极光花** 本身, 可以重新种植
* 额外获得一朵活花的 **15% 概率**

破坏未成熟的花朵不会获得任何东西 - 耐心会有回报.

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">保存的花朵 (精准采集)</Color>
</Column>

使用 **精准采集** 工具采集完全成熟的极光花, 会得到 **装饰性极光花** 而非冻结花瓣.装饰性变体:

* 不会在日出时凋谢 - 永久留存
* 始终显示第 3 阶段的外观
* 可放入 **花盆** 中展示
* 被破坏时掉落自身, 因此可以在任何地方复制

这是在极光活跃期之外保留极光花的唯一方式.

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">冻结花瓣的用途</Color>
</Column>

* **粗制的药水** - 在任何酿造台中像下界疣一样用水瓶酿造
* <ItemLink id="cold_brewing_stand" /> - 与微光钢锭结合
* <ItemLink id="glow_leek_seeds" /> - 与小麦种子结合
* <ItemLink id="frosted_cookies" /> - 带有魔法微光的甜点
* <ItemLink id="aurora_shard" /> - 在冰川之盆中以 1 级灵气灌注

<RecipeFor id="glow_leek_seeds" />

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">末影转化</Color>
</Column>

<Row>
  <ItemImage id="aurora_ender_shard" />
  ### <Color id="aqua">手持末影珍珠右击</Color>
</Row>

手持 **末影珍珠** 右击极光花, 会将其转化为相同生长阶段的 <ItemLink id="ender_bloom" />.珍珠会在此过程中被消耗.完整生命周期见 [末影花](ender_bloom.md).
