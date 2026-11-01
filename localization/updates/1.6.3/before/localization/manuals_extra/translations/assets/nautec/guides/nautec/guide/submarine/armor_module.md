---
navigation:
  title: 护甲模块
  icon: nautec:armor_module
  position: 8
  parent: submarine/submarine-index.md
item_ids:
  - nautec:armor_module
---

# <Color id="light_purple">护甲模块</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="armor_module" scale="2"/>
  为艇体加装更厚重的装甲.
</Column>

护甲模块提高艇体的护甲韧性, 并使其不再被攻击击退.

***

## <Color id="gold">改变的内容</Color>

| | 未安装 | 已安装 |
|---|---|---|
| 护甲 | 20 | 20 |
| 护甲韧性 | 8(钻石) | 12(下界合金) |
| 击退 | 正常 | 无 |

韧性会降低强力攻击穿透护甲的程度, 因此该模块对重型攻击者最为重要. 击退被消除后, 攻击不再把你撞离航向.

它属于被动模块, 放在任意槽位都生效, 且不消耗能量. 取下后艇体会立刻恢复原始数值. 一个就够, 第二个不会提供额外效果. 它提供的韧性可配置(`submarineArmorModuleToughness`).

将它和[护盾模块](shield_module.md)搭配, 可吸收护甲未能挡下的伤害. 艇体的其他防御手段见[艇体与修复](submarine_hull.md).

***

### <Color id="aqua">护甲模块配方</Color>

<Recipe id="nautec:armor_module"/>
