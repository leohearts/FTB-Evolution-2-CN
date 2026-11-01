---
navigation:
  title: 海洋侦察艇船坞
  icon: nautec:submarine_dock
  position: 4
  parent: submarine/submarine-index.md
item_ids:
  - nautec:submarine_dock
---

# <Color id="light_purple">海洋侦察艇船坞</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="submarine_dock" scale="2"/>
  为停靠艇体充能的平台.
</Column>

海洋侦察艇船坞可为停在其上方的海洋侦察艇充能, 固定空艇, 并为乘员供氧.

***

## <Color id="gold">搭建</Color>

船坞是一个低矮的平台, 可以放在水下. 从任意一侧用至少 20 AP 的激光束为其供能(见[激光供能](nautec:getting_started/laser_power.md)). 光束只需存在: 船坞不会消耗它, 因此无论光束多强, 艇体的充能速率都相同.

将艇体停在平台上方. 当艇体与平台正上方 3×3 区域重叠, 最高 3 格时, 即视为停靠. 船坞固定时会发出咔哒声, 艇体离开或光束低于 20 AP 时会松开. 透过 <ItemLink id="prism_monocle"/> 观察平台, 可看出是否有海洋侦察艇停靠.

***

## <Color id="gold">功能</Color>

* 在 20 AP 光束下以每刻 40 能量为艇体充能, 从空到满约 21 分钟, 无需收起艇体. 更强的光束充能更快(见下文). 该速率可配置.
* 固定空艇, 这样你留在平台上的艇体在你回来时仍在原处. 驾驶员始终可以覆盖固定, 直接驶离.
* 即使艇体电池耗尽, 也能用船坞的能量维持艇上所有人呼吸.

***

### <Color id="aqua">海洋侦察艇船坞配方</Color>

<Recipe id="nautec:submarine_dock"/>

***

## <Color id="gold">更强的光束</Color>

潜艇船坞需要 20 AP. 更强的光束能让停靠的潜艇充能更快: 速度是(光束 ÷ 20)的平方根.

| 光束 | 速度 |
|---|---|
| 20 AP | ×1(正常) |
| 80 AP | ×2 |
| 180 AP | ×3 |
| 320 AP | ×4 |

在 20 AP 光束下它每刻充 40 能量, 80 AP 时每刻 80, 以此类推.

规则及其适用的所有机器见[更强的光束](nautec:getting_started/stronger_beams.md).
