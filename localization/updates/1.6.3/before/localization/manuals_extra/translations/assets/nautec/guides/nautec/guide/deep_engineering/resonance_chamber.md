---
navigation:
  title: 共鸣室
  icon: nautec:resonance_chamber
  position: 1
  parent: deep_engineering/deep_engineering-index.md
item_ids:
  - nautec:resonance_chamber
---

# <Color id="light_purple">共鸣室</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="resonance_chamber" scale="2"/>
  将激光束储存为充能, 并在充能达到临界水平时进行合成.
</Column>

共鸣室将<ItemLink id="prismarine_crystal_shard"/>转化为共鸣碎片, 并为[水晶培育](crystal_cultivation.md)将休眠晶种唤醒为海晶晶种. 它需要纯度 3.0 或更高的光束. 它可从四个侧面和顶部接收光束.

***

## <Color id="gold">充能与上限</Color>

当输入光束每 tick 至少携带 20 AP 时(`resonancePowerUsage`), 共鸣室每 tick 都会将光束的全部功率加入充能. 低于该值时, 充能会流失.

上限是共鸣室能安全容纳的充能量. 它为 2,000 x (1 + 纯度), 因此纯度 3.0 的光束给出的上限为 8,000. 基础值 2,000 是 `config/nautec-common.toml` 中的 `resonanceBaseCeiling`.

| 充能 | 发生什么 |
|---|---|
| 低于上限的 90% | 继续充能 |
| 90% 到 110%(临界) | 若可以, 合成一个物品, 然后充能降为零 |
| 高于 110% | 排气 |

在纯度 3.0 时, 临界区间为 7,200 到 8,800 充能. 40 AP 的光束需要 180 tick(9 秒)达到该区间.

***

## <Color id="gold">合成</Color>

在充能达到临界之前放入海棱水晶碎片. 每次进入临界状态时, 共鸣室会消耗一份碎片, 在其输出中放入一份共鸣碎片, 并重新从零开始充能, 因此一整组碎片可以自行完成.

手持碎片右键点击可装入. 它只接受能用于其配方的物品, 无论手动还是自动化. 空手右键点击可取出输出, 输出为空时则取出输入. 漏斗和管道可插入碎片并抽出共鸣碎片, 例如在下方放一个漏斗. 默认每个面都允许两者; [侧面配置](nautec:getting_started/utilities.md)可更改.

透过<ItemLink id="prism_monocle"/>看向它, 可看到充能占上限的百分比, 上限本身以及光束纯度. 进入临界时充能会变成金色.

***

## <Color id="gold">排气</Color>

如果充能超过上限的 110%, 共鸣室会排气. 4 格范围内的所有生物受到 8 点伤害, 共鸣室会破裂 10 秒, 期间没有充能也无法合成. 它不会损坏.

当它达到临界却无法合成时就会排气, 情况包括:

* 输入槽为空
* 光束纯度低于 3.0
* 输出槽已满

保持输出为空, 或在下方放一个漏斗, 并在碎片用完时关闭光束. 光束强度是安全的: 从低于 90% 上升的充能会在进入临界区间的那个 tick 停在上限的 100%, 无论光束多强.

排气伤害, 范围和冷却分别是 `config/nautec-common.toml` 中的 `resonanceVentDamage`, `resonanceVentRadius` 和 `resonanceVentCooldown`.

***

## <Color id="gold">获得纯度 3.0</Color>

从侧面击中的<ItemLink id="prismarine_crystal"/>会发出 3.0. 将它直接对准共鸣室, 或通过海晶石激光中继器和激光转接器将光束传到那里, 它们不会改变纯度. [聚焦透镜](beam_optics.md)只能将纯度提升到 2.0, 因此在这里没有帮助.

***

### <Color id="aqua">共鸣室配方</Color>

<Recipe id="nautec:resonance_chamber"/>

***

## <Color id="gold">更强的光束</Color>

共鸣室本身就会每 tick 将光束的全部功率加入充能, 因此更强的光束会按正比加快充能: 光束翻倍, 速度也翻倍. 它不使用其他机器遵循的平方根规则.

关于该规则及其适用的每台机器, 见[更强的光束](nautec:getting_started/stronger_beams.md).
