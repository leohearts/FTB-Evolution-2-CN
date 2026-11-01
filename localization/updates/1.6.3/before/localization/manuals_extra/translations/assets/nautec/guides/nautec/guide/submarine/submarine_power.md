---
navigation:
  title: 能量与空气
  icon: nautec:prismatic_battery
  position: 2
  parent: submarine/submarine-index.md
---

# <Color id="light_purple">能量与空气</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="prismatic_battery" scale="2"/>
  电池为哪些项目供能.
</Column>

海洋侦察艇的所有设备都由一块 1,000,000 能量的电池驱动: 推进, 乘员的空气以及每个模块.

***

## <Color id="gold">运行消耗</Color>

只有有人在艇上时, 艇体才会耗电. 空艇无论停靠还是漂流, 都会保留电量.

| 在艇上时 | 每刻能量 |
|---|---|
| 静止 | 1 |
| 移动 | 再增加 6 |
| 为乘员供氧 | 再增加 2 |
| 飞行, 装有[飞行模块](flight_module.md) | 再增加 4 |

载人航行的艇体每刻消耗 9, 因此满电电池可支持约一个半小时的航行. 模块也使用同一块电池, 且每次使用的消耗高得多, 所以频繁使用模块的潜航会更快耗尽电量(见[模块](submarine_modules.md)).

这些数值都可配置. 创造模式下的驾驶员不消耗能量.

***

## <Color id="gold">空气</Color>

只要电池还有电, 艇体就保持密封, 无论潜得多深, 艇上所有人都能保持满空气条.

电池归零时, 密封也随之失效. 读数显示 CHG, 推进器停止工作, 你的空气会像正常游泳一样开始消耗. 在此之前浮出水面或抵达[海洋侦察艇船坞](submarine_dock.md), 或者穿上[潜水服](nautec:getting_started/diving_gear.md)作为后备.

艇体本身不会溺水.

***

## <Color id="gold">充能</Color>

| 来源 | 速率 | 从空到满 |
|---|---|---|
| [海洋侦察艇船坞](submarine_dock.md) | 每刻 40 | 约 21 分钟 |
| <ItemLink id="charger"/>(艇体作为物品) | 光束提供的功率, 最高每刻 128 | 128 AP 时约 6 分半钟, 光束较弱时更长 |
| [太阳能模块](solar_module.md) | 白天每 5 秒 2,000(约每刻 20) | 约 42 分钟 |

船坞是给艇体补充能量的实用方式: 停好, 离开, 再回来. 充能器需要先把艇体收起, 充能速度取决于供给它的光束: 40 AP 的光束与船坞相当, 更强的光束则更快. 太阳能模块无论是否有人在艇上都会工作, 因此白天停在开阔水域的艇体会自行充能.
