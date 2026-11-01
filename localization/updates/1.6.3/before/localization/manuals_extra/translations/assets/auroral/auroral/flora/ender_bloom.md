---
item_ids:
  - auroral:ender_bloom
  - auroral:aurora_ender_shard
navigation:
  title: 末影花
  icon: auroral:aurora_ender_shard
  parent: index.md
  position: 33
---

# <Color id="gold">末影花</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="ender_bloom" scale="2" />

  极光花的末影近亲 - 紫色, 躁动不安, 也是末影珍珠的可再生来源.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">创造</Color>
</Column>

末影花不会自行生成.制作方法:

1. 在极光事件期间找到或种植一株 <ItemLink id="aurora_bloom" />.
2. 手持 **末影珍珠** 右击该花.
3. 花朵会转化为相同生长阶段的末影花.珍珠会被消耗.

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">持久性</Color>
</Column>

与极光花不同, 末影花 **永久存留**.它们不会在日出时枯萎, 极光结束后也会留下.

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">生长要求</Color>
</Column>

末影花只有在以下方块上种植时才会推进生长阶段:

* <ItemLink id="shimmer_soil" />
* **末地石**

在其他任何支撑方块上, 它能无限期存活, 但会停留在放置时的阶段.除非种植在上述方块之一上, 否则骨粉也无效.

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">采集</Color>
</Column>

破坏 **任意** 阶段的末影花都会掉落一个末影花物品 (重新种植时总是从第 0 阶段开始).

在第 3 阶段破坏时, 它 **还会** 掉落:

* 一个 <ItemLink id="aurora_ender_shard" />
* 额外一朵末影花的 **5% 概率**

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">极光末影碎片</Color>
</Column>

<Row>
  <ItemImage id="aurora_ender_shard" />
  ### <Color id="aqua">可再生末影珍珠</Color>
</Row>

两个极光末影碎片可以合成回一个末影珍珠.成熟的末影花农场将成为可再生的末影珍珠来源.

<RecipeFor id="ender_pearl_from_shards" />
