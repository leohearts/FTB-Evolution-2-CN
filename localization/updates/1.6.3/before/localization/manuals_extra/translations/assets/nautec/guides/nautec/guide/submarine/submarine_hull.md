---
navigation:
  title: 艇体与修复
  icon: nautec:submarine
  position: 3
  parent: submarine/submarine-index.md
---

# <Color id="light_purple">艇体与修复</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="submarine" scale="2"/>
  损伤, 破损与修复.
</Column>

艇体拥有自己的生命值和护甲, 你在艇上时, 被攻击的是艇体而不是你.

***

## <Color id="gold">艇体强度</Color>

| | 默认 |
|---|---|
| 艇体值 | 80(40 颗心) |
| 护甲 | 20, 与全套钻石护甲相同 |
| 护甲韧性 | 8, 与全套钻石护甲相同 |

这三项都可配置. [护甲模块](armor_module.md)提高韧性并消除击退, [护盾模块](shield_module.md)则消耗能量吸收攻击.

登艇时, 32 格内正在追猎你的生物会将目标转为艇体; 乘艇期间, 任何试图以你为目标的攻击都会改为瞄准艇体. [隐形模块](stealth_module.md)是甩掉它们的方法.

艇体不会因溺水, 冰冻, 在方块内窒息, 拥挤或坠落而受伤, 艇上的人也无法伤害它. 药水与治疗效果对它无效.

***

## <Color id="gold">自我修复</Color>

无论是否有人在艇上, 艇体每 10 秒恢复 1% 的艇体值, 因此轻微受损的艇体放置一段时间后会自行恢复满值. 间隔和恢复量可配置, 整合包也可以关闭自我修复.

读数的 HULL 行会显示当前状态(见[驾驶](submarine_controls.md)).

***

## <Color id="gold">破损</Color>

艇体值耗尽时, 它会把乘员安然抛出, 并作为物品掉落, 保留全部模块和电量. 该物品处于破损状态: 使用时会提示 "艇体已破损. 请先在铁砧上修复再下水", 它的悬停提示也相同.

<Color id="gold">提示</Color>: 乘员会被丢在艇体破损的位置, 往往在深水之下. 如果你要驾驶受损的艇体, 请穿着[潜水服](nautec:getting_started/diving_gear.md).

***

## <Color id="gold">在铁砧上修复</Color>

<ItemImage id="deep_steel_plating" scale="1"/>

将艇体放入铁砧左侧槽位, 将 <ItemLink id="deep_steel_plating"/> 放入右侧. 每块镀板恢复 20% 的艇体并消耗 2 级经验, 铁砧只会使用修复所需的数量, 因此五块就能把破损的艇体修满.

这适用于任何受损的艇体物品, 不只是破损的艇体. 深海钢镀板在[深海压力锻炉](nautec:deep_engineering/pressure_forge.md)中压制. 修复材料和每件的修复量都可配置, 整合包也可能已将修复材料改为钻石.
