---
navigation:
  title: 飞行模块
  icon: nautec:flight_module
  position: 15
  parent: submarine/submarine-index.md
item_ids:
  - nautec:flight_module
---

# <Color id="light_purple">飞行模块</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="flight_module" scale="2"/>
  让海洋侦察艇离开水面并飞行.
</Column>

安装飞行模块后, 艇体离开水面时不再下坠. 它能在空中维持高度, 并以与游泳相同的方式飞行, 只是更快.

***

## <Color id="gold">飞行</Color>

它属于被动模块, 放在任意槽位都生效. 驶出水面, 或在陆地上按空格起飞, 艇体便可持续飞行.

* 转向与水下完全相同: 艇首跟随你的视线并上下俯仰, 空格上浮, C 下潜.
* 在空中, 它的移动速度快一半, 最高速度也高一半.
* 俯冲至地面或回到水中即可降落.

如果无人驾驶, 飞行中的艇体会缓缓沉向地面而不是坠落, 因此在半空中爬出不会摔坏它. 艇体永远不会受到坠落伤害.

***

## <Color id="gold">能量</Color>

当艇体载人在空中时, 维持高度会在正常运行消耗之外额外消耗每刻 4 能量. 如果在空中耗尽电池, 艇体会像其他东西一样坠落, 因此长途飞行时要留意读数.

速度加成和维持消耗可配置(`submarineFlightSpeedMultiplier`, `submarineFlightPowerUsage`). 一个模块就够, 第二个不会提供额外效果.

***

### <Color id="aqua">飞行模块配方</Color>

<Recipe id="nautec:flight_module"/>
