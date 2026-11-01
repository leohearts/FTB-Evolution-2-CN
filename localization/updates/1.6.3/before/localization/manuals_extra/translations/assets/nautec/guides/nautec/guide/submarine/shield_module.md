---
navigation:
  title: 护盾模块
  icon: nautec:shield_module
  position: 12
  parent: submarine/submarine-index.md
item_ids:
  - nautec:shield_module
---

# <Color id="light_purple">护盾模块</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="shield_module" scale="2"/>
  用能量代替艇体承受伤害.
</Column>

护盾模块消耗储存的能量吸收艇体受到的伤害, 也可以发射, 将艇体周围的一切震开.

***

## <Color id="gold">被动护盾</Color>

模块安装在任意槽位时, 艇体受到的攻击会先由电池支付: 护盾每吸收一颗心消耗 10,000 能量. 艇体的护甲会先削减攻击, 再由护盾承受, 因此能量只需覆盖穿透护甲的部分. 如果电池无法承担全部, 剩余部分由艇体承受.

满电电池最多可吸收 100 颗心, 但同一块电池还要驱动推进器并为乘员供氧. 战斗中要留意 PWR 行, 因为长时间战斗可能耗尽电池并切断你的空气.

护盾只覆盖会被护甲削减的攻击. 无视护甲的伤害, 例如魔法, 火焰或监守者的音波, 会直接作用于艇体.

***

## <Color id="gold">放电</Color>

| | 默认 |
|---|---|
| 每次放电能量 | 25,000 |
| 半径 | 艇体周围 5 格 |
| 伤害 | 10(5 颗心) |
| 眩晕 | 3 秒 |
| 冷却 | 5 秒 |

发射模块后, 一道环形冲击会从艇体爆发. 5 格内的所有活物, 除艇体自己的乘员以外, 都会受到 10 点伤害, 被从艇体旁击退, 并眩晕 3 秒. 眩晕的生物无法移动或攻击, 并会忘记自己正在追猎的目标.

放电会击中玩家, 宠物和被动生物, 也会击中敌对生物, 因此要确保艇体附近只有你想伤害的目标.

所有数值都可配置.

***

### <Color id="aqua">护盾模块配方</Color>

<Recipe id="nautec:shield_module"/>
