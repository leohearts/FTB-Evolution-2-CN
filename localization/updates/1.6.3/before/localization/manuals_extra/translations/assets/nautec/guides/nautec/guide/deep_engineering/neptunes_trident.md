---
navigation:
  title: 海王三叉戟
  icon: nautec:neptunes_trident
  position: 6
  parent: deep_engineering/deep_engineering-index.md
item_ids:
  - nautec:neptunes_trident
---

# <Color id="light_purple">海王三叉戟</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="neptunes_trident" scale="2"/>
  一把不会损坏的三叉戟, 会返回你身边, 并在命中处释放潮汐冲击波.
</Column>

海王三叉戟的功能类似原版三叉戟, 但伤害更高. 它永不损坏, 并总是以忠诚 III 的速度飞回你身边. 按住使用键再松开即可投掷; 用它攻击则进行近战.

***

## <Color id="gold">伤害</Color>

| 攻击 | 伤害 |
|---|---|
| 投掷 | 18 |
| 近战 | 19(攻击速度 1.2) |
| 激流旋转 | 18 |

近战挥击会像剑一样横扫, 命中目标旁边的生物.

***

## <Color id="gold">潮汐冲击波</Color>

投出的三叉戟命中的第一个东西, 无论是生物还是方块, 都会在那里释放潮汐冲击波. 一道闪电会显示其爆发位置; 该闪电只是视觉效果, 不会引发火焰.

* 它会命中 5 格范围内的所有东西, 中心造成 14 点伤害, 边缘降至 7 点, 并将它们从中心击退.
* 每级锋利增加 3 点伤害. 每级击退会增强推力.
* 它不会命中你, 你已驯服的宠物, 你的队友, 或处于创造或旁观模式的玩家.
* 释放一次冲击波后, 三叉戟需要 3 秒才能再次释放. 在此期间你仍可继续投掷; 这些投掷只会命中, 不会产生冲击波. 三叉戟的物品栏槽位会显示剩余时间.

范围, 伤害, 每级加成和冷却都在 `config/nautec-common.toml` 中(`tridentShockwaveRadius`, `tridentShockwaveDamage`, `tridentShockwaveDamagePerSharpness`, `tridentShockwaveKnockback`, `tridentShockwaveKnockbackPerLevel`, `tridentShockwaveCooldown`).

***

## <Color id="gold">附魔</Color>

它可接受三叉戟附魔和剑类附魔:

* 穿刺, 激流和引雷
* 锋利, 亡灵杀手, 节肢杀手, 击退, 火焰附加, 抢夺和横扫之刃
* 消失诅咒

忠诚已内置, 它永远不需要耐久或经验修补. 与任何三叉戟一样, 锋利, 亡灵杀手, 节肢杀手和穿刺中只能附上一种. 其中锋利还会提高冲击波伤害. 激流和引雷不能同时附上.

附有激流时, 在水中或雨中使用它会使你向前突进, 而不是将其投出, 因此激流三叉戟不会释放冲击波. 引雷会在雷暴期间对开阔天空下的目标召唤真正的闪电, 与原版三叉戟相同.

它的附魔能力很低, 因此请在铁砧上使用附魔书, 而不要使用附魔台.

***

## <Color id="gold">获取</Color>

该配方使用来自[共鸣室](resonance_chamber.md)和[深海压力锻炉](pressure_forge.md)的材料, 因此请先让两者都运转起来. 见[深海材料](materials.md).

<Recipe id="nautec:neptunes_trident"/>
