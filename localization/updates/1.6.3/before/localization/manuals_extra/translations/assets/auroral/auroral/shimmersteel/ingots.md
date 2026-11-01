---
item_ids:
  - auroral:shimmersteel_ingot
  - auroral:unrefined_shimmersteel
navigation:
  title: 微光钢锭
  icon: auroral:shimmersteel_ingot
  parent: index.md
  position: 40
---

# <Color id="gold">微光钢锭</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="shimmersteel_ingot" scale="2" />

  极光 核心的魔法金属. 经极光灌注, 略强于铁, 也是模组中所有升级工具, 武器和配饰的入口.
</Column>

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">第1步 - 未精炼微光钢</Color>
</Column>

<Row>
  <ItemImage id="unrefined_shimmersteel" />
  ### <Color id="aqua">铁 + 极光碎片</Color>
</Row>

用铁锭和 <ItemLink id="aurora_shard" /> 合成未精炼微光钢.

<RecipeFor id="unrefined_shimmersteel" />

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">第2步 - 冰川之盆灌注</Color>
</Column>

<Row>
  <ItemImage id="glacial_basin" />
  ### <Color id="aqua">灌注</Color>
</Row>

在充满液态灵气的 <ItemLink id="glacial_basin" /> 中灌注未精炼微光钢.

1. 在寒冷生物群系中, 将冰川之盆放置在露天之下.
2. 等待极光将盆完全充满(3/3灵气).
3. 手持未精炼微光钢右键点击盆.
4. 盆会消耗**全部**液态灵气, 产出一个微光钢锭.

**重要:** 盆必须完全装满才能进行此灌注.

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">属性</Color>
</Column>

* **高附魔能力** - 容易接受附魔
* **极光亲和** - 微光钢工具和护甲在极光期间自我修复
* **属性** - 略强于铁, 低于钻石

<ItemImage id="minecraft:air" scale="0.25"/>
***

<Column alignItems="center" fullWidth={true}>
  ## <Color id="gold">用途</Color>
</Column>

微光钢锭可通过锻造台升级铁制装备. 你需要一个**微光钢升级锻造模板**才能进行升级.

* <ItemImage id="shimmersteel_pickaxe" scale="0.75"/> [微光钢工具](tools.md) - 镐, 斧, 锹, 锄, 剑
* <ItemImage id="shimmersteel_bow" scale="0.75"/> [微光钢弓](bow.md) - 用雪球发射星弹
* <ItemImage id="shimmer_spear" scale="0.75"/> [微光矛](spear.md) - 长攻击距离的穿刺矛
